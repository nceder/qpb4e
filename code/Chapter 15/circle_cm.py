"""circle_cm module: contains the Circle class."""
class Circle:
    """Circle class"""
    all_circles = []              #A
    pi = 3.14159
    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self):
        """determine the area of the Circle"""
        return self.__class__.pi * self.radius * self.radius

    @classmethod             #A
    def total_area(cls):              #B
        total = 0
        for c in cls.all_circles:          #C
            total = total + c.area()
        return total
        