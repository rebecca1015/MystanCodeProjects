"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.vx, graphics.vy)
        if graphics.ball_in_paddle():
            graphics.vy = - abs(graphics.vy)
        elif graphics.ball_on_obj():
            graphics.vy = - graphics.vy
            graphics.remove_object()
        if graphics.ball.y > graphics.window.height:
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:  # win
                break
        if graphics.brick_num == 0:  # win
            break
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.vx = - graphics.vx
        if graphics.ball.y <= 0:
            graphics.vy = - graphics.vy


if __name__ == '__main__':
    main()
