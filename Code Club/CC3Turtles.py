'''
Created on Oct 25, 2017

@author: Bryson
'''

from turtle import *
from random import randint

speed(0)
penup() #Tells the cursor to not trace
goto(-140,140) #Moves the starting cursor location from the center (0,0) to new coordinates

for step in range(21):
    write(step, align='center')
    right(90) #Rotates the cursor 90 degrees
    forward(10) #adds gap
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

cly = Turtle()
cly.color('yellow')
cly.shape('turtle')

cly.penup()
cly.goto(-160,40)
cly.pendown()

dan = Turtle()
dan.color('green')
dan.shape('turtle')

dan.penup()
dan.goto(-160,10)
dan.pendown()

for turn in range(50):
    ada.right(36)
    ada.left(36)
    cly.forward(20)
    cly.backward(20)
    dan.right(36)

for turn in range(150):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    cly.forward(randint(1,5))
    dan.forward(randint(1,5))