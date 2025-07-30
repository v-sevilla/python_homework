#Task 5: Extending a Class
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        return NotImplemented
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def distance_to(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

class Vector(Point):
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        
p1 = Point(2, 3)
p2 = Point(0, 5)
p3 = Point (0, 5)

print(f"p1: {p1}")
print(f"p1 == p2: {p1 == p2}")
print(f"p2 == p3: {p2 == p3}")
print(f"Distance from p1 to p3: {p1.distance_to(p3)}")

v1 = Vector(2, 3)
v2 = Vector(1, 5)
v3 = v1 + v2

print(f"v2: {v2}")
print(f"v1 + v2 = {v3}")