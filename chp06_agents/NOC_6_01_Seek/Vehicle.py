# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Seek_Arrive

# The "Vehicle" class

class Vehicle:

    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, -2)
        self.position = PVector(x, y)
        self.r = 6

        # Maximum speed
        self.maxspeed = 4

        # Maximum steering force
        self.maxforce = 0.1

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

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        # A vector pointing from the position to the target
        desired = PVector.sub(target, self.position)

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
