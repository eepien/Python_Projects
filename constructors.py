# Constructor: A function that gets called at the time of creating a class.
class Point:
    def __init__(self, x, y):  # This is a construct. Helps us create a new object.
        self.x = x             # construct initialization, self = current attribute
        self.y = y             # construct initialization

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)
print(point.y)

#we can assign new values to point.x and point.y
point.x = 11
point.y = 21
print(f"New (x,y) = ({point.x},{point.y})")

