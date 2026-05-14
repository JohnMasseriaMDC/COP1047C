cr = "*"

def draw_square(size):
    draw_rect(size, size)


def draw_rect(height, width):
    for h in range(height):
        for w in range(width):
            print(cr, end="")
        print()

draw_rect(3, 7)
draw_square(5)
