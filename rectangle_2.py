from rectangle import Rectangle, Square, Circle

# далее создаем два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

# вывод площади наших двух прямогулоьников
print(rect_1.get_area())
print(rect_2.get_area())

# далее создаем два квадрата
square_1 = Square(5)
square_2 = Square(10)
# вывод площади наших двух квадратов
print(square_1.get_area_square(),
      square_2.get_area_square())

# создаем круг
circle_1 = Circle(3)
# вывод площади круга
print(circle_1.get_area_circle())

print("***")

figures = [rect_1, rect_2, square_1, square_2, circle_1]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure,Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())

