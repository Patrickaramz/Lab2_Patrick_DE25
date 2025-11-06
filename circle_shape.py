# Importerar matte-funktioner och basklassen Shape
import math
from shape import Shape


# Skapar en klass som heter Circle och ärver från Shape
class Circle(Shape):

    # Bygger shapen för Circle
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)  # Kör Shape så x och y sätts

        # Kollar så radius är ett tal
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        
        # Kollar så radius inte är 0 eller negativt
        if radius <= 0:
            raise TypeError("radius must be a positive number")
        
        self._radius = radius


    @property
    def radius(self):
        # Returnerar cirkelns radie
        return self._radius

    # Beräknar area
    @property
    def area(self):
        return math.pi * self._radius ** 2
    
  # Veräknar omkrets
    @property
    def perimeter(self):
        return 2 * math.pi * self._radius
    
    # Kollar om cirkeln är en enhetscirkel
    def is_unit_circle(self):
        return self._radius == 1 and self._x == 0 and self._y == 0
