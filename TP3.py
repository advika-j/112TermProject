
# This demos using modes (aka screens).

from cmu_112_graphics import *
import random

##########################################
# Splash Screen Mode
##########################################

#Citation: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
# used the multimode and images notes from cmu 112

def splashScreenMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_rectangle(0,0,app.width,app.height,fill="lightBlue")
    canvas.create_text(app.width/2, 150, text='Welcome to Wean Path Finder',
     font=font)
    #canvas.create_text(app.width/2, 200, text='This is a modal splash screen!',
    #  font=font)
    canvas.create_text(app.width/2, 250, text='Press any key to start',font=font)

def splashScreenMode_keyPressed(app, event):
    app.mode = 'gameMode'
##########################################
# Game Mode
##########################################

def gameMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_rectangle(0,0,app.width,app.height,fill="lightBlue")
    #canvas.create_text(app.width/2, 20, text=f'Score: {app.score}', font=font)
    canvas.create_text(app.width/2, app.height/2-40, 
    text='Provide your starting and end destination', font=font)
    canvas.create_text(app.width/2, app.height/2, 
    text='Press i to input the room numbers!', font=font)
    
    canvas.create_text(app.width/2,  app.height/2,
                       text=app.message, font=font)
def gameMode_timerFired(app):
    pass
def gameMode_mousePressed(app, event):
    pass

# DIJKSTRAS ALGORITHM# 
#==== Citations for Dijstraks. Used the following readings and 
# examples to generate a structure for my algorithm: =====
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
#https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
def gameMode_findRoute(app):
       # Make starting distance for node point infinity 
        unvisited=dict()
        for n in app.nodes:
            unvisited[n]= float("inf")
      
        # Assign the starting node to 0 
        unvisited[app.start] = 0  
        # list of all visited nodes
        visited = dict() 
        # previously seen that we are moving from 
        parents = dict() 
        print(unvisited)
        while True:
    #cite: 
    # https://www.codegrepper.com/code-examples/python/how+to+find+the+minimum+value+in+a+dictionary+python
    # Used this website to find an instant way to establish the minimum value of the nodes. 

            # get smallest distance    
            minNode= min(unvisited, key=unvisited.get)  
            # iterates through all the neighbors of the mimumNode
            for neighbour in app.inputGraph[minNode]:
               
                if neighbour in visited:
                    continue
                
                distance = unvisited[minNode] + app.inputGraph[minNode].get(neighbour)
                print(distance,unvisited[neighbour],neighbour)
                

                if distance < unvisited[neighbour]:
                    unvisited[neighbour] = distance
                    parents[neighbour] = minNode
            visited[minNode] = unvisited[minNode]
            #remove node from unvistited as we are done with looking at it
            unvisited.pop(minNode)
            if minNode == app.end:
                break
            
        app.distance=visited[app.end]
        app.parents=parents
        app.visited=visited

def gameMode_generatePath(app):
        path = [app.end]
        while True:
            key = app.parents[path[0]]
            #reversing order to print first visted node 
            path.insert(0, key)
            if key == app.start:
                break
        app.solution=path

def gameMode_keyPressed(app, event):
#Takes input from user to determine the starting and ending position desired
    if (event.key == 'i'):
         app.start= app.getUserInput('What location do you want to start from')
         if app.start==None:
             app.message='You cancelled!'
         app.end= app.getUserInput('What location do you want to go to  ')
         if app.start==None:
             app.message='You cancelled!'
         if (app.start or app.end) not in app.inputGraph:
            app.message=='these rooms do not exsist. Please try again!'
            app.mode='splashScreenMode'
        

         gameMode_findRoute(app)
         gameMode_generatePath(app)
        
         app.mode='routeMode'
   

##########################################
# Shortest Route generation
##########################################

def routeMode_keyPressed(app, event):
     if event.key=='g':
        if app.getUserInput('Do you want a map generation')== 'yes':
            app.mode='floorMode'  
def routeMode_mousePressed(app,event):
    #user can click generate map button
    if (event.x>(app.width/2-50) and event.x<app.width/2+50) and (event.y>(app.height/2)and event.y< (app.height/2+100)):
         app.mode='floorMode'

