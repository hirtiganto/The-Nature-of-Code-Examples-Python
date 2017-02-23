# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/
from vehicle import Vehicle

def setup():
    size(640, 360)
    
    global v
    v = Vehicle(width / 2, height / 2)


def draw():
    background(255)

    mouse = PVector(mouseX, mouseY)

    # Draw an ellipse at the mouse position
    fill(200)
    stroke(0)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 48, 48)

    # Call the appropriate steering behaviors for our agents
    v.seek(mouse)
    v.update()
    v.display()