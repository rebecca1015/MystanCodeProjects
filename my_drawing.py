"""
File: my_drawing.py
Name: Rebecca
----------------------
my drawing which is alien with ufo and planet.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GArc, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    my drawing which is alien with ufo and planet.
    """
    window = GWindow(600, 600)

    # background
    background = GRect(600, 600)
    background.filled = True
    background.color = 'khaki'
    background.fill_color = 'khaki'
    window.add(background)
    background1 = GRect(600, 170)
    background1.filled = True
    background1.color = 'gold'
    background1.fill_color = 'gold'
    window.add(background1, 0, 430)

    # alien
    # body
    body = GRect(100, 150)
    body.filled = True
    body.color = 'royalblue'
    body.fill_color = 'royalblue'
    window.add(body, 240, 220)
    # mark
    mark1 = GOval(20, 20)
    mark1.color = 'orange'
    window.add(mark1, 311, 282)
    mark2 = GOval(30, 2)
    mark2.filled = True
    mark2.color = 'yellow'
    mark2.fill_color = 'yellow'
    window.add(mark2, 306, 292)
    mark3 = GOval(4, 4)
    mark3.filled = True
    mark3.color = 'crimson'
    mark3.fill_color = 'crimson'
    window.add(mark3, 322, 285)
    mark4 = GOval(2, 2)
    mark4.filled = True
    mark4.color = 'crimson'
    mark4.fill_color = 'crimson'
    window.add(mark4, 316, 287)
    mark5 = GOval(4, 4)
    mark5.filled = True
    mark5.color = 'crimson'
    mark5.fill_color = 'crimson'
    window.add(mark5, 318, 295)
    # belt
    belt1 = GRect(100, 15)
    belt1.filled = True
    belt1.color = 'darkblue'
    belt1.fill_color = 'darkblue'
    window.add(belt1, 240, 310)
    belt2 = GRect(30, 26)
    belt2.filled = True
    belt2.color = 'darkblue'
    belt2.fill_color = 'darkblue'
    window.add(belt2, 275, 304)
    # left foot
    left_foot = GOval(70, 25)
    left_foot.filled = True
    left_foot.color = 'darkblue'
    left_foot.fill_color = 'darkblue'
    window.add(left_foot, 220, 355)
    # right foot
    right_foot = GOval(70, 25)
    right_foot.filled = True
    right_foot.color = 'darkblue'
    right_foot.fill_color = 'darkblue'
    window.add(right_foot, 290, 355)
    # pants
    pants = GPolygon()
    pants.add_vertex((290, 350))
    pants.add_vertex((285, 370))
    pants.add_vertex((295, 370))
    pants.filled = True
    pants.color = 'darkblue'
    pants.fill_color = 'darkblue'
    window.add(pants)
    # left hand
    left_hand = GOval(80, 20)
    left_hand.filled = True
    left_hand.color = 'royalblue'
    left_hand.fill_color = 'royalblue'
    window.add(left_hand, 190, 260)
    # right hand
    right_hand = GOval(80, 20)
    right_hand.filled = True
    right_hand.color = 'royalblue'
    right_hand.fill_color = 'royalblue'
    window.add(right_hand, 310, 260)
    # scarf
    scarf = GOval(120, 80)
    scarf.filled = True
    scarf.color = 'blueviolet'
    scarf.fill_color = 'blueviolet'
    window.add(scarf, 230, 200)
    # face
    face1 = GOval(180, 120)
    face1.filled = True
    face1.color = 'yellowgreen'
    face1.fill_color = 'yellowgreen'
    window.add(face1, 200, 150)
    # eyes
    eye1_1 = GOval(40, 40)
    eye1_1.filled = True
    eye1_1.color = 'white'
    eye1_1.fill_color = 'white'
    window.add(eye1_1, 220, 180)
    eye1_2 = GOval(40, 40)
    eye1_2.filled = True
    eye1_2.color = 'white'
    eye1_2.fill_color = 'white'
    window.add(eye1_2, 270, 170)
    eye1_3 = GOval(40, 40)
    eye1_3.filled = True
    eye1_3.color = 'white'
    eye1_3.fill_color = 'white'
    window.add(eye1_3, 320, 180)
    # eyeballs
    eyeball1_1 = GOval(15, 15)
    eyeball1_1.filled = True
    window.add(eyeball1_1, 245, 192)
    eyeball1_2 = GOval(15, 15)
    eyeball1_2.filled = True
    window.add(eyeball1_2, 295, 182)
    eyeball1_3 = GOval(15, 15)
    eyeball1_3.filled = True
    window.add(eyeball1_3, 345, 192)
    # horn
    triangle1 = GPolygon()
    triangle1.add_vertex((290, 100))
    triangle1.add_vertex((280, 160))
    triangle1.add_vertex((300, 160))
    triangle1.filled = True
    triangle1.color = 'yellowgreen'
    triangle1.fill_color = 'yellowgreen'
    window.add(triangle1)
    circle1 = GOval(20, 20)
    circle1.filled = True
    circle1.color = 'yellowgreen'
    circle1.fill_color = 'yellowgreen'
    window.add(circle1, 280, 100)
    # left ear
    left_ear1 = GPolygon()
    left_ear1.add_vertex((183, 170))
    left_ear1.add_vertex((183, 210))
    left_ear1.add_vertex((203, 210))
    left_ear1.filled = True
    left_ear1.color = 'yellowgreen'
    left_ear1.fill_color = 'yellowgreen'
    window.add(left_ear1)
    left_ear2 = GOval(20, 40)
    left_ear2.filled = True
    left_ear2.color = 'yellowgreen'
    left_ear2.fill_color = 'yellowgreen'
    window.add(left_ear2, 182, 200)
    # right ear
    right_ear1 = GPolygon()
    right_ear1.add_vertex((397, 170))
    right_ear1.add_vertex((397, 210))
    right_ear1.add_vertex((377, 210))
    right_ear1.filled = True
    right_ear1.color = 'yellowgreen'
    right_ear1.fill_color = 'yellowgreen'
    window.add(right_ear1)
    right_ear2 = GOval(20, 40)
    right_ear2.filled = True
    right_ear2.color = 'yellowgreen'
    right_ear2.fill_color = 'yellowgreen'
    window.add(right_ear2, 377.5, 200)
    # mouth
    mouth1 = GArc(100, 40, 180, 180)
    window.add(mouth1, 240, 225)
    mouth2 = GLine(242, 232, 237, 237)
    window.add(mouth2)
    mouth3 = GLine(338, 232, 343, 237)
    window.add(mouth3)

    # label
    label_a = GLabel('A')
    label_a.color = 'black'
    label_a.font = 'Verdana-100-bold'
    window.add(label_a, 80, 575)
    label_i = GLabel('I')
    label_i.color = 'black'
    label_i.font = 'Verdana-100-bold'
    window.add(label_i, 260, 575)
    label_n = GLabel('N')
    label_n.color = 'black'
    label_n.font = 'Verdana-100-bold'
    window.add(label_n, 440, 575)
    label_l = GLabel('L')
    label_l.color = 'dimgray'
    label_l.font = 'Verdana-100-bold'
    window.add(label_l, 170, 575)
    label_e = GLabel('E')
    label_e.color = 'dimgray'
    label_e.font = 'Verdana-100-bold'
    window.add(label_e, 345, 575)

    # ufo
    ufo0 = GOval(30, 20)
    ufo0.filled = True
    ufo0.color = 'black'
    ufo0.fill_color = 'black'
    window.add(ufo0, 70, 85)
    ufo0_1 = GRect(2, 10)
    ufo0_1.filled = True
    ufo0_1.color = 'gray'
    ufo0_1.fill_color = 'gray'
    window.add(ufo0_1, 84, 40)
    ufo0_2 = GOval(5, 5)
    ufo0_2.filled = True
    ufo0_2.color = 'gray'
    ufo0_2.fill_color = 'gray'
    window.add(ufo0_2, 82.5, 39)
    ufo1 = GOval(50, 50)
    ufo1.filled = True
    ufo1.color = 'steelblue'
    ufo1.fill_color = 'steelblue'
    window.add(ufo1, 60, 50)
    ufo2 = GPolygon()
    ufo2.add_vertex((60, 75))
    ufo2.add_vertex((30, 95))
    ufo2.add_vertex((60, 90))
    ufo2.filled = True
    ufo2.color = 'gray'
    ufo2.fill_color = 'gray'
    window.add(ufo2)
    ufo3 = GPolygon()
    ufo3.add_vertex((110, 75))
    ufo3.add_vertex((140, 95))
    ufo3.add_vertex((110, 90))
    ufo3.filled = True
    ufo3.color = 'gray'
    ufo3.fill_color = 'gray'
    window.add(ufo3)
    ufo4 = GOval(110, 10)
    ufo4.filled = True
    ufo4.color = 'gray'
    ufo4.fill_color = 'gray'
    window.add(ufo4, 30, 90)
    ufo5 = GRect(50, 20)
    ufo5.filled = True
    ufo5.color = 'gray'
    ufo5.fill_color = 'gray'
    window.add(ufo5, 60, 75)
    ufo6 = GOval(8, 8)
    ufo6.filled = True
    ufo6.color = 'gold'
    ufo6.fill_color = 'gold'
    window.add(ufo6, 81, 84)
    ufo7 = GOval(7, 7)
    ufo7.filled = True
    ufo7.color = 'gold'
    ufo7.fill_color = 'gold'
    window.add(ufo7, 64, 83.5)
    ufo8 = GOval(7, 7)
    ufo8.filled = True
    ufo8.color = 'gold'
    ufo8.fill_color = 'gold'
    window.add(ufo8, 98, 83.5)
    ufo9 = GOval(6, 6)
    ufo9.filled = True
    ufo9.color = 'gold'
    ufo9.fill_color = 'gold'
    window.add(ufo9, 50, 83)
    ufo10 = GOval(6, 6)
    ufo10.filled = True
    ufo10.color = 'gold'
    ufo10.fill_color = 'gold'
    window.add(ufo10, 112, 83.5)

    # fire
    fire1_1 = GPolygon()
    fire1_1.add_vertex((70, 120))
    fire1_1.add_vertex((65, 150))
    fire1_1.add_vertex((75, 150))
    fire1_1.filled = True
    fire1_1.color = 'yellow'
    fire1_1.fill_color = 'yellow'
    window.add(fire1_1)
    fire1_2 = GOval(10, 10)
    fire1_2.filled = True
    fire1_2.color = 'yellow'
    fire1_2.fill_color = 'yellow'
    window.add(fire1_2, 65, 145)
    fire2_1 = GPolygon()
    fire2_1.add_vertex((85, 130))
    fire2_1.add_vertex((80, 160))
    fire2_1.add_vertex((90, 160))
    fire2_1.filled = True
    fire2_1.color = 'yellow'
    fire2_1.fill_color = 'yellow'
    window.add(fire2_1)
    fire2_2 = GOval(10, 10)
    fire2_2.filled = True
    fire2_2.color = 'yellow'
    fire2_2.fill_color = 'yellow'
    window.add(fire2_2, 80, 155)
    fire3_1 = GPolygon()
    fire3_1.add_vertex((100, 120))
    fire3_1.add_vertex((95, 150))
    fire3_1.add_vertex((105, 150))
    fire3_1.filled = True
    fire3_1.color = 'yellow'
    fire3_1.fill_color = 'yellow'
    window.add(fire3_1)
    fire3_2 = GOval(10, 10)
    fire3_2.filled = True
    fire3_2.color = 'yellow'
    fire3_2.fill_color = 'yellow'
    window.add(fire3_2, 95, 145)

    # planet1
    planet1 = GOval(60, 60)
    planet1.filled = True
    planet1.color = 'darkorange'
    planet1.fill_color = 'darkorange'
    window.add(planet1, 450, 70)
    planet2 = GOval(100, 10)
    planet2.filled = True
    planet2.color = 'chocolate'
    planet2.fill_color = 'chocolate'
    window.add(planet2, 430, 100)
    planet3 = GOval(10, 10)
    planet3.filled = True
    planet3.color = 'brown'
    planet3.fill_color = 'brown'
    window.add(planet3, 465, 80)
    planet4 = GOval(8, 8)
    planet4.filled = True
    planet4.color = 'crimson'
    planet4.fill_color = 'crimson'
    window.add(planet4, 488, 85)
    planet5 = GOval(10, 10)
    planet5.filled = True
    planet5.color = 'brown'
    planet5.fill_color = 'brown'
    window.add(planet5, 480, 115)

    # planet2
    planet2_1 = GOval(40, 40)
    planet2_1.filled = True
    planet2_1.color = 'lightblue'
    planet2_1.fill_color = 'lightblue'
    window.add(planet2_1, 520, 40)
    planet2_2 = GOval(70, 8)
    planet2_2.filled = True
    planet2_2.color = 'cyan'
    planet2_2.fill_color = 'cyan'
    window.add(planet2_2, 505, 58)

if __name__ == '__main__':
    main()
