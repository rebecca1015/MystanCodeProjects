"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, window_width / 2 - paddle_width / 2, window_height - paddle_offset - paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, window_width / 2 - ball_radius, window_height / 2 - ball_radius)

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Initialize our mouse listeners
        self.turn_on = 1
        onmousemoved(self.move_paddle)
        onmouseclicked(self.reset_velocity)

        # Draw bricks
        self.brick_num = 0
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif 1 < j < 4:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif 3 < j < 6:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif 5 < j < 8:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, (brick_width + brick_spacing) * i,
                                brick_offset + (brick_height + brick_spacing) * j)
                self.brick_num += 1

    # paddle move with mouse
    def move_paddle(self, mouse):
        paddle_x = mouse.x - self.paddle.width / 2
        if paddle_x < 0:
            paddle_x = 0
        if paddle_x + self.paddle.width > self.window.width:
            paddle_x = self.window.width - self.paddle.width
        self.window.add(self.paddle, paddle_x, self.paddle.y)

    # ball velocity
    def reset_velocity(self, mouse):
        if self.turn_on == 1:
            self.turn_on = 0
            self._dx = random.randint(0, MAX_X_SPEED)
            while self._dx == 0:
                self._dx = random.randint(0, MAX_X_SPEED)
            self._dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self._dx = -self._dx

    @property
    def vx(self):
        return self._dx

    @vx.setter
    def vx(self, new_vx):
        self._dx = new_vx

    @property
    def vy(self):
        return self._dy

    @vy.setter
    def vy(self, new_vy):
        self._dy = new_vy

    # ball in the center of the window, and velocity is zero
    def reset_ball(self):
        self.turn_on = 1
        self.window.add(self.ball, self.window.width / 2 - self.ball.width / 2,
                        self.window.height / 2 - self.ball.height / 2)
        self._dx = 0
        self._dy = 0

    # ball hit the object
    def ball_on_obj(self):
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if obj1 is not None or obj2 is not None or obj3 is not None or obj4 is not None:
            return True

    # ball hit the paddle
    def ball_in_paddle(self):
        paddle_left_side = self.paddle.x
        paddle_right_side = self.paddle.x + self.paddle.width
        paddle_top = self.paddle.y
        paddle_bottom = self.paddle.y + self.paddle.height
        obj1_in_paddle = paddle_left_side <= self.ball.x <= paddle_right_side and paddle_top <= self.ball.y <= paddle_bottom
        obj2_in_paddle = paddle_left_side <= self.ball.x+self.ball.width <= paddle_right_side and paddle_top <= self.ball.y <= paddle_bottom
        obj3_in_paddle = paddle_left_side <= self.ball.x <= paddle_right_side and paddle_top <= self.ball.y+self.ball.height <= paddle_bottom
        obj4_in_paddle = paddle_left_side <= self.ball.x+self.ball.width <= paddle_right_side and paddle_top <= self.ball.y+self.ball.height <= paddle_bottom
        if obj1_in_paddle or obj2_in_paddle or obj3_in_paddle or obj4_in_paddle:
            return True

    # remove bricks
    def remove_object(self):
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if obj1 is not None:
            self.window.remove(obj1)
            self.brick_num -= 1
        elif obj2 is not None:
            self.window.remove(obj2)
            self.brick_num -= 1
        elif obj3 is not None:
            self.window.remove(obj3)
            self.brick_num -= 1
        elif obj4 is not None:
            self.window.remove(obj4)
            self.brick_num -= 1
