from turtle import *

def fractal_line(order: int, size: float) -> None:
    '''
    Recursively draws a fractal curve based on the Koch curve.

    Args:
        order (int): Recursion level (0 is a straight line)
        size (float): The length of the curve segment
    '''

    if order == 0:
        forward(size)
    else:
        fractal_line(order - 1, size / 2)
        left(120)
        fractal_line(order - 1, size / 2)
        right(60)
        fractal_line(order - 1, size / 2)
        left(120)
        fractal_line(order - 1, size / 2)


def spiral_composition(depth, length) -> None:
    '''
    Draws a spiral composition of fractal curves.

    Args:
        depth (int): The level of recursion for fractals
        length (float): The base length of the segment
    Returns:
        None: The function draws and does not return values.
    '''

    for ray_ind in range(6):
        up()
        goto(0, 0)

        spiral_offset = ray_ind * 15
        setheading(ray_ind * 45 + spiral_offset)
        down()

        current_size = length * (0.8 - ray_ind * 0.08)

        for fractal_small in range(2):
            fractal_line(depth, current_size / (fractal_small + 1))
            right(120 + ray_ind * 5)


def main() -> None:
    '''
      The main function of the program.
    Requests parameters from the user and draws a fractal composition.
    '''
    speed(0)
    width(1)

    depth = int(input('Глубина рекурсии (1-3): '))
    length = int(input('Длина стороны (70-180): '))

    clear()
    up()
    goto(0, 0)
    down()

    spiral_composition(depth, length)

    hideturtle()
    done()


if __name__ == '__main__':
    main()
