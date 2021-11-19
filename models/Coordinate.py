class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Coordinate(x={self.x}, y={self.y})'