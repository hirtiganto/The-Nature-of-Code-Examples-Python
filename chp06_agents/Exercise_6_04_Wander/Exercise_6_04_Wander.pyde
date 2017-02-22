# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# ported by: Jakub Pustelnik

# Demonstration of Craig Reynolds' "Wandering" behavior
# See: http://www.red3d.com/cwr/

# Click mouse to turn on and off rendering of the wander circle
from vehicle import Vehicle

def setup():
    size(640, 360)

    global wanderer
    wanderer = Vehicle(width / 2, height / 2)

def draw():
    background(255)
    wanderer.wander()
    wanderer.run()

def mousePressed():
    wanderer.debug = not wanderer.debug
