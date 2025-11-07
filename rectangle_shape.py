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
        

        # Kontrollerar att height är et tall
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")