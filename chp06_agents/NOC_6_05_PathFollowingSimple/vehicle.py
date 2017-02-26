# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# The "Vehicle" class

class Vehicle:

    def __init__(self, l, ms, mf):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(ms, 0)
        self.position = l.copy()
        self.r = 4.0
        self.maxspeed = ms
        self.maxforce = mf
        self.debug = True

    # Main "run" function
    def run(self):
        self.update()
        self.display()

    # This function implements Craig Reynolds' path following algorithm
    # http://www.red3d.com/cwr/steer/PathFollow.html
    def follow(self, p):
        # Predict position 50 (arbitrary choice) frames ahead
        predict = self.velocity.copy()
        predict.setMag(50)
        predictpos = PVector.add(self.position, predict)

        # Look at the line segment
        a = p.startP
        b = p.endP

        # Get the normal point to that line
        normalPoint = self.getNormalPoint(predictpos, a, b)

        dir = PVector.sub(b, a)
        
        # This could be based on velocity instead of just an arbitrary 10px
        dir.setMag(10)
        target = PVector.add(normalPoint, dir)

        distance = PVector.dist(predictpos, normalPoint)
        
        # Only if the distance is greater than the path's radius do we bother
        # to steer
        if distance > p.radius:
            self.seek(target)

        if self.debug:
            fill(0)
            stroke(0)
            line(self.position.x, self.position.y, predictpos.x, predictpos.y)
            ellipse(predictpos.x, predictpos.y, 4, 4)

            # Draw normal position
            fill(0)
            stroke(0)
            line(predictpos.x, predictpos.y, normalPoint.x, normalPoint.y)
            ellipse(normalPoint.x, normalPoint.y, 4, 4)

            if distance > p.radius:
                fill(255, 0, 0)
            noStroke()
            ellipse(target.x + dir.x, target.y + dir.y, 8, 8)

    # A function to get the normal point from a point (p) to a line segment
    # (a-b)
    def getNormalPoint(self, p, a, b):
        ap = PVector.sub(p, a)
        ab = PVector.sub(b, a)

        # Project vector "diff" onto line by using the dot product
        ab.normalize()
        ab.mult(ap.dot(ab))

        return PVector.add(a, ab)

    # Method to update position
    def update(self):
        self.velocity.add(self.acceleration)

        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)

        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        # A vector pointing from the position to the target
        desired = PVector.sub(target, self.position)

        # If the x and y are equal to 0, skip out of here
        if desired.x == 0 and desired.y == 0:
            return

        # Scale to maximum speed
        desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2

        fill(127)
        stroke(0)
        strokeWeight(1)

        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(theta)

        beginShape()
        vertex(0, -self.r * 2)
        vertex(-self.r, self.r * 2)
        vertex(self.r, self.r * 2)
        endShape(CLOSE)

        popMatrix()

    # Wrap around
    def borders(self, p):
        if self.position.x > p.endP.x + self.r:
            self.position.x = p.startP.x - self.r
            self.position.y = p.startP.y + (self.position.y - p.endP.y)
