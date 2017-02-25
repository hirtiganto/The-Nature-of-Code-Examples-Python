# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Ported by: Jakub Pustelnik

# Flow Field Following

class FlowField:

    def __init__(self, r):
        self.resolution = r   # How large is each "cell" of the flow field

        # Determine the number of columns and rows based on sketch's width and
        # height
        self.cols = int(width / self.resolution)
        self.rows = int(height / self.resolution)

        self.initialize()

    def initialize(self):
        # Reseed noise so we get a new flow field every time
        noiseSeed(int(random(10000)))

        self.field = []

        xoff = 0
        for _ in range(0, self.cols):
            yoff = 0
            y = []
            for _ in range(0, self.rows):
                theta = map(noise(xoff, yoff), 0, 1, 0, TWO_PI)

                y.append(PVector(cos(theta), sin(theta)))
                yoff += 0.1
            self.field.append(y)
            xoff += 0.1

    # Draw every vector
    def display(self):
        for x in range(0, self.cols):
            for y in range(0, self.rows):
                xres = x * self.resolution
                yres = y * self.resolution
                self.drawVector(
                    self.field[x][y], xres, yres, self.resolution - 2)

    # Renders a vector object 'v' as an arrow and a position 'x,y'
    def drawVector(self, v, x, y, scayl):
        pushMatrix()

        # Translate to position to render vector
        translate(x, y)
        stroke(0, 100)

        # Call vector heading function to get direction (note that pointing to
        # the right is a heading of 0) and rotate
        rotate(v.heading())

        # Calculate length of vector & scale it to be bigger or smaller if
        # necessary
        leng = v.mag() * scayl

        # Draw three lines to make an arrow (draw pointing up since we've
        # rotate to the proper direction)
        line(0, 0, leng, 0)

        popMatrix()

    def lookup(self, lookup):
        column = int(constrain(lookup.x / self.resolution, 0, self.cols - 1))
        row = int(constrain(lookup.y / self.resolution, 0, self.rows - 1))
        return self.field[column][row].copy()
