import turtle

DEFAULT_BRUSH_SIZE_PX = 20
DEFAULT_BRUSH_SHAPE = "square"
DEFAULT_BRUSH_COLOR = "white"


class PermanentBrush:
    """Class to easily draw permanent (not deleted after Screen Update) elements with desired shape"""

    def __init__(self):
        self.brush_size_px = DEFAULT_BRUSH_SIZE_PX
        self.color = DEFAULT_BRUSH_COLOR
        self.shape = DEFAULT_BRUSH_SHAPE

    def set_color(self, color):
        self.color = color

    def set_brush_size(self, size_px):
        self.brush_size_px = size_px

    def set_shape(self, shape):
        self.shape = shape

    def draw_line(self, start_coordinate, stop_coordinate):
        delta_x = stop_coordinate[0] - start_coordinate[0]
        delta_y = stop_coordinate[1] - start_coordinate[1]

        if not self.divisible_by_brush_size(delta_x, delta_y):
            print("Warning! Line is not divisible by brush size!")

        nr_of_elements = int(self.get_number_of_elements(delta_x, delta_y))
        x_step = delta_x / nr_of_elements
        y_step = delta_y / nr_of_elements

        line = []
        x_coordinate = start_coordinate[0]
        y_coordinate = start_coordinate[1]

        for element in range(nr_of_elements):
            x_coordinate += x_step
            y_coordinate += y_step
            line.append(self.draw_element(x_coordinate, y_coordinate))

        return line

    def draw_rectangle(self, origin_coordinate, width_px, height_px):
        rectangle = []
        coordinate_a = (origin_coordinate[0] - width_px / 2, origin_coordinate[1] - height_px / 2)
        coordinate_b = (origin_coordinate[0] + width_px / 2, origin_coordinate[1] - height_px / 2)
        coordinate_c = (origin_coordinate[0] + width_px / 2, origin_coordinate[1] + height_px / 2)
        coordinate_d = (origin_coordinate[0] - width_px / 2, origin_coordinate[1] + height_px / 2)

        rectangle.append(self.draw_line(coordinate_a, coordinate_b))
        rectangle.append(self.draw_line(coordinate_b, coordinate_c))
        rectangle.append(self.draw_line(coordinate_c, coordinate_d))
        rectangle.append(self.draw_line(coordinate_d, coordinate_a))

    def divisible_by_brush_size(self, delta_x, delta_y):
        if delta_x % self.brush_size_px != 0:
            return False
        elif delta_y % self.brush_size_px != 0:
            return False
        return True

    def get_number_of_elements(self, delta_x, delta_y):
        number_of_x_elements = delta_x / self.brush_size_px
        number_of_y_elements = delta_y / self.brush_size_px
        return max(abs(number_of_y_elements), abs(number_of_x_elements))

    def draw_element(self, x_coordinate, y_coordinate):
        element = turtle.Turtle(self.shape)
        self.adjust_element_size(element)
        element.penup()
        element.color(self.color)
        element.setposition(x=x_coordinate, y=y_coordinate)
        return element

    def adjust_element_size(self, element):
        """Adjust Element size according to set Brush Size"""
        stretch_factor_x = self.brush_size_px / DEFAULT_BRUSH_SIZE_PX
        stretch_factor_y = self.brush_size_px / DEFAULT_BRUSH_SIZE_PX
        stretch_factor_outline = 1.0
        element.shapesize(stretch_factor_x, stretch_factor_y, stretch_factor_outline)
