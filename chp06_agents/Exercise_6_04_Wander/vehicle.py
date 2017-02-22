# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# ported by: Jakub Pustelnik

# The "Vehicle" class (for wandering)

class Vehicle:

    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, 0)
        self.position = PVector(x, y)
        self.r = 6
        self.wandertheta = 0
        self.maxspeed = 2
        self.maxforce = 0.05
        self.debug = True

    def run(self):
        self.update()
        self.borders()
        self.display()

    # Method to update position
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)

        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)

        # Reset accelertion to 0 each cycle
        self.acceleration.mult(0)

    def wander(self):
        wanderR = 25   # Radius for our "wander circle"
        wanderD = 80   # Distance for our "wander circle"
        change = 0.3
        # Randomly change wander theta
        self.wandertheta += random(-change, change)

        # Now we have to calculate the new position to steer towards on the
        # wander circle
        circlepos = self.velocity.get()   # Start with velocity
        circlepos.normalize()   # Normalize to get heading
        circlepos.mult(wanderD)   # Multiply by distance
        circlepos.add(self.position)   # Make it relative to boid's position

        # We need to know the heading to offset wandertheta
        h = self.velocity.heading()

        xoff = wanderR * cos(self.wandertheta + h)
        yoff = wanderR * sin(self.wandertheta + h)
        circleOffSet = PVector(xoff, yoff)

        target = PVector.add(circlepos, circleOffSet)
        self.seek(target)

        # Render wandering circle, etc.
        if self.debug:
            drawWanderStuff(self.position, circlepos, target, wanderR)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        # A vector pointing from the position to the target
        desired = PVector.sub(target, self.position)

        # Scale to maximum speed
        desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)   # Limit to maximum steering force

        self.applyForce(steer)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + radians(90)

        fill(127)
        stroke(0)

        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(theta)

        beginShape(TRIANGLES)
        vertex(0, -self.r * 2)
        vertex(-self.r, self.r * 2)
        vertex(self.r, self.r * 2)
        endShape()

        popMatrix()

    # Wrap around
    def borders(self):
        if self.position.x < -self.r:
            self.position.x = width + self.r
        if self.position.y < -self.r:
            self.position.y = height + self.r
        if self.position.x > width + self.r:
            self.poxition.x = -self.r
        if self.position.y > height + self.r:
            self.position.y = -self.r

# A method just to draw the circle associated with wandering
def drawWanderStuff(position, circle, target, rad):
    stroke(0)
    noFill()
    ellipseMode(CENTER)
    ellipse(circle.x, circle.y, rad * 2, rad * 2)
    ellipse(target.x, target.y, 4, 4)
    line(position.x, position.y, circle.x, circle.y)
    line(circle.x, circle.y, target.x, target.y)
