
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
    canvas.create_text(app.width/2, 150, text='Welcome to CMU Path Finder', font=font)
    #canvas.create_text(app.width/2, 200, text='This is a modal splash screen!', font=font)
    canvas.create_text(app.width/2, 250, text='Press any key to start', font=font)

def splashScreenMode_keyPressed(app, event):
    app.mode = 'gameMode'
##########################################
# Game Mode
##########################################

def gameMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_rectangle(0,0,app.width,app.height,fill="lightBlue")
    #canvas.create_text(app.width/2, 20, text=f'Score: {app.score}', font=font)
    canvas.create_text(app.width/2, 60, text='Provide your starting and End destination', font=font)
    canvas.create_text(app.width/2, 100, text='Press i to input the destitation coordinates!', font=font)
    
    #canvas.create_oval(app.x-app.r, app.y-app.r, app.x+app.r, app.y+app.r,
                       #fill=app.color)
    #if app.makeAnMVCViolation:
       # app.ohNo = 'This is an MVC Violation!'
    canvas.create_text(app.width/2,  app.height/2,
                       text=app.message, font=font)
def gameMode_timerFired(app):
    pass
def gameMode_mousePressed(app, event):
    pass

# DIJKSTRAS ALGORITHM# 
#==== Citations for Dijstraks. Used the following readings and examples to generate a structure for my algorithm: =====
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
    #cite: https://www.codegrepper.com/code-examples/python/how+to+find+the+minimum+value+in+a+dictionary+python
    # Used this website to find an instant way to establish the minimum value of the nodes. 

            # get smallest distance    
            minNode= min(unvisited, key=unvisited.get)  
            # iterates through all the neighbors of the mimumNode
            for neighbour in app.inputGraph[minNode]:
                print(neighbour)
                if neighbour in visited:
                    continue
                distance = unvisited[minNode] + app.inputGraph[minNode].get(neighbour)
                print(distance)
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
    if (event.key == 'i'):
         app.start= app.getUserInput('What location do you want to start from')
         if app.start==None:
             app.message='You cancelled!'
         app.end= app.getUserInput('What location do you want to go to  ')
         if app.start==None:
             app.message='You cancelled!'
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
    if (event.x>(app.width/2-50) and event.x<app.width/2+50) and (event.y>(app.height/2)and event.y< (app.height/2+100)):
         app.mode='floorMode'

def routeMode_redrawAll(app, canvas):
        font = 'Arial 26 bold'
        canvas.create_rectangle(0,0,app.width,app.height,fill="lightBlue")
        canvas.create_text(app.width/2, 150, text=f'The shortest route from {app.start} to {app.end} is:{app.solution}', font=font)
        canvas.create_rectangle(app.width/2-50,app.height/2,app.width/2+50,app.height/2+100,fill='red')
        canvas.create_text(app.width/2,app.height/2+50,text='generate map!')

######### Map Generation: ###################
def floorMode_keyPressed(app,event):
    #zooms out
    if event.key=='Up':
        app.image2 = app.scaleImage(app.image2, 2/3)
        app.r=app.r*(2/3)
    #zooms in 
    if event.key=='Down':
        app.image2 = app.scaleImage(app.image2, 3/2)
        app.r=app.r*(3/2)
    #shows the next place to  move: 
    if event.key=='Right':
        app.count+=1
    if event.key=='Left':
        app.count-=1
           
def floorMode_drawBoard(app,canvas):
    solutionSet=[]
    if app.count <len(app.solution) and app.count>-1:
        node=app.solution[app.count] 
        solutionSet.append(app.nodeLocation[node])
        for value in solutionSet:
            cx,cy=value
            canvas.create_oval(cx-app.r,cy-app.r,cx+app.r,cy+app.r,fill=app.fill)
    elif app.count>= len(app.solution):
        canvas.create_text(app.width/2, app.height/2, text= 'You reached your destination!', fill='blue')


'''def floorMode_solution(app,canvas):
    solutionNodes=[]
    #creates line between solution nodes
    for element in app.solutions:
        position=element
        solutionNodes.append(app.nodes[position])
    
    for i in range(len(solutionNodes)-1):
        canvas.create_line(solutionNodes[i][0], solutionNodes[i][1], 
        solutionNodes[i+1][0],solutionNodes[i+1][1],fill='red')  
'''
def floorMode_redrawAll(app, canvas): 
    canvas.create_rectangle(0,0,app.width,app.height,fill='lightBlue')
    canvas.create_image(600, 300, image=ImageTk.PhotoImage(app.image2))
    floorMode_drawBoard(app,canvas)

# create lines between them    
##########################################
# Main App
##########################################

def appStarted(app):
    app.mode = 'splashScreenMode'
    app.score = 0
    app.timerDelay = 50
    app.makeAnMVCViolation = False
    app.start=None
    app.message=None
    app.end=None
    app.parents=None
    app.visited=None
    app.path=None
    app.distance=0

    app.inputGraph  = {
    #First Floor
        "1000": {"1001": 4, "1001A": 6, "1001B":5,"1002":7, "1004":4,"1006":4,"1009":2,"1010":2,"1011":1,"1013":1,"1014":2},
        "1001": {"1000": 4},
        "1001A": {"1000": 6},
        "1001B": {"1000": 5},
        "1002":{"1000":7,"1003":1},
        "1003":{"1002":1,"1003A":.5},
        "1003A":{"1003":.5},
        "1004":{"1000":4},
        "1006":{"1000":4,"1007":1},
        "1007":{"1006":1},
        "1008":{"1009":.5},
        "1009":{"1000":2,"1008":.5},
        "1010":{"1000":2},
        "1011":{"1000":1,"1012":1},
        "1012":{"1000":1,"1011":1},
        "1013":{"1000":1},
        "1014":{"1000":2},
    }
# Return a map that connects all these values#
    app.nodes = ("1000", "1001", "1001A", "1001B","1001C",'1002','1003','1003A'
    ,'1004','1006','1007','1008','1009','1010','1011','1012','1013','1014')

    #app.inputNode= ["1000", "1001", "1001A", "1001B"]

    app.nodeLocation = {"1000":(250,275), "1001":(250,245), "1001A":(174,370), "1001B":(210,370)}
    app.solution= None
    app.fill='red'
    app.image1 = app.loadImage('weanF1.PNG')
    app.image2 = app.scaleImage(app.image1, 13/14)
    app.r=8
    app.count=0

runApp(width=600, height=500)


#==================Things to Finalize and improv===================
# Side scrolling for multiple levels
# allowing users to block a specific path
# improve pixel quality of the zooming in and zooming out 