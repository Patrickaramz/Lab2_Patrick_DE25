
# Importerar matte funktioner samt tar in klassen shape
import math
from shape import Shape


class Circle(Shape):

# Kör Shape klassen so att x och y stäts
    def __init__(self, x = 0, y = 0, radius = 1):
        super().__init__(x, y):

        #Kollar att radius är ett tal
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        
        # Kollar att radius inte är 0 eller negativt
        if radius <= 0:
            raise TypeError("radius must be a positive number")
        
        self._radius = radius

    @property
def radius(self):

    #Returnerar cirkelns radie
    return self._radius