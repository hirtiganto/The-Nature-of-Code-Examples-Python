# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Stay Within Walls
# "Made-up" Steering behavior to stay within walls
from vehicle import Vehicle

def setup():
    global debug, d, v
    debug = True
    d = 25
    v = Vehicle(width / 2, height / 2)

    size(640, 360)

def draw():
    background(255)

    if debug:
        stroke(175)
        noFill()
        rectMode(CENTER)
        rect(width / 2, height / 2, width - d * 2, height - d * 2)

    v.boundaries(d)
    v.run()

def mousePressed():
    global debug
    debug = not debug