def routeMode_redrawAll(app, canvas):
        font = 'Arial 26 bold'
        canvas.create_rectangle(0,0,app.width,app.height,fill="lightBlue")
        canvas.create_text(app.width/2, 150, text=f'Finding the shortest route from room {app.start} to room {app.end}', font=font)
        canvas.create_rectangle(app.width/2-50,app.height/2,
        app.width/2+50,app.height/2+100,fill='green')
        canvas.create_text(app.width/2,app.height/2+50,text='generate map!')

######### Map Generation: ###################

def floorMode_appStarted(app):
    app.image = None
    app.image1 = app.loadImage('weanF1.PNG')
    app.scale=5/6
    app.image2 = app.scaleImage(app.image1, app.scale) 
    app.floor2= app.loadImage('WeanF2.PNG')
    app.floor2Scaled = app.scaleImage(app.floor2, app.scale)
    app.r=5
    app.count=0
    app.move=1
    app.snapshotImage=None

def floorMode_keyPressed(app,event):
    #zooms out

    #shows the next place to  move: 
    if event.key=='Right':
        app.count+=100
        app.help -=10
    if event.key=='Left':
        app.count-=100
        app.help+=10
    if event.key=='Up':
            if app.image==None:
                snapshotImage = app.getSnapshot()
                app.image = app.scaleImage(snapshotImage, 5/6)
            app.scale+=(1/6)
            app.move+=(1/6)
            app.image2=app.scaleImage(app.image,app.scale)
    #Cite:https://www.gmai.cmu.edu/~112/notes/notes-animations-part4.html#getAndSaveSnapshot
    #zooms in 
    if event.key=='Down':
            if app.image==None:
                snapshotImage = app.getSnapshot()
                app.image = app.scaleImage(snapshotImage, 5/6)
            app.scale-=(1/6)
            app.move-=(1/6)
            app.image2=app.scaleImage(app.image,app.scale )
    #undo:
    if event.key=='u':
        floorMode_appStarted(app)
    #restart game:
    if event.key=='r':
        appStarted(app)
    if event.key=='n':
        app.move+=1
    if event.key=='b':
        app.move-=1
    if event.key=='h':
        app.mode='helpMode'
def floorMode_mousePressed(app,event):
    if event.x<150+app.help and event.x>100+app.help and event.y<750 and event.y>700:
        app.mode='helpMode'


           
def floorMode_drawBoard(app,canvas):
    for element in app.nodeLocation:
            cx,cy= app.nodeLocation[element]
            canvas.create_oval(cx+app.count+app.r,cy+app.r,cx+app.count-app.r,cy-app.r,fill='grey')
def floorMode_solution(app,canvas):
    solutionNodes=[]
    #creates line between solution nodes
    for position in app.solution:
        solutionNodes.append(app.nodeLocation[position])
    
    for i in range(len(solutionNodes)-1):
        canvas.create_line(solutionNodes[i][0]+app.count, solutionNodes[i][1], 
        solutionNodes[i+1][0]+app.count,solutionNodes[i+1][1],fill='red')  

def floorMode_move(app,canvas):
    solutionSet=[]
    if app.move <len(app.solution) and app.move>-1:
        node=app.solution[app.move] 
        solutionSet.append(app.nodeLocation[node])
        if node==('1001A' or '1001B' or '1001C' or '1330' or '2001A'or '2001B' or '2001C' or '2330'):
            node='elevator'
        canvas.create_text(app.width/2+app.count,600,text=f'current location: {node}')
        for value in solutionSet:
            cx,cy=value
            canvas.create_oval(cx+app.count-app.r,cy-app.r,cx+app.count+app.r,cy+app.r,fill=app.fill)
    elif app.move>= len(app.solution):
        font = 'Arial 26 bold'
        canvas.create_rectangle(2,2,app.width,app.height,fill='black')
        canvas.create_text(app.width/2, app.height/2, text= 'You reached your destination!',fill='white',font=font)


def floorMode_redrawAll(app, canvas): 
    canvas.create_rectangle(0,0,app.width,app.height,fill='lightBlue')
    if app.image==None:
       
        canvas.create_image(500+app.count, 300, image=ImageTk.PhotoImage(app.image2))
        canvas.create_image(1600+app.count, 300, image=ImageTk.PhotoImage(app.floor2))
        canvas.create_rectangle(100+app.help,700,150+app.help,750,fill='red')
        canvas.create_text(125+app.help,725,text="help")
        


        floorMode_drawBoard(app,canvas)
        floorMode_solution(app,canvas)
        floorMode_move(app,canvas)
    else: 
        canvas.create_image(500+app.count, 300, image=ImageTk.PhotoImage(app.image2))

