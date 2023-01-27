import turtle
import time
import ball
import court
import player
from math import sqrt
from permanentbrush import DEFAULT_BRUSH_SIZE_PX
import scoreboard

DEFAULT_COLLISION_THRESHOLD = round(sqrt((DEFAULT_BRUSH_SIZE_PX / 2) ** 2 * 2))
DEFAULT_RACKET_SIMULATION_ADDITIONAL_MOVES = 3
DEFAULT_ADDITIONAL_MOVES_WHEN_BOUNCING = 1
DEFAULT_MAX_SCORE = 3


def create_screen(title):
    screen = turtle.Screen()
    screen.setup(width=court.DEFAULT_SCREEN_WIDTH_PX, height=court.DEFAULT_SCREEN_HEIGHT_PX)
    screen.bgcolor(court.DEFAULT_BACKGROUND_COLOR)
    screen.title(title)
    screen.tracer(0)  # Turns Animation off
    return screen


def initialize_controls():
    pong_screen.listen()
    pong_screen.onkey(left_player.racket_up, "w")
    pong_screen.onkey(left_player.racket_down, "s")
    pong_screen.onkey(right_player.racket_up, "Up")
    pong_screen.onkey(right_player.racket_down, "Down")


def collision_detected(ball_pong, sideline):
    for element in sideline:
        if element.distance(ball_pong) < DEFAULT_COLLISION_THRESHOLD:
            return True
    return False


if __name__ == '__main__':

    pong_screen = create_screen(title="Pong")
    pong_court = court.Court()
    right_player = player.Player("right")
    left_player = player.Player("left")
    pong_ball = ball.Ball()
    pong_scoreboard = scoreboard.Scoreboard()
    initialize_controls()
    game_is_on = True

    while game_is_on:
        pong_screen.update()
        pong_ball.move()
        if collision_detected(pong_ball.ball, pong_court.sideline_right):
            pong_scoreboard.left_score += 1
            pong_scoreboard.update_score()
            pong_ball.ball.goto(0, 0)
            pong_ball.set_speed_to_default()
            time.sleep(3)
            pong_ball.set_random_direction(towards="left")
        elif collision_detected(pong_ball.ball, pong_court.sideline_left):
            pong_scoreboard.right_score += 1
            pong_scoreboard.update_score()
            pong_ball.ball.goto(0, 0)
            pong_ball.set_speed_to_default()
            time.sleep(3)
            pong_ball.set_random_direction(towards="right")
        elif collision_detected(pong_ball.ball, pong_court.sideline_top) or \
                collision_detected(pong_ball.ball, pong_court.sideline_bottom):
            pong_ball.bounce()
            pong_ball.addition_move_for_bug_fix(nr_of_moves=DEFAULT_ADDITIONAL_MOVES_WHEN_BOUNCING)
        elif collision_detected(pong_ball.ball, left_player.racket) or \
                collision_detected(pong_ball.ball, right_player.racket):
            pong_ball.hit_by_racket()
            pong_ball.addition_move_for_bug_fix(nr_of_moves=DEFAULT_ADDITIONAL_MOVES_WHEN_BOUNCING)
            pong_ball.additional_move_to_simulate_racket_hit(nr_of_moves=DEFAULT_RACKET_SIMULATION_ADDITIONAL_MOVES)
        elif pong_scoreboard.left_score == DEFAULT_MAX_SCORE:
            pong_scoreboard.left_winner = "Wins!!!"
            pong_scoreboard.update_score()
            game_is_on = False
        elif pong_scoreboard.right_score == DEFAULT_MAX_SCORE:
            pong_scoreboard.right_winner = "Wins!!!"
            pong_scoreboard.update_score()
            game_is_on = False
    pong_screen.exitonclick()