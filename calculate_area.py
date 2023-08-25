import math
class Shape():
    def calculate_area(self):
        pass

class Square(Shape):
    def calculate_area(self,side_of_length):
        return side_of_length**2

class triangle(Shape):
    def calculate_area(self,height,base):
        return 0.5*height*base

class circle(Shape):
    def calculate_area(self,radius):
        return math.pi*radius**2

side_length = float(input("Enter the side length of the square : "))
sq = Square()
print("Area of square :", sq.calculate_area(side_length))

height = float(input("Enter the height of the triangle : "))
base = float(input("Enter the base base of the triangle : "))

tr = triangle()
print("Area of triangle :", tr.calculate_area(height, base))

radius = float(input("Enter the radius of the circle : "))
cr = circle()
print("Area of circle :", cr.calculate_area(radius))

