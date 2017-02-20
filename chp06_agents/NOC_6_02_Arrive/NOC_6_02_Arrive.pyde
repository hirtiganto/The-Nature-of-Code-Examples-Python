# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# One vehicle "arrives"
# See: http://www.red3d.com/cwr/
from Vehicle import Vehicle

def setup():
    global v

    size(640, 360)
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
    v.arrive(mouse)
    v.update()
    v.display()
