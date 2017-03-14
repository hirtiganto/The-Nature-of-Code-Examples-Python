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

        nrmal = None   # I use nrmal since 'normal' appears to be a method name
        target = None
        worldRecord = 1000000

        for i in range(0, len(p.points) - 1):
            # Look at a line segment
            a = p.points[i]
            b = p.points[i + 1]

            normalPoint = self.getNormalPoint(predictpos, a, b)

            # This only works because we know our path goes from left to right
            if normalPoint.x < a.x or normalPoint.x > b.x:
                # This is something of a hacky solution, but if it's not within
                # the line segment consider the normal to just be the end of
                # the line segment (point b).
                normalPoint = b.copy()

            distance = PVector.dist(predictpos, normalPoint)
            if distance < worldRecord:
                worldRecord = distance
                nrmal = normalPoint

                # Look at the direction of the line segment so we can seek a
                # little bit ahead of the normal.
                dir = PVector.sub(b, a)
                dir.normalize()

                # "This is an oversimplification. It should be based on distance
                # to path & velocity" - said Dan Shiffman so who am I to judge?
                dir.mult(10)
                target = normalPoint.copy()
                target.add(dir)

        # Only if the distance is greater than the path's radius do we bother
        # to steer
        if worldRecord > p.radius:
            self.seek(target)

        if self.debug:
            fill(0)
            stroke(0)
            line(self.position.x, self.position.y, predictpos.x, predictpos.y)
            ellipse(predictpos.x, predictpos.y, 4, 4)

            # Draw normal position
            fill(0)
            stroke(0)
            line(predictpos.x, predictpos.y, nrmal.x, nrmal.y)
            ellipse(nrmal.x, nrmal.y, 4, 4)

            if worldRecord > p.radius:
                fill(255, 0, 0)
            noStroke()
            ellipse(target.x, target.y, 8, 8)

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
        if self.position.x > p.getEnd().x + self.r:
            self.position.x = p.getStart().x - self.r
            self.position.y = p.getStart().y + (self.position.y - p.getEnd().y)
