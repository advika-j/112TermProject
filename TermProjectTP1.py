from cmu_112_graphics import *

#=====================DF===========================#

#Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, '5')


#=========================dijkstra========================#
#This function uses the dijsktras backtracking algorithm to find the 
# shortest path: 


# Pseudo Code ideas for dijsktras# 
#https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode- concepts from 
#there 
''''def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path
'''
#Create a graph class that creates a graph with nodes being the rooms and edges
# being the distances. 
class Vertex(object):
    def __init__(self,node):
        self.node=node
        self.adjacent={}
        self.length= float('inf')
    
    def getNode(self):
        return self.node

    def addAdjacent(self,other,distance):
        self.adjacent[other]=distance
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.node) + ' adjacent: ' + str([x.node for x in self.adjacent])



class Graph(object):
    def __init__(self):
        self.nodes={}
    def addNodes(self,node):
    #add instance into each graph node dictionary 
        self.nodes[node]=Vertex(node)
    #returns the desired node in the list( use to add to path return)
    def getNode(self,node):
        if node in self.nodes:
            return self.nodes[node]
        else:
            return None
    #Add edgedes to add distance between each distance
    def addEdge(self,start,goal,distance):
        if start and goal in self.nodes:
            self.nodes[start].addAdjacent(self.nodes[goal],distance)
            self.nodes[start].addAdjacent(self.nodes[goal],distance)
        elif start not in self.nodes:
            self.addNodes(start)
        elif goal not in self.nodes:
            self.addNodes(goal)
    def getNodes(self):
        return self.nodes.keys()

#https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php    
    def shortest(v, path):
        ''' make shortest path from v.previous'''
        if v.previous:
            path.append(v.previous.get_id())
        return shortest(v.previous, path)
   
    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

#Manually input parsed floor plan data

g = Graph()
#Wean floor plan FLOOR 1 
#===Floor I hall 100s===
g.addNodes('1000')
g.addNodes('1001')
g.addNodes('1001A')
g.addNodes('1001B')
g.addNodes('1001C')
g.addNodes('1002')
g.addNodes('1003')
g.addNodes('1003A')
g.addNodes('1004')
g.addNodes('1006')
g.addNodes('10007')
g.addNodes('1008')
g.addNodes('1009')
g.addNodes('1010')
g.addNodes('1011')
g.addNodes('1012')
g.addNodes('1013')
g.addNodes('1014')

#1000 to ---
g.addEdge('1000', '1001',4)  
g.addEdge('1000', '1002',7)  
g.addEdge('1000', '1001A',6)  
g.addEdge('1000', '1001B',5)  
g.addEdge('1000', '1004',4)  
g.addEdge('1000', '1006',4)  
g.addEdge('1000', '1009',2)  
g.addEdge('1000', '1010',2)  
g.addEdge('1000', '1011',1)  
g.addEdge('1000', '1013',1) 
g.addEdge('1000', '1014',2) 

#1002 to ----
g.addEdge('1002', '1003',1)

#1003 to ____
g.addEdge('1003','1003A',.5)

#1006 to 
g.addEdge('1006','1007',1)

#1009 to 
g.addEdge('1009','1008',.5)

#1011 to 
g.addEdge('1011','1012',1)
        
#===Floor 1 hall 1300s===

g.addNodes('1300')
g.addNodes('1301')
g.addNodes('1301')
g.addNodes('1302')
g.addNodes('1303')
g.addNodes('1305')
g.addNodes('1307')
g.addNodes('1309')
g.addNodes('1311')
g.addNodes('1312')
g.addNodes('1312A')
g.addNodes('1313')
g.addNodes('1315')
g.addNodes('1317')
g.addNodes('1318')
g.addNodes('1319')
g.addNodes('1320')
g.addNodes('1320A')
g.addNodes('1321')
g.addNodes('1322')
g.addNodes('1323')
g.addNodes('1324')
g.addNodes('1325')
g.addNodes('1326')
g.addNodes('1327')
g.addNodes('1329')
g.addNodes('1330')
g.addNodes('1331')
g.addNodes('1333')
g.addNodes('1337')
g.addNodes('1338')
g.addNodes('1340')
g.addNodes('1352')
g.addNodes('1354')
g.addNodes('1354A')
g.addNodes('1356')


#1300to ---
g.addEdge('1300', '1301',8)  
g.addEdge('1300', '1302',7)  
g.addEdge('1300', '1303',7)  
g.addEdge('1300', '1305',6)  
g.addEdge('1300', '1307',5)  
g.addEdge('1300', '1309',4)   
g.addEdge('1300', '1311',3)  
g.addEdge('1300', '1312',3)  
g.addEdge('1300', '1313',2) 
g.addEdge('1300', '1315',1) 

g.addEdge('1300', '1317',1) 
g.addEdge('1300', '1318',2)  
g.addEdge('1300', '1319',2)  
g.addEdge('1300', '1320',1)  
g.addEdge('1300', '1321',2)  
g.addEdge('1300', '1322',1)   
g.addEdge('1300', '1323',3)  
g.addEdge('1300', '1324',3)  
g.addEdge('1300', '1325',4) 
g.addEdge('1300', '1326',4) 
g.addEdge('1300', '1329',5)
g.addEdge('1300','1330',8 )
g.addEdge('1300','1331',6)
g.addEdge('1300','1333',7)
g.addEdge('1300','1340',9)

