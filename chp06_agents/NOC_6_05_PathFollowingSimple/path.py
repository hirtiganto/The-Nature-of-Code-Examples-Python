# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Path Following

class Path:

    def __init__(self):
        # Arbitrary radius of 20
        self.radius = 20
        self.startP = PVector(0, height / 3)
        self.endP = PVector(width, 2 * height / 3)

    def display(self):
        strokeWeight(self.radius * 2)
        stroke(0, 100)
        line(self.startP.x, self.startP.y, self.endP.x, self.endP.y)

        strokeWeight(1)
        stroke(0)
        line(self.startP.x, self.startP.y, self.endP.x, self.endP.y)