# create lines between them 
##########################################
#Help Mode
##########################################   
def helpMode_redrawAll(app, canvas): 
    canvas.create_rectangle(0,0,app.width,app.height,fill='grey')
    canvas.create_text(app.width/2, app.height/4, text= 'The followinng keys perform these actions:')
    canvas.create_text(app.width/2, app.height/4+30, text= '[Up]: Zooms out')
    canvas.create_text(app.width/2, app.height/4+60, text= '[Down]:zooms out')
    canvas.create_text(app.width/2, app.height/4+90, text= '[u]: undos the zoom and goes back to original')
    canvas.create_text(app.width/2, app.height/4+120, text= '[Left]: moves the map left')
    canvas.create_text(app.width/2, app.height/4+150, text= '[Right]: moves the map Right')
    canvas.create_text(app.width/2, app.height/4+180, text= '[n]: shows next coordinate')
    canvas.create_text(app.width/2, app.height/4+210, text= '[b]: moves back a step')
    canvas.create_text(app.width/2, app.height/4+240, text= ' [r]: restarts whole simulation')

    canvas.create_rectangle(400,600,500,700,fill='purple')
    canvas.create_text(450,650,text='return')

def helpMode_mousePressed(app,event):
    if event.x<500 and event.x>400 and event.y<700 and event.x>400:
        app.mode='floorMode'
        floorMode_appStarted(app)


##########################################
# Main App
##########################################


def appStarted(app):
    app.mode = 'splashScreenMode'
    
    app.start=None
    app.message=None
    app.end=None
    app.parents=None
    app.visited=None
    app.path=None
    app.distance=0
    app.image = None
#Citation for weanF1 image: https://cmu.app.box.com/s/1anow0tytv4fdceamh9vzzyxn7vysulu

    app.image1 = app.loadImage('weanF1.PNG')
    app.scale=5/6
    app.image2 = app.scaleImage(app.image1, app.scale) 
#Citation for wean floor 2 image: https://cmu.app.box.com/s/ac858q3ngochp35xiccl5f5f7wr9ucv3
    app.floor2= app.loadImage('WeanF2.PNG')
    app.floor2Scaled = app.scaleImage(app.floor2, app.scale)
    app.r=5
    app.count=0
    app.move=1
    app.snapshotImage=None
    app.solution= None
    app.fill='red'
    app.move=0
