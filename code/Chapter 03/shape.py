"""shape module. Contains classes Shape, Square and Circle"""
class Shape:                         #1
    """Shape class: has method move"""
    def __init__(self, x, y):       #2
        self.x = x         #3
        self.y = y         #3
    def move(self, deltaX, deltaY):  #4
        self.x = self.x + deltaX
        self.y = self.y + deltaY
class Square(Shape):
    """Square Class:inherits from Shape"""
    def __init__(self, side=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.side = side
class Circle(Shape):            #5
    """Circle Class: inherits from Shape and has method area"""
    pi = 3.14159           #6
    def __init__(self, r=1, x=0, y=0):
        Shape.__init__(self, x, y)   #7
        self.radius = r
    def area(self):
        """Circle area method: returns the area of the circle."""
        return self.radius * self.radius * self.pi
    def __str__(self):                      #8
        return f"Circle of radius {self.radius} at ({self.x}, {self.y})"
