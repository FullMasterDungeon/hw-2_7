class Rectangle():
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        if type(length) and type(width) and type(height) not in [int, float] or length < 0 or width < 0 or height < 0:
            raise ValueError
    def calculate_volume(self):
        return self.height * self.length * self.width
        

# c = Rectangle(1, 2, 3)
# c.volume()
# print(c.calculate_volume)
