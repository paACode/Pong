from math import atan2, pi
import permanentbrush
from player import DEFAULT_RACKET_SIZE_PX
from court import DEFAULT_COURT_WIDTH, DEFAULT_COURT_HEIGHT
import random

DEFAULT_SPEED = 5  # 5 Slow , 4 Medium, 3 Fast, 2 Super Fast, 1 World Class
DEFAULT_COURT_STEP_DIVISION = 50  # Speed needs to adapt dependent on Screensize
MAX_SPEED_COURT_DIVISION = DEFAULT_COURT_STEP_DIVISION

class Ball:
    def __init__(self):
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.direction_dx = random.choice([-1, 1]) * DEFAULT_COURT_WIDTH
        self.direction_dy = random.randint(-DEFAULT_COURT_HEIGHT / 2, DEFAULT_COURT_HEIGHT / 2)
        self.direction_angle = self.calculate_direction_angle()
        self.ball = self.create()
        self.step = int(DEFAULT_COURT_WIDTH / DEFAULT_COURT_STEP_DIVISION / DEFAULT_SPEED)  # Speed needs to adapt dependent on Screensize

    def create(self):
        brush = permanentbrush.PermanentBrush()
        brush.set_shape("circle")
        brush.set_color("yellow")
        ball = brush.draw_element(self.x_coordinate, self.y_coordinate)
        return ball

    def move(self):
        self.ball.setheading(self.direction_angle)
        self.ball.forward(self.step)

    def bounce(self):
        self.direction_dy = - self.direction_dy
        self.direction_angle = self.calculate_direction_angle()

    def hit_by_racket(self):
        self.increase_speed()
        print(self.step)
        self.direction_dx = -self.direction_dx
        self.direction_angle = self.calculate_direction_angle()

    def increase_speed(self):
        self.step += 1
        print(int(DEFAULT_COURT_WIDTH / MAX_SPEED_COURT_DIVISION))
        if self.step > int(DEFAULT_COURT_WIDTH / MAX_SPEED_COURT_DIVISION):
            self.step = int(DEFAULT_COURT_WIDTH / MAX_SPEED_COURT_DIVISION)

    def set_speed_to_default(self):
        self.step = int(DEFAULT_COURT_WIDTH / DEFAULT_COURT_STEP_DIVISION / DEFAULT_SPEED)

    def calculate_direction_angle(self):
        return atan2(self.direction_dy, self.direction_dx) * 180 / pi  # allows calculating atan() of all 4 quadrants

    def set_random_direction(self, towards):
        if towards == "right":
            self.direction_dx = DEFAULT_COURT_WIDTH / 2
            self.direction_dy = random.randint(-DEFAULT_COURT_HEIGHT / 2, DEFAULT_COURT_HEIGHT / 2)
            self.direction_angle = self.calculate_direction_angle()
        elif towards == "left":
            self.direction_dx = -DEFAULT_COURT_WIDTH / 2
            self.direction_dy = random.randint(-DEFAULT_COURT_HEIGHT / 2, DEFAULT_COURT_HEIGHT / 2)
            self.direction_angle = self.calculate_direction_angle()

    def addition_move_for_bug_fix(self, nr_of_moves):
        """Bug: When the ball bounces from Sideline or Racket it returns direction and moves by a step. If step is
        not big enough in main loop the same event can occur again and the ball bounces back again and again. In
        order to avoid that additional moves can be added after ball bounces to make sure ball is far away from event
        triggering sideline or racket
        """
        for _ in range(nr_of_moves):
            self.move()

    def additional_move_to_simulate_racket_hit(self, nr_of_moves):
        for _ in range(nr_of_moves):
            self.move()