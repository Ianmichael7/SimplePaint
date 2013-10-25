# Code by Ian Ford
import sys, math, random
from pyglet.gl import *
from pyglet.window import *

WIDTH = 800
HEIGHT = 600

window = pyglet.window.Window(WIDTH,HEIGHT)

print "Change the Size by pressing the buttons Z,X, and C"
print "Change the Color by pressing the buttons R,B, and G"

currentColor = [1,0,0] #Starting Color that changes as one presses R,G,B
currentSize = 1

dots = [[-100,-100]] #Array of arrays that each contain a different shape
colors = [[1,0,0]] #List of Colors for each individial drawn item
sizes = [1]

temp = [] #Temp Shape array untill the array is added into the dats array

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(len(dots)): #Prints each individual shape in dots array
        sizeDot = len(dots[i])/2
        if sizeDot > 1:
            glLineWidth(sizes[i])
            dotList = pyglet.graphics.vertex_list(sizeDot, ('v2f', dots[i]))
            curColor = colors[i]
            glColor3f(curColor[0],curColor[1],curColor[2])
            dotList.draw(GL_LINE_STRIP)
        if sizeDot == 1:
            glPointSize(sizes[i])
            dotList = pyglet.graphics.vertex_list(sizeDot, ('v2f', dots[i]))
            curColor = colors[i]
            glColor3f(curColor[0],curColor[1],curColor[2])
            dotList.draw(GL_POINTS)

    if len(temp) != 0: #prints out the shape currently being drawn
        glLineWidth(currentSize)
        glColor3f(currentColor[0],currentColor[1],currentColor[2])
        
        sizeDot = len(temp)/2
        dotList = pyglet.graphics.vertex_list(sizeDot, ('v2f', temp))
        dotList.draw(GL_LINE_STRIP)

@window.event
def on_mouse_press(x, y, button, modifiers):
    global temp, tempColors
    if button == pyglet.window.mouse.LEFT:
        temp += [x,y]

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global temp
    if buttons == pyglet.window.mouse.LEFT:
        temp += [x,y]

@window.event
def on_mouse_release(x, y, button, modifiers):
    global dots, temp, colors, tempColors, sizes
    if button == pyglet.window.mouse.LEFT:
        dots += [temp]
        colors += [currentColor]
        sizes += [currentSize]
        temp = []

@window.event
def on_key_press(key,modifiers):
    global currentColor, currentSize
    
    if key == pyglet.window.key.R: #Colors
        print "Color: RED"
        currentColor = [1,0,0]
    if key == pyglet.window.key.G:
        print "Color: GREEN"
        currentColor = [0,1,0]
    if key == pyglet.window.key.B:
        print "Color: BLUE"
        currentColor = [0,0,1]
        
    if key == pyglet.window.key.Z: #Sizes
        print "Size: 1"
        currentSize = 1
    if key == pyglet.window.key.X:
        print "Size: 2"
        currentSize = 5
    if key == pyglet.window.key.C:
        print "Size: 3"
        currentSize = 10


pyglet.app.run()
