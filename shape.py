class Shape:

    # Skapar figurens centrumkoordinater
    def __init__(self, x=0, y=0):
        # Kollar så att x och y är ett tal (int eller float)
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        
        self._x = x
        self._y = y

    # Returnerar objektets nuvarande x/y koordinater
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # Gör det möjligt att flytta figurens centrum i x och y led samt kontrollerar att värdena är numeriska
    # dx - förflyttning i x-led, dy - förflyttning i y-led
    def translate(self, dx, dy):
        if not isinstance(dx, (int, float)):
            raise TypeError("dx must be a number")
        if not isinstance(dy, (int, float)):
            raise TypeError("dy must be a number")
        
        self._x += dx
        self._y += dy

    # Returnerar objektet för debugging
    def __repr__(self):
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"

    # Returnerar läsbar string när man printar objektet
    def __str__(self):
        return f"{self.__class__.__name__} at ({self._x}, {self._y})"