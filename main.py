# Tic Tac Toe game

def all_the_same(elements):
   return len(elements) == elements.count(elements[0])

def get_game_result(g):
    check_list = [
        g[0],# row1
        g[1],# row2
        g[2],# row3
        [g[0][0], g[1][0], g[2][0]],# col1
        [g[0][1], g[1][1], g[2][1]],# col2
        [g[0][2], g[1][2], g[2][2]],# col3
        [g[0][0], g[1][1], g[2][2]],# cross1
        [g[0][2], g[1][1], g[2][0]] # cross2
    ]

    for x in check_list:
        if all_the_same(x):
            return x[0]
    return 0

state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

#  --- --- --- 
# |   |   |   |
#  --- --- --- 
# |   |   |   |
#  --- --- --- 
# |   |   |   |
#  --- --- --- 
def draw(st):
    s = '';
    for rowInd, row in enumerate(st):
        for x in range(0, 2):
            if x == 0:
                for y in range(0, len(st[0])):
                    s += ' ---'
                s += ' '
            else:
                for colInd, col in enumerate(row):
                    n = state[rowInd][colInd]
                    val = n == 1 and 'x' or n == 2 and 'o' or ' '
                    s += ('| ' + val + ' ')
                s += '|'
            s +='\n'
    for y in range(0, len(st[0])):
        s += ' ---'
    s += ' '
    print(s)

def init_game():
    counter = 0
    draw(state)
    while get_game_result(state) == 0:
        if counter == 9:
            print('it is a draw')
            return

        turn = counter % 2 == 0 and 1 or 2
        print('user ' + str(turn) + ' turn')
        one = input('coordinates: "row col" e.g. "1 1" ?')
        try:
            row = int(one[0]) - 1
            col = int(one[2]) - 1
            if state[row][col] == 0:
                state[row][col] = turn
                print('accepted')
                counter += 1
                draw(state)
            else:
                print('cell has been already choosen')
        except Exception as e:
            print('incorrect input. use following format: "row col" e.g "1 1" or "1 2"')
            continue
    print('player ' + str(get_game_result(state)) + ' won')

init_game()
