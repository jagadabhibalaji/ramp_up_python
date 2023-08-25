import math
class Shape():
    def calculate_area(self,*args):
        pass

class Square(Shape):
    def calculate_area(self,*args):
        if "side_length" in args:
            side_of_length = float(input("enter side_of_length value :"))
            print(f"square area: {side_of_length ** 2}")
            return
        else:
            super().calculate_area(*args)

class triangle(Square):
    def calculate_area(self,*args):
        if "base" in args[0] and "height" in args[0]:
            base=float(input("enter base value :"))
            height=float(input("enter height value :"))
            print(f"traingle area: {0.5*base*height}")
            return
        else:
            super().calculate_area(*args)

class circle(triangle):
    def calculate_area(self,*args):
        if "radius" in args:
            radius=float(input("enter radius value :"))
            print(f"circle area: { math.pi*radius**2}")
            return
        else:
            super().calculate_area(*args)


cir= circle()
d={"square":"side_length","circle":"radius","triangle":["base","height"]}
shape=input("Enter shape :")
area=cir.calculate_area(d[shape])
