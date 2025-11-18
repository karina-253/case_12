from turtle import *

def koch(order: int, size: float) -> None:
    '''
    The function draws a Koch curve of a given order and size recursively.

     Args:
        order (int):  The depth of the recursion (the order of the curve).
        if order=0 - straight line
        size (float): Length of the current curve segment

    Returns:
        None: The function draws and does not return values.
    '''

    if order == 0:
        forward(size)
    else:
        koch(order - 1, size / 3)
        left(60)

        koch(order - 1, size / 3)
        right(120)

        koch(order - 1, size / 3)
        left(60)

        koch(order - 1, size / 3)


def snowflake_koch(order, size) -> None:
    '''
    The function draws the Koch snowflake - three copies of the Koch curve,
    built (with the tips facing out) on the sides of a regular triangle.

    Args:
        order (int):  The depth of the recursion  for Koch curves.
        if order=0 - straight line
        size (float): Length of the current curve segment

    Returns:
        None: Функция выполняет отрисовку, не возвращает значений
    '''

    for side in range(3):
        koch(order, size)
        right(120)


def main() -> None:
    '''
    The main function of the program.
    Requests parameters from the user and draws a Koch snowflake.
    '''

    up()
    goto(-100,0)
    down()

    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))

    snowflake_koch(n, a)

if __name__ == '__main__':
    main()
