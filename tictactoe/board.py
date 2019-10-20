HEADER = """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="15.0cm" height="15.0cm" viewBox="0 0 1500 1500"
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


def rect(file, x, y, width, height):
    file.write('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="blue" stroke-width="1"/>' % (x, y, width, height))

def o(file, cx, cy):
    INNER_R = (PLACE_WIDTH_PX - MARGIN_PX * 6) / 2
    OUTER_R = (PLACE_WIDTH_PX - MARGIN_PX * 1) / 2
    file.write('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="blue" stroke-width="1" />' % (cx, cy, INNER_R))
    file.write('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="blue" stroke-width="1" />' % (cx, cy, OUTER_R))

def x(file, cx, cy):
    S = MARGIN_PX * 1.5
    for rotate in [0, 90, 180, 270]:
      file.write('<path transform="rotate(%d, %f, %f)" d="M %f %f m %f %f v %f a %f %f 0 0 1 %f %f v %f" fill="none" stroke="blue" stroke-width="1"/>' % 
          (rotate, cx, cy, cx, cy, -S, -S, -(PLACE_WIDTH_PX/2 - 2.2 * S), S, S, 2*S, 0 , (PLACE_WIDTH_PX/2 - 2.2 * S)))

def board():
    out = file("board_base.svg", "w")
    out.write(HEADER)
    rect(out, 0, 0, 1500, 1500)
    out.write(FOOTER)
    out.close()

    out = file("board_layer1.svg", "w")
    out.write(HEADER)
    rect(out, 0, 0, 1500, 1500)
    
    desired_os = 0
    desired_xs = 5
    for row in range(3):
        for col in range(3):
            rect(out, MARGIN_PX * (row + 1) + row * (PLACE_WIDTH_PX),
                 MARGIN_PX * (col + 1) + col * (PLACE_WIDTH_PX),
                 PLACE_WIDTH_PX,
                 PLACE_WIDTH_PX
                 )
            if desired_os > 0:
                o(out, MARGIN_PX * (row + 1) + row * (PLACE_WIDTH_PX) + PLACE_WIDTH_PX / 2,
                MARGIN_PX * (col + 1) + col * (PLACE_WIDTH_PX) + PLACE_WIDTH_PX / 2)
                desired_os = desired_os - 1
            elif desired_xs > 0:
                x(out, MARGIN_PX * (row + 1) + row * (PLACE_WIDTH_PX) + PLACE_WIDTH_PX / 2,
                MARGIN_PX * (col + 1) + col * (PLACE_WIDTH_PX) + PLACE_WIDTH_PX / 2)
                desired_xs = desired_xs - 1
    out.write(FOOTER)
    out.close()

    out = file("x_pieces.svg", "w")
    out.write(HEADER)

    
    # Compact Xes for different colored material
    for i in range(1, desired_xs + 1):
        x(out, i*PLACE_WIDTH_PX/1.5, ((i%2)+1.5)*MARGIN_PX*5)

    out.write(FOOTER)
    out.close()

if __name__ == "__main__":
    board()