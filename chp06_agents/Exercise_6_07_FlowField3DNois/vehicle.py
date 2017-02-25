# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Flow Field Following

class Vehicle:

    def __init__(self, l, ms, mf):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, 0)
        self.position = l.copy()
        self.r = 3.0
        self.maxspeed = ms
        self.maxforce = mf

    def run(self):
        self.update()
        self.borders()
        self.display()

    # Implementing Reynolds' flow field following algorithm
    # http://www.red3d.com/cwr/steer/FlowFollow.html
    def follow(self, flow):
        # What is the vector at that spot in the flow field?
        desired = flow.lookup(self.position)
        desired.mult(self.maxspeed)   # Scale it up by maxspeed

        # Steering is desired minus velocity
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)   # Limit to maximum steering force
        self.applyForce(steer)

    # Method to update position
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)

        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)

        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

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
    def borders(self):
        if self.position.x < -self.r:
            self.position.x = width + self.r
        if self.position.y < -self.r:
            self.position.y = height + self.r
        if self.position.x > width + self.r:
            self.position.x = -self.r
        if self.position.y > height + self.r:
            self.position.y = -self.r
