from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass  # No implementation here

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Must override abstract method
        return 3.14 * self.radius * self.radius

# shape = Shape()  # ❌ Error: Can't instantiate abstract class
circle = Circle(5)
print(circle.area())  # 78.5
