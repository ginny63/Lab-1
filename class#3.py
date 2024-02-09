class Shape:
     def area(self):
         print(0)
        
 class Rectangle(Shape):
     def __init__(self, lenght, width):
         super().__init__()
         self.lenght = lenght
         self.width = width
        
     def area(self):
         print(self.lenght * self.width)

 rect = Rectangle(5, 20)
 rect.area()