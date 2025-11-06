class Shape:
# Skapar figurens centrumkoordinater
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


# Returnerar objektets nuvaranda x/y koordinater
@property
def x(self):
    return self._y


@property
def x(self):
    return self._y

# Gör det möjligt att flytta figurens centrum i x och y led samt kontrollerar att värdena är numeriska annars skrivs felmeddelande ut.
def translate(self, dx, dy):
    if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float))
    else TypeError("dx and dy must be numbers")
