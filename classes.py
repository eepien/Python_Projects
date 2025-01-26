# We use classes to define new types.
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()   # equates point1 to the class (or "function") Point
point1.draw()     # executes the draw part of the class
point1.move()     # executes the move part of the class

point1.x = 10
point1.y = 20
print(f"(x,y) = ({point1.x},{point1.y})")