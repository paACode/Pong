import permanentbrush
from court import DEFAULT_COURT_WIDTH, DEFAULT_COURT_HEIGHT

DEFAULT_RACKET_SIZE_ELEMENTS = 6
DEFAULT_RACKET_SIZE_PX = 20
DIRECTION_UP = 90
DIRECTION_DOWN = 270
RACKET_STEPS_PER_KEY_INPUT = int(DEFAULT_RACKET_SIZE_ELEMENTS/2)


class Player:
    def __init__(self, player_side):
        self.racket_size_elements = DEFAULT_RACKET_SIZE_ELEMENTS
        self.racket_size_px = DEFAULT_RACKET_SIZE_PX
        self.racket_element_max_y_coordinate = DEFAULT_COURT_HEIGHT/2 - DEFAULT_RACKET_SIZE_PX
        self.score = 0
        if player_side == "right":
            self.position = (DEFAULT_COURT_WIDTH / 2 - self.racket_size_px, 0)
        elif player_side == "left":
            self.position = (-DEFAULT_COURT_WIDTH/2 + self.racket_size_px, 0)
        else:
            print("Warning: Could not create Player, because left and right was not chosen correctly")
        self.racket = self.create_racket()

    def create_racket(self):
        brush = permanentbrush.PermanentBrush()
        brush.set_color("magenta")
        brush.set_brush_size(DEFAULT_RACKET_SIZE_PX)
        racket_size_px = self.racket_size_elements * brush.brush_size_px
        start_point = (self.position[0], self.position[1] - racket_size_px / 2)
        stop_point = (self.position[0], self.position[1] + racket_size_px / 2)
        racket = brush.draw_line(start_point, stop_point)
        return racket

    def racket_sideline_reached(self, sideline):
        if sideline == "top":
            top_racket_element = self.racket[self.racket_size_elements - 1]
            if top_racket_element.ycor() < self.racket_element_max_y_coordinate:
                return False
        elif sideline == "bottom":
            bottom_racket_element = self.racket[0]
            if abs(bottom_racket_element.ycor()) < self.racket_element_max_y_coordinate:
                return False
        return True

    def racket_up(self):
        # RACKET_STEPS_PER_KEY_INPUT: Allows to adjust Racket-Speed without overshooting sideline with racket
        # --> Better Game-Parameters can be found much easier like this
        for _ in range(RACKET_STEPS_PER_KEY_INPUT):
            if not self.racket_sideline_reached("top"):
                for racket_element in self.racket:
                    racket_element.setheading(DIRECTION_UP)
                    racket_element.forward(self.racket_size_px)

    def racket_down(self):
        # RACKET_STEPS_PER_KEY_INPUT: Allows to adjust Racket-Speed without overshooting sideline with racket
        # --> Better Game-Parameters can be found much easier like this
        for _ in range(RACKET_STEPS_PER_KEY_INPUT):
            if not self.racket_sideline_reached("bottom"):
                for racket_element in self.racket:
                    racket_element.setheading(DIRECTION_DOWN)
                    racket_element.forward(self.racket_size_px)