#Citation for help button image: https://www.google.com/search?q=help+button+transparent&tbm=isch&ved=2ahUKEwjWxN6Pq8D0AhXtlnIEHQO0AmgQ2-cCegQIABAA&oq=help+button+tra&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQ6BAgAEEM6BAgAEBhQsQJYmgZgtw1oAHAAeACAAX6IAZ8DkgEDNC4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=fTqmYZaSB-2tytMPg-iKwAY&bih=683&biw=1061#imgrc=vigsyUeoGKTM7M

    app.help = 0

    

    app.inputGraph  = {
    #First Floor
        "1000": {"1011": 1, "1013": 1, "1004Door":1.5,"1014Door":4},
        "1000A":{"1004Door":3,"1001":1,"1001C":1},
        "1001": {"1000": 4,"1000A":1},
        "1001A": {"1001B":1,"1002Door":1,"2001A":.1},
        "1001B": {"1001A": 1,"1001C": 1,"2001B":.1},
        "1001C": {"1000A": 1,"1001B":1,"2001C":.1},
        "1002":{"1002Door":1,"1003":1},
        "1002Door":{"1001A":.3,"1002":1},
        "1003":{"1002":1},
        "1003A":{"1003":.5},
        "1004":{"1004Door":1},
        "1004Door":{"1000":1.5,"1000A":4,"1004":1},
        "1006":{"1010Door":1,"1007":1},
        "1007":{"1006":1},
        "1008":{"1009":.5},
        "1009":{"1008":.5,"1010Door":1,"1011":1,"1013":1.2},
        "1010":{"1010Door":1},
        "1010Door":{"1006":1,"1009":1,"1010":1,"1013":.5},
        "1011":{"1000":1,"1012":1,"1009":1},
        "1012":{"1011":1},
        "1013":{"1009":1.2,"1011":.5,"1000":1},
        "1014Door":{"1000":4,"1014":1,"1301":1},
        "1014":{"1014":1,"1301":1},
        #1300s
        "1301":{"1014Door":1, "1302Door":1,"1303":1},
        "1302Door":{ "1301":1,"1302":1},
        "1302":{ "1302Door":1,"1352":1,"1303":1},
        "1352":{ "1302":1},
        "1303":{ "1301":1,"1302":1,"1305Door":1},
        "1305Door":{ "1303":1,"1305":.5, "1307Door":1},
        "1305":{ "1305Door":.5,"1307":.5},
        "1307":{"1305":.5,"1307Door":.2},
        "1307Door":{"1307":.2,"1305Door":1,"1309":1},
        "1309":{"1307Door":1,"1312":1,"1311Door":1},
        "1312":{"1309":12,"1312A":1},
        "1312A":{"1312":1},
        "1311Door":{"1309":1,"1311":1,"1318":1,"1313Door":1},
        "1311":{"1311Door":1,"1313":1},
        "1313Door":{"1311Door":1,"1313":1,"1315Door":1},
        "1313":{"1313Door":1,"1311":1,"1315":1},
        "1315":{"1315Door":1,"1313":1},
        "1315Door":{"1313Door":1,"1315":1,"1320":1,"1317":1},
        "1318":{"1311Door":1},
        "1320":{"1315Door":1},
        "1320A":{"1320":1,"1354":1},
        "1354":{"1320A":1,"1322":1}, 
        "1317":{"1315Door":1,"1319":1},
        "1319":{"1317":1,"1322":1.5,"1321Door":1},
        "1322":{"1319":1.5,"1354":1},
        "1321Door":{"1319":1,"1321":1,"1323Door":1},
        "1321":{"1321Door":1,"1323":1},
        "1323":{"1325":1,"1323Door":1,"1321":1},
        "1323Door":{"1323":1,"1325Door":1, "1324":1,"1321Door":1},
        "1325":{"1323":1,"1325Door":.5,"1327":1},
        "1325Door":{"1325":.5,"1323Door":1,"1326":1,"1329":1},
        "1327":{"1325":1},
        "1324":{"1323Door":1},
        "1326":{"1325Door":1,"1326Door":1,"1356":1},
        "1356":{"1326":1},
        "1329":{"1325":1,"1331":.2},
        "1331":{"1329":.2,"1333":.2},
        "1333":{"1331":.2},
        "1326Door":{"1326":1,"1330":1,"1340":.5},
        "1330":{"1326Door":1,"2330":.1},
        "1340":{"1326Door":.5},

    #2nd Floor: 
       "2000":{"2001A":1,"2001B":1,"2001C":1,"2002A":1,"2016A":1},
       "2016A":{"2000":1,"2016":1},
       "2001A":{"2000":1,"1001A":.1,},
       "2001B":{"2000":1,"1001B":.1},
       "2001C":{"2000":1,"1001C":.1},
       "2002A":{"2000":1,"2002":1},
       "2002":{"2002A":1,"2221":1,"2005":1},
       "2221":{"2002":1,"2201A":1},
       "2201A":{"2221":1,"2201":1},
       "2201":{"2201A":1,"2201B":1},
       "2201B":{"2201":1,"2202":1},
       "2202":{"2201B":1,"2203":1},
       "2005":{"2002":1,"2016":1,"2009":1,"2011":1,"2006":1},
       "2006":{"2005":1},
       "2009":{"2005":1,"2008":1},
       "2008":{"2009":1},
       "2011":{"2005":1,"2012":1},
       "2012":{"2011":1},
       "2016":{"2005":1,"2016A":1,"2014Door":1},
       "2014Door":{"2016":1,"2014":1,"2301":1},
       "2014":{"2014Door":1,"2015":1},
       "2015":{"2014":1},
       "2203Door":{"2202":1,"2203":1},
       "2203":{"2203Door":1,"2204":1,"2206":1},
       "2206":{"2203":1,"2207":1},
       "2207":{"2206":1,"2208":1},
       "2208":{"2207":1},
       "2204":{"2203":1},
       "2301":{"2014Door":1, "2303Door":1,"2302Door":1},
       "2302Door":{"2301":1,"2302":1},
       "2302":{"2302Door":1,"2352":1},
       "2303Door":{"2301":1,"2303":1,"2305Door":1},
       "2303":{"2303Door":1,"2305":1},
       "2305":{"2303":1,"2305Door":1,"2307":1},
       "2307":{"2305":1,"2307Door":1},
       "2305Door":{"2305":1,"2303Door":1},
       "2307Door":{"2307":1,"2309":1},
       "2309":{"2307Door":1,"2311Door":1,"2310":1},
       "2311Door":{"2309":1,"2311":1,"2313Door":1},
       "2311":{"2311Door":1,"2313":1},
       "2313":{"2311":1,"2313Door":1},
       "2313Door":{"2311Door":1,"2313":1,"2315Door":1},
       "2310":{"2309":1,"2352":1,"2314":1},
       "2314":{"2310":1,"2315Door":1,"2354":1},
       "2315Door":{"2314":1,"2313Door":1,"2315":1,"2317":1},
       "2315":{"2315Door":1},
       "2317":{"2315":1,"2318":1,"2319Door":1},
       "2318":{"2317":1,"2354":1,"2323Door":1},
       "2319Door":{"2317":1,"2319":1,"2321Door":1},
       "2319":{"2319Door":1,"2321":1},
       "2321":{"2319":1,"2321Door":1,"2323":1},
       "2321Door":{"2321":1,"2319Door":1,"2323Door":1},
       "2323Door":{"2318":1,"2321Door":1,"2323":1,"2324Door":1},
       "2323":{"2323Door":1},
       "2324Door":{"2323Door":1,"2324":1,"2325Door":1},
       "2325Door":{"2324Door":1,"2325":1,"2329":1,"2331":1},
       "2331":{"2325Door":1,"2333":1},
       "2333":{"2331":1,"2334Door":1,"2324":1},
       "2334Door":{"2333":1,"2334":1,"2340":1,"2330":1},
       "2330":{"2334Door":1,"1330":.1},
       "2340":{"2334Door":1},
       "2329":{"2325Door":1},
       "2325":{"2325Door":1,"2327":1},
       "2327":{"2325":1},
       "2324":{"2324Door":1,"2356":1,"2333":1},
       "2356":{"2324":1,"2334":1},
       "2334":{"2356":1,"2338":1,"2334Door":1},
       "2338":{"2334":1},
       "2354":{"2318":1,"2314":1},
       "2352":{"2310":1,"2302":1}

    }



