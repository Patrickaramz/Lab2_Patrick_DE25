# Importerar matte-funktioner och basklassen Shape
import math
from shape import Shape
import matplotlib.pyplot as plt


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
            raise ValueError("radius must be a positive number")
        
        self._radius = radius


    @property
    def radius(self):
        return self._radius


    # Beräknar area
    @property
    def area(self):
        return math.pi * self._radius ** 2
    

    # Beräknar omkrets
    @property
    def perimeter(self):
        return 2 * math.pi * self._radius
    

    # Kollar om cirkeln är en enhetscirkel
    def is_unit_circle(self):
        return self._radius == 1 and self._x == 0 and self._y == 0


    # Jämför två cirklar baserat på radien (lika med)
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self._radius == other._radius
    

    # Mindre än
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return False
        return self._radius < other._radius
    

    # Större än
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return False
        return self._radius > other._radius
    

    # Mindre än eller lika med
    def __le__(self, other):
        if not isinstance(other, Circle):
            return False
        return self._radius <= other._radius
    

    # Större än eller lika med
    def __ge__(self, other):
        if not isinstance(other, Circle):
            return False
        return self._radius >= other._radius


    # Returnerar representation för debuggning
    def __repr__(self):
        return f"Circle(x={self._x}, y={self._y}, radius={self._radius})"
    

    # Returnerar användarvänlig beskrivning
    def __str__(self):
        return f"Circle with center at ({self._x}, {self._y}) and radius {self._radius}"
    

