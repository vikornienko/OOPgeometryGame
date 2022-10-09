"""
This script displays the coordinates of the rectangle in the terminal and checks whether
a user-specified point within this rectangle.
Returns True or False.
An image is drawn in the graphical interface.

Данный скрипт выводит в терминал координаты прямоугольника и проверяет находятся ли
указанная пользователем точка в пределах этого прямоугольника.
Возвращается True или False.
Рисуется изображение в графическом интерфейсе.
"""

# Import required modules
# Импорт необходиых модулей
import turtle
from random import randint

# Create class Point
# Создаем класс Point
class Point:
    """
    Указывает координаты точки по осям X и Y.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

# Создаем класс Прямоугольник
class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

# Create class for GUI returning.

class GUIRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        # turtle.done()

class GUIPoint(Point):
    def draw(self, canvas, size=25, color='red'):
        """

        :type canvas: object
        """
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


gui_rectanglex = GUIRectangle(
    Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400))
)

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      gui_rectanglex.point1.x, ",",
      gui_rectanglex.point1.y, "and",
      gui_rectanglex.point2.x, ",",
      gui_rectanglex.point2.y)

# Get point and area from user
user_point = GUIPoint(float(input("Guess x: ")), float(input("Guess y: ")))
# user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(gui_rectanglex))
# print("Your area was off by: ", gui_rectanglex.area() - user_area)

myturtle = turtle.Turtle()

gui_rectanglex.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
