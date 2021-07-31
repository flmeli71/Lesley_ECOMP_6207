# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 03:50:31 2021

@author: Flora
"""
#import turtle module
import turtle

#define honeycomb as a turtle object
honeycomb = turtle.Turtle()

#choose black as pen color and orange as fill color
honeycomb.begin_fill()
honeycomb.color("black","orange")

#outer for loop is responsible for the honeycomb shape
for i in range(6):
    #inner for loop is responsible for each hexagon
    for n in range(6):
        honeycomb.forward(100)
        honeycomb.left(60)
    honeycomb.forward(100)
    honeycomb.right(60)

#fill in the honeycomb with orange
honeycomb.end_fill()

#conclude honeycomb drawing
turtle.done()
    