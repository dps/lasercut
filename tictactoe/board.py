HEADER = """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="30.0cm" height="15.0cm" viewBox="0 0 3000 1500"
     xmlns="http://www.w3.org/2000/svg" version="1.1">
"""

FOOTER = """
</svg>
"""

PX_PER_CM = 100
MARGIN_CM = 0.33
WIDTH_PX = 1500
MARGIN_PX = MARGIN_CM * PX_PER_CM
PLACE_WIDTH_PX = (WIDTH_PX - 4 * MARGIN_PX) / 3
TOTAL_OS = 0


def rect(x, y, width, height):
    print ('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="blue" stroke-width="1"/>' % (x, y, width, height))

def o(cx, cy):
    INNER_R = (PLACE_WIDTH_PX - MARGIN_PX * 6) / 2
    OUTER_R = (PLACE_WIDTH_PX - MARGIN_PX * 1) / 2
    print ('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="blue" stroke-width="1" />' % (cx, cy, INNER_R))
    print ('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="blue" stroke-width="1" />' % (cx, cy, OUTER_R))

def x(cx, cy):
    S = MARGIN_PX * 1.5
    for rotate in [0, 90, 180, 270]:
    #   print('<path transform="rotate(%d, %f, %f)" d="M %f %f m %f %f v %f q %f %f, %f %f v %f" fill="none" stroke="blue" stroke-width="1"/>' % 
    #       (rotate, cx, cy, cx, cy, -S, -S, -(PLACE_WIDTH_PX/2 - 2 * S), S, -1.5*S, 2*S, 0 , (PLACE_WIDTH_PX/2 - 2 * S)))
      print('<path transform="rotate(%d, %f, %f)" d="M %f %f m %f %f v %f a %f %f 0 0 1 %f %f v %f" fill="none" stroke="blue" stroke-width="1"/>' % 
          (rotate, cx, cy, cx, cy, -S, -S, -(PLACE_WIDTH_PX/2 - 2.2 * S), S, S, 2*S, 0 , (PLACE_WIDTH_PX/2 - 2.2 * S)))

def board():
    print HEADER
    #rect(0,0,1500,1500)
    desired_os = 0
    desired_xs = 5
    # for row in range(3):
    #     for col in range(3):
    #         # rect(MARGIN_PX * (row + 1) + row * (PLACE_WIDTH_PX),
    #         #      MARGIN_PX * (col + 1) + col * (PLACE_WIDTH_PX),
    #         #      PLACE_WIDTH_PX,
    #         #      PLACE_WIDTH_PX
    #         #      )
    #         if desired_os > 0:
    #             o(MARGIN_PX * (row + 1) + row * (PLACE_WIDTH_PX) + PLACE_WIDTH_PX / 2,
    #             MARGIN_PX * (col + 1) + col * (PLACE_WIDTH_PX) + PLACE_WIDTH_PX / 2)
    #             desired_os = desired_os - 1
    #         elif desired_xs > 0:
    #             x(MARGIN_PX * (row + 1) + row * (PLACE_WIDTH_PX) + PLACE_WIDTH_PX / 2,
    #             MARGIN_PX * (col + 1) + col * (PLACE_WIDTH_PX) + PLACE_WIDTH_PX / 2)
    #             desired_xs = desired_xs - 1
    for i in range(1,6):
        x(i*PLACE_WIDTH_PX/1.5, ((i%2)+1.5)*MARGIN_PX*5)
    print FOOTER

if __name__ == "__main__":
    board()