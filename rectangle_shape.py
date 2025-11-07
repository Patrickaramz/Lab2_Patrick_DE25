from shape import Shape
import matplotlib.pyplot as plt


class Rectangle(Shape):
    #Bygger the shape för retangeln
    def __init__(self, x=0, y=0, width=1, height=1):
        super().__init__(x, y)

        # Kontrollerar att width är ett tal och inte bokstav    
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        
        # Kontrollerar att width är ett positivt tal och inte negativt
        if width <= 0:
            raise ValueError("width must be a positive number")
        

        # Kontrollerar att height är ett tal
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        
        # Kollar så att height inte är ett negativt tal
        if height <= 0:
            raise ValueError("height must be a positive number")
        
        self._width = width
        self._height = height


    @property
    def width(self):
        return self._width
    

    @property
    def height(self:)
        return self._height