g.addEdge('1302','1352',1)
g.addEdge('1352','1312A',1)
g.addEdge('1312','1312A',1)
g.addEdge('1312A','1352',1)


g.addEdge('1320','1320A',1)
g.addEdge('1320A','1354',1)
g.addEdge('1354A','1322',1)
g.addEdge('1326','1356',1)

g.addEdge('1325','1327',1)
g.addEdge('1325','1323',1)
g.addEdge('1323','1321',1)
g.addEdge('1315','1313',1)
g.addEdge('1313','1311',1)
g.addEdge('1305','1307',1)


# 4th floor# 

g.addEdge('1302','1352',1)
g.addEdge('1352','1312A',1)
g.addEdge('1312','1312A',1)
g.addEdge('1312A','1352',1)


g.addEdge('1320','1320A',1)
g.addEdge('1320A','1354',1)
g.addEdge('1354A','1322',1)
g.addEdge('1326','1356',1)

g.addEdge('1325','1327',1)
g.addEdge('1325','1323',1)
g.addEdge('1323','1321',1)
g.addEdge('1315','1313',1)
g.addEdge('1313','1311',1)
g.addEdge('1305','1307',1)


g.addEdge('1320','1320A',1)
g.addEdge('1320A','1354',1)
g.addEdge('1354A','1322',1)
g.addEdge('1326','1356',1)

g.addEdge('1325','1327',1)
g.addEdge('1325','1323',1)
g.addEdge('1323','1321',1)
g.addEdge('1315','1313',1)
g.addEdge('1313','1311',1)
g.addEdge('1305','1307',1)



print(g.getNodes)
#======================User interface============================#
def appStarted(app):
    app.counter = 0
    app.waitingForFirstKeyPress = True
    app.start=None
    app.end=None
    app.message= None
def keyPressed(app, event):
    if (app.waitingForFirstKeyPress):
        app.waitingForFirstKeyPress = False
    else: 
        app.start= app.getUserInput('What location do you want to start from')
        app.end= app.getUserInput('What location do you want to go to  ')

    if (app.start or app.end == None):
        app.showMessage = 'You canceled!'
    else:
        app.Message=('Finding Shortest route from' + str(app.start)+'to' +str(app.end))
         
def drawBoard(app,canvas):
#Cite: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
    canvas.create_text(app.width/2, app.height/2-100,
               text="Chose your starting point and end point by pressing any key",fill='white', 
               font='Arial 20 bold')
    
    
def displayMessage(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="green")
    canvas.create_text(app.width/2, app.height/2-300,
               text=app.message,fill='white', 
               font='Arial 20 bold')
    
def redrawAll(app, canvas): 

    canvas.create_rectangle(0,0,app.width,app.height,fill="green")
    if (app.waitingForFirstKeyPress):
        canvas.create_text(app.width/2, app.height/2,
               text="CMU Access Map",fill='white', font='Arial 30 bold')
        canvas.create_text(app.width/2, app.height/2+50,
                           text='Press any key to start!',
                           font='Arial 26 bold',fill='white')
    else: 
        drawBoard(app,canvas)

runApp(width=400, height=400)



# Return a map that connects all these values#
def appStarted(app):
    app.solution=[1,0,4,5]
    app.nodes=[(200,210),(100,200),(200,230),(50,400),(200,260),(250,300),(350,200)]
    app.fill='grey'
    app.image1 = app.loadImage('weanF1.PNG')
    app.image2 = app.scaleImage(app.image1, 2/3)
def drawBoard(app,canvas):
    counter=0
    for node in app.nodes:
        
        cx,cy=node
        r=5
        if counter in app.solution:
            app.fill='red'
        else:
            app.fill='grey'
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=app.fill)
        canvas.create_text(cx, cy, text= str(counter),
                 font="Helvetica 4 bold underline")
        counter+=1
def Solution(app,canvas):
    solutionNodes=[]
    #creates line between solution nodes
    for element in app.solution:
        position=element
        solutionNodes.append(app.nodes[position])
    
    for i in range(len(solutionNodes)-1):
        canvas.create_line(solutionNodes[i][0], solutionNodes[i][1], 
        solutionNodes[i+1][0],solutionNodes[i+1][1],fill='red')  

# create lines between them '''       
def redrawAll(app, canvas): 
    canvas.create_image(400, 300, image=ImageTk.PhotoImage(app.image2))

    drawBoard(app,canvas)
    Solution(app,canvas)

runApp(width=600, height=600)

'''# Import Image of map and add nodes like shown above# 
def appStarted(app,canvas):
    url = 'https://tinyurl.com/great-pitch-gif'
        app.image1 = app.loadImage(url)
        app.image2 = app.scaleImage(app.image1, 2/3)
'def redrawAll(app, canvas):
    canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
    canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))

runApp(width=700, height=600)'''