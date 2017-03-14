# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Path Following

class Path:

    def __init__(self):
        # Arbitrary radius of 20
        self.radius = 20
        self.points = []

    def addPoint(self, x, y):
        self.points.append(PVector(x, y))
    
    def getStart(self):
        return self.points[0]
    
    def getEnd(self):
        return self.points[-1]

    def display(self):
        # Draw thick line for radius
        stroke(175)
        noFill()
        strokeWeight(self.radius * 2)
        beginShape()
        for v in self.points:
            vertex(v.x, v.y)
        endShape()
        
        # Draw thin line for center of path
        stroke(0)
        strokeWeight(1)
        beginShape()
        for v in self.points:
            vertex(v.x, v.y)
        endShape()
