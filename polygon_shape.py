"""A Polygon class that draws regular polygons with turtle."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Save polygon settings and create a turtle for this polygon."""
        if not isinstance(sides, int) or isinstance(sides, bool) or sides < 3:
            raise ValueError("sides must be an integer at least 3")
        if side_length <= 0:
            raise ValueError("side_length must be positive")
        if pen_size <= 0:
            raise ValueError("pen_size must be positive")

        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen_size = pen_size
        self._angle = angle
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)

    def draw(self):
        """Draw the polygon starting from its first vertex."""
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(self._angle)
        self._pen.pencolor(self._color)
        self._pen.pensize(self._pen_size)
        self._pen.pendown()
        for _ in range(self._sides):
            self._pen.forward(self._side_length)
            self._pen.left(360 / self._sides)
        self._pen.penup()

    def move_to(self, x, y):
        """Move the polygon without leaving its old drawing behind."""
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()
