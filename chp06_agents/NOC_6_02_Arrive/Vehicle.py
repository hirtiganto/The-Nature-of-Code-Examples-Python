# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# The "Vehicle" class

class Vehicle:
    position = None
    velocity = None
    acceleration = None
    r = None
    maxfroce = None # Maximum steering force
    maxspeed = None # Maximum speed
    
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector (0, -2)
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 4
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
    def arrive(self, target):
        desired = PVector.sub(target, self.position)  # A vector pointing from the position to the target
        d = desired.mag()
        
        # Scale with arbitrary damping within 100 pixels
        if d > 100:
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)
        
        # Steering = Desired minus Velocity
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)
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