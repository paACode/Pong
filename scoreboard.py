import turtle
from court import DEFAULT_SCREEN_HEIGHT_PX, DEFAULT_COURT_WIDTH

FONT_TYPE = "Arial"
FONT_SIZE = 40
FONT_STYLE = "normal"
COLOR = "turquoise"

class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.right_winner = " "
        self.left_winner = " "
        self.penup()
        self.color(COLOR)
        self.x_position = None
        self.y_position = DEFAULT_SCREEN_HEIGHT_PX / 2 - 4 * FONT_SIZE
        self.update_score()
        self.hideturtle()



    def update_score(self):
        self.clear()
        #Left Score
        self.x_position = -DEFAULT_COURT_WIDTH / 4
        self.goto(self.x_position, self.y_position)
        self.write(arg=f"{self.left_score} {self.left_winner}", align="center", font=(FONT_STYLE, FONT_SIZE, FONT_STYLE))
        # Right Score
        self.x_position = DEFAULT_COURT_WIDTH / 4
        self.goto(self.x_position, self.y_position)
        self.write(arg=f"{self.right_score} {self.right_winner}", align="center", font=(FONT_STYLE, FONT_SIZE, FONT_STYLE))

