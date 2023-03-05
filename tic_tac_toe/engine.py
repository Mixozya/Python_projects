playing_field = [[' ', '1', '2', '3'],
                 ['1', '-', '-', '-'],
                 ['2', '-', '-', '-'],
                 ['3', '-', '-', '-'],
                 ]


def greet_user():
    print('Welcome to tic-tac-toe!\n'
          'Please put X or 0 mark using numbers representing strings and columns.\n'
          'For example: 1 1 or 2 3. (use space between numbers).')
    print()


def print_field(field):
    for i in field:
        print(*i)
    print()


def move():
    coordinates = input('Enter coordinates: ').split()

    if len(coordinates) != 2:
        print('Too many symbols!')
        return move()

    x, y = coordinates[0], coordinates[1]

    if not x.isdigit() or not y.isdigit():
        print('Enter numbers!')
        return move()

    x, y = int(x), int(y)

    if x > 3 or y > 3:
        print('Out of range!')
        return move()

    if playing_field[x][y] != '-':
        print('Square is occupied!')
        return move()

    return x, y


def check_win():
    win = [[playing_field[1][1], playing_field[1][2], playing_field[1][3]],
           [playing_field[2][1], playing_field[2][2], playing_field[2][3]],
           [playing_field[3][1], playing_field[3][2], playing_field[3][3]],
           [playing_field[1][1], playing_field[2][1], playing_field[3][1]],
           [playing_field[1][2], playing_field[2][2], playing_field[3][2]],
           [playing_field[1][3], playing_field[2][3], playing_field[3][3]],
           [playing_field[1][1], playing_field[2][2], playing_field[3][3]],
           [playing_field[3][1], playing_field[2][2], playing_field[1][3]]]
    for i in win:
        if i == ['X', 'X', 'X']:
            print('X won!')
            return True
        if i == ['0', '0', '0']:
            print('0 won!')
            return True
    return False


def game():
    num_of_moves = 0
    print_field(playing_field)

    while True:
        if num_of_moves % 2 == 0:
            print('X to move')
            x, y = move()
            playing_field[x][y] = 'X'
            print_field(playing_field)
        else:
            print('0 to move')
            x, y = move()
            playing_field[x][y] = '0'
            print_field(playing_field)

        num_of_moves += 1

        if check_win():
            break

        if num_of_moves == 9:
            print('Draw!')
            break
