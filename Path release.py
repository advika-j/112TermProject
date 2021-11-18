from cmu_112_graphics import *

from tkinter import *
import random
import math

'''def appStarted(app):
    app.solution=[1,0,4,5]
   
    app.nodes=[(100,100),(500,100),(300,350),(50,400),(50,550),(250,550),(550,500)]
    app.fill='grey'
def drawBoard(app,canvas):
    counter=0
    for node in app.nodes:
        
        cx,cy=node
        r=30
        if counter in app.solution:
            app.fill='red'
        else:
            app.fill='grey'
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=app.fill)
        canvas.create_text(cx, cy, text= str(counter),
                 font="Helvetica 26 bold underline")
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

# create lines between them 
#        
def redrawAll(app, canvas): 
    drawBoard(app,canvas)
    Solution(app,canvas)

runApp(width=600, height=600)'''

# This demos loadImage and scaleImage from a local file



    




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