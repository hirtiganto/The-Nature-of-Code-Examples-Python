# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Flow Field Following
# Via Reynolds: http://www.red3d.com/cwr/steer/FlowFollow.html
from flowfield import FlowField
from vehicle import Vehicle

def setup():
    size(640, 360)

    global debug
    debug = True

    # Make a new flow field with "resolution" of 20
    global flowfield
    flowfield = FlowField(20)

    # Make a whole bunch of vehicles with random maxspeed and maxforce values
    global vehicles
    vehicles = []
    for _ in range(0, 120):
        l = PVector(random(0, width), random(0, height))
        ms = random(2, 5)
        mf = random(0.1, 0.5)
        vehicles.append(Vehicle(l, ms, mf))

def draw():
    background(255)

    # Display the flowfield in "debug" mode
    if debug:
        flowfield.display()

    # Tell all the vehicles to follow the flow field
    for v in vehicles:
        v.follow(flowfield)
        v.run()

    # Instructions
    fill(0)
    text("Hit space bar to toggle debugging lines.\n" +
         "Click the mouse to generate a new flow field.", 10, height - 20)

def keyPressed():
    global debug

    if key == ' ':
        debug = not debug

def mousePressed():
    flowfield.initialize()
