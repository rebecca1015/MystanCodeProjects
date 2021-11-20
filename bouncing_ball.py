"""
File: bouncing_ball.py
Name: Rebecca
-------------------------
A system which simulates a bouncing ball, and it operates while user clicks.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
window.add(ball, x=START_X, y=START_Y)
x = 1  # the operation times of the function 'bouncing_ball'
turn_on = 1  # the switch of the function 'bouncing_ball'


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball.filled = True
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    global ball
    global x
    global turn_on
    if turn_on == 1 and x <= 3:
        vy = 0
        turn_on = 0  # switch off
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.x >= window.width:
                break
            if ball.y >= window.height-ball.height:
                vy = -(vy * REDUCE)
            pause(DELAY)
        window.add(ball, x=START_X, y=START_Y)
        x += 1
        turn_on = 1  # switch on


if __name__ == "__main__":
    main()
