# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Path Following
# Via Reynolds: // http://www.red3d.com/cwr/steer/PathFollow.html
from path import Path
from vehicle import Vehicle

def setup():
    size(640, 360)

    newPath()

    global car1, car2
    car1 = Vehicle(PVector(0, height / 2), 2, 0.02)
    car2 = Vehicle(PVector(0, height / 2), 3, 0.05)

def draw():
    background(255)
    path.display()

    car1.follow(path)
    car2.follow(path)

    car1.run()
    car2.run()

    car1.borders(path)
    car2.borders(path)

    # Instructions
    fill(0)
    text("Hit space bar to toggle debugging lines.", 10, height - 30)

def newPath():
    global path
    path = Path()
    path.addPoint(-20, height / 2)
    path.addPoint(random(0, width / 2), random(0, height))
    path.addPoint(random(width / 2, width), random(0, height))
    path.addPoint(width + 20, height / 2)

def keyPressed():
    if key == ' ':
        car1.debug = not car1.debug
        car2.debug = not car2.debug

def mousePressed():
    newPath()
