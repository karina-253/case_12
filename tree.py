from turtle import *

def draw_tree(depth: int, size: float, angle: float) -> None:
    '''
    The function draws a colored fractal tree recursively.

    Args:
        depth (int): Depth of recursion (defines the number of branching levels)
        size (float):  Length of the current branch
        angle (float): The angle between the left and right branches

    Returns:
        None: The function only draws branches.
    '''

    if depth == 0:
        return

    colormode(255)
    green_component = 255 - int(depth * (250 / 6)) % 255
    color(0, green_component, 0)

    forward(size)

    right(angle)
    draw_tree(depth - 1, size / 2, angle)

    left(angle * 2)
    draw_tree(depth - 1, size / 2, angle)

    right(angle)
    backward(size)


def main() -> None:
    '''
    The main function of the program.
    Requests parameters from the user and initiates the drawing of the tree
    '''

    depth = int(input('Высота дерева:'))
    angle = int(input('Угол ветвления:'))

    speed(0)

    left(90)
    draw_tree(depth, 100, angle)

    done()

if __name__ == '__main__':
    main()