# Return a map that connects all these values#
    
   
    
    app.nodes = (
     #1st floor- 100 hallway    
    "1000","1000A", "1001", "1001A", "1001B","1001C",'1002','1002Door','1003',
    '1003A','1004','1004Door','1006','1007','1008','1009','1010','1010Door',
    '1011','1012','1013','1014','1014Door',
    
    #1st floor- 300 hall way:

    "1301","1302","1302Door","1352","1303","1305Door","1305","1307Door",
    "1307","1309","1312","1312A","1311Door","1311","1313Door","1313","1315Door"
    ,"1315","1318","1320","1320A","1354","1317","1319","1322","1321Door","1321"
    ,"1323","1323Door","1324","1325","1325Door","1326","1327","1356","1329",
    "1331","1333","1326Door","1330","1340",
    #SECOND FLOOR: 

    "2000","2001A","2001B","2001C","2002A","2002","2005","2006","2008","2009",
    "2011","2012","2015","2016","2014","2016A","2014Door","2221","2201A","2201B"
    ,"2201","2202","2203Door","2203","2204","2206","2207","2208","2301",
    "2302Door", "2302","2352","2303Door","2303","2305","2305Door","2307",
    "2307Door","2309","2311","2311Door","2313","2313Door","2310","2314",
    "2315","2315Door","2317","2319Door","2319","2321","2321Door","2323",
    "2323Door","2325","2325Door","2324Door","2324","2356","2318","2354",
    "2325","2329","2331","2333","2334","2334Door","2330","2340","2338","2327"

    
    )

    #app.inputNode= ["1000", "1001", "1001A", "1001B"]
    app.count=0

    app.nodeLocation = {"1000":(215,280), 
    "1000A":(215,390),
    "1001":(180,390), 
    "1001A":(120,390),
     "1001B":(150,390),
     "1001C":(180,390),
     "1002Door":(120,405),
    "1002":(90,405),
    "1003":(80,355),
    "1004Door":(215,320)
    ,"1004":(175,320),
    "1006":(90,260),
     "1007":(85,310),
     "1008":(125,230),
     "1009":(130,270),
    "1010Door":(110,270),
    "1010":(110,320),
    "1011":(180,270),  
    "1012":(180,220),
    "1013":(170,290),
    "1014Door":(215,190),
    "1014":(160,190),
    #1300s:
    "1301":(250,190),
    "1302Door":(285,190),
    "1302":(285,230),
    "1352":(315,300),
    "1303":(285,190),
    "1305Door":(310,190),
    "1305":(310,160), 
    "1307Door":(330,190)
    ,"1307":(335,160),
    "1309":(380,190),
    "1312":(390,250),
    "1312A":(390,290),
    "1311Door":(410,190),
    "1311":(410,160),
    "1313Door":(440,190),
    "1313":(440,160),
    "1315Door":(480,190),
    "1315":(480,160),
    "1318":(430,220),
    "1320":(490,250),
    "1320A":(480,290), 
    "1354":(520,300),
    "1317":(520,190),
    "1319":(550,190),
    "1322":(560,250),
    "1321Door":(580,190),
    "1321":(590,160),
    "1323":(630,160),
    "1323Door":(630,190)
    ,"1325":(660,160),
    "1325Door":(660,190),
    "1324":(630,220),
    "1326":(690,260),
    "1356":(700,300),
    "1329":(690,190),
    "1331":(710,190),
    "1333":(730,190),
    "1327":(690,100),
    "1326Door":(780,190),
    "1330":(780,150),
    "1340":(800,195),

    #====2nd floor=====
    "2000":(1560,380),
    "2001A":(1525,350),
    "2001B":(1555,350),
    "2001C":(1575,350),
    "2002A":(1510,389),
    "2002":(1510,300),
    "2005":(1559,288),
    "2006":(1560,330),
    "2009":(1550,270),
    "2008":(1550,245),
    "2011":(1570,270),
    "2012":(1570,245),
    "2015":(1550,210),
    "2014":(1570,210),
    "2016":(1605,288),
    "2016A":(1605,380),
    "2014Door":(1600,220),
    "2221":(1480,280),
    "2201A":(1480,244),
    "2201":(1340,244), 
    "2201B":(1200,244),
    "2202":(1220,344),
    "2203Door":(1230,410),
    "2203":(1200,410),
    "2204":(1200,380),
    "2206":(1100,410),
    "2207":(1110,370),
    "2208":(1150,370),
    "2301":(1630,220),
    "2302Door":(1630,220),
    "2302":(1670,270),
    "2352":(1690,300),
    "2303Door":(1660,220),
    "2303":(1655,195),
    "2305":(1675,195),
    "2305Door":(1675,220),
    "2307":(1705,195),
    "2307Door":(1705,220),
    "2309":(1725,220),
    "2311Door":(1755,220),
    "2311":(1755,195),
    "2313":(1785,195),
    "2313Door":(1785,220),
    "2310":(1755,260),
    "2314":(1785,260),
    "2315":(1815,195),
    "2315Door":(1815,220),
    "2317":(1835,220),
    "2319Door":(1865,220),
    "2319":(1865,195),
    "2321":(1885,195),
    "2321Door":(1885,220),
    "2323Door":(1915,220),
    "2323":(1915,195),
    "2325Door":(1965,220),
     "2324Door":(1945,220),
     "2324":(1955,260),
    "2356":(1995,300),
    "2318":(1870,260),
    "2354":(1860,300),
    "2325":(1945,195),
    "2329":(1995,175),
    "2331":(1995,220),
    "2333":(2015,220),
    "2334":(2050,260),
    "2334Door":(2050,220),
    "2330":(2050,180),
    "2340":(2080,220),
    "2338":(2090,270),
    "2327":(1995,155)
                      }

runApp(width=1000, height=780)


#==================Things to Finalize and improv===================
# Side scrolling for multiple levels
# allowing users to block a specific path
# improve pixel quality of the zooming in and zooming out 