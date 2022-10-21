i = 0 
do_you_win = None

def enter_letter():
    Left, Right, Up, Down = input("Please enter 4 different letters for left, right, up and down:").split()
    print('Use letters', Left, Right, Up, Down, 'for left, right, up and down moves.')
    return Left, Right, Up, Down

def random_number():  
    import random
    number_list = random.sample(range(0,9),9)
    return number_list

### We first consider 8-puzzle
def eight_puzzle_initial_table():
    i = 0
    initial_list = random_number()
    for num in initial_list:
        if num != 0:
            print(num,end='\t')
        else:
            print(' ',end='\t')
        if (i+1) % 3 == 0:
            print()
        i += 1
    return initial_list
def eight_puzzle_moved_table(moved_list):
    i = 0
    for num in moved_list:
        if num != 0:
            print(num,end='\t')
        else:
            print(" ",end='\t')
        if (i+1) % 3 == 0:
            print()
        i += 1

def move_number1(Left,Right,Up,Down,initial_list):
    ## We actually print down the table, which means we do not need to use 'table function' seperately.
    if initial_list[0] == 0:
        print('Enter your move:','left-',Left,'up-',Up,end='')
        move_step = input(">>")
        if move_step is Up:
            initial_list[0] = initial_list[3]
            initial_list[3] = 0
        elif move_step is Left:
            initial_list[0] = initial_list[1]
            initial_list[1] = 0

    elif initial_list[1] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'up-',Up,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[1] = initial_list[2]
            initial_list[2] = 0
        elif move_step is Right:
            initial_list[1] = initial_list[0]
            initial_list[0] = 0
        elif move_step is Up:
            initial_list[1] = initial_list[4]
            initial_list[4] = 0

    elif initial_list[2] == 0:
        print('Enter your move:','right-',Right,'up-',Up,end='')
        move_step = input(">>")
        if move_step is Right:
            initial_list[2] = initial_list[1]
            initial_list[1] = 0
        elif move_step is Up:
            initial_list[2] = initial_list[5]
            initial_list[5] = 0

    elif initial_list[3] == 0:
        print('Enter your move:','left-',Left,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[3] = initial_list[4]
            initial_list[4] = 0
        elif move_step is Up:
            initial_list[3] = initial_list[6]
            initial_list[6] = 0
        elif move_step is Down:
            initial_list[3] = initial_list[0]
            initial_list[0] = 0

    elif initial_list[4] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[4] = initial_list[5]
            initial_list[5] = 0
        elif move_step is Right:
            initial_list[4] = initial_list[3]
            initial_list[3] = 0
        elif move_step is Up:
            initial_list[4] = initial_list[7]
            initial_list[7] = 0
        else:
            initial_list[4] = initial_list[1]
            initial_list[1] = 0
    elif initial_list[5] == 0:
        print('Enter your move:','right-',Right,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Right:
            initial_list[5] = initial_list[4]
            initial_list[4] = 0
        elif move_step is Up:
            initial_list[5] = initial_list[8]
            initial_list[8] = 0
        elif move_step is Down:
            initial_list[5] = initial_list[2]
            initial_list[2] = 0

    elif initial_list[6] == 0:
        print('Enter your move:','left-',Left,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Down:
            initial_list[6] = initial_list[3]
            initial_list[3] = 0
        elif move_step is Left:
            initial_list[6] = initial_list[7]
            initial_list[7] = 0

    elif initial_list[7] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[7] = initial_list[8]
            initial_list[8] = 0
        elif move_step is Right:
            initial_list[7] = initial_list[6]
            initial_list[6] = 0
        elif move_step is Down:
            initial_list[7] = initial_list[4]
            initial_list[4] = 0

    else:
        print('Enter your move:','right-',Right,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Right:
            initial_list[8] = initial_list[7]
            initial_list[7] = 0
        elif move_step is Down:
            initial_list[8] = initial_list[5]
            initial_list[5] = 0
    return initial_list

# win1 is for 8-puzzle game
def check_whether_win1(list_we_get):
    do_you_win = None
    if list_we_get == [1,2,3,4,5,6,7,8,0]:
        do_you_win = True
    return do_you_win
def check_whether_win2(list_we_get):
    do_you_win = None
    if list_we_get ==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]:
        do_you_win = True
    return do_you_win

def eight_puzzle_game(left,right,up,down):
    count = 0
    do_you_win = None
    # left, right, up, down = enter_letter()

    initial_list = eight_puzzle_initial_table()
    while do_you_win is not True:
        moved_list = move_number1(left,right,up,down,initial_list)
        # Here we print moved table.
        eight_puzzle_moved_table(moved_list)
        # Check whether the player win.
        do_you_win = check_whether_win1(moved_list)
        count += 1
        initial_list = moved_list
    print("Congratulations!!! You solved the puzzle in", count, "moves!!!")


def random_number_fif():  # we may let num1,2... be argument
    import random
    number_list = random.sample(range(0,16),16)
    return number_list
def fif_puzzle_initial_table():
    i = 0
    initial_list = random_number_fif()
    for num in initial_list:
        if num != 0:
            print(num,end='\t')
        else:
            print(' ',end='\t')
        if (i+1) % 4 == 0:
            print()
        i += 1
    return initial_list
def fif_puzzle_moved_table(moved_list):
    i = 0
    for num in moved_list:
        if num != 0:
            print(num,end='\t')
        else:
            print(" ",end='\t')
        if (i+1) % 4 == 0:
            print()
        i += 1
def move_number2(Left,Right,Up,Down,initial_list):
    if initial_list[0] == 0:
        print('Enter your move:','left-',Left,'up-',Up,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[0] = initial_list[1]
            initial_list[1] = 0
        elif move_step is Up:
            initial_list[0] = initial_list[4]
            initial_list[4] = 0

    elif initial_list[1] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'up-',Up,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[1] = initial_list[2]
            initial_list[2] = 0
        elif move_step is Right:
            initial_list[1] = initial_list[0]
            initial_list[0] = 0
        elif move_step is Up:
            initial_list[1] = initial_list[5]
            initial_list[5] = 0

    elif initial_list[2] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'up-',Up,end='')
        move_step = input(">>")
        if move_step is Up:
            initial_list[2] = initial_list[6]
            initial_list[6] = 0
        elif move_step is Right:
            initial_list[2] = initial_list[1]
            initial_list[1] = 0
        elif move_step is Left:
            initial_list[2] = initial_list[3]
            initial_list[3] = 0

    elif initial_list[3] == 0:
        print('Enter your move:','right-',Right,'up-',Up,end='')
        move_step = input(">>")
        if move_step is Right:
            initial_list[3] = initial_list[2]
            initial_list[2] = 0
        elif move_step is Up:
            initial_list[3] = initial_list[7]
            initial_list[7] = 0
    elif initial_list[4] == 0:
        print('Enter your move:','left-',Left,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[4] = initial_list[5]
            initial_list[5] = 0
        elif move_step is Up:
            initial_list[4] = initial_list[8]
            initial_list[8] = 0
        elif move_step is Down:
            initial_list[4] = initial_list[0]
            initial_list[0] = 0
    elif initial_list[5] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[5] = initial_list[6]
            initial_list[6] = 0
        elif move_step is Right:
            initial_list[5] = initial_list[4]
            initial_list[4] = 0
        elif move_step is Up:
            initial_list[5] = initial_list[9]
            initial_list[9] = 0
        elif move_step is Down:
            initial_list[5] = initial_list[1]
            initial_list[1] = 0
    elif initial_list[6] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[6] = initial_list[7]
            initial_list[7] = 0
        elif move_step is Right:
            initial_list[6] = initial_list[5]
            initial_list[5] = 0
        elif move_step is Up:
            initial_list[6] = initial_list[10]
            initial_list[10] = 0
        elif move_step is Down:
            initial_list[6] = initial_list[2]
            initial_list[2] = 0
    elif initial_list[7] == 0:
        print('Enter your move:','right-',Right,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Right:
            initial_list[7] = initial_list[6]
            initial_list[6] = 0
        elif move_step is Up:
            initial_list[7] = initial_list[11]
            initial_list[11] = 0
        elif move_step is Down:
            initial_list[7] = initial_list[3]
            initial_list[3] = 0
    elif initial_list[8] == 0:
        print('Enter your move:','left-',Left,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[8] = initial_list[9]
            initial_list[9] = 0
        elif move_step is Up:
            initial_list[8] = initial_list[12]
            initial_list[12] = 0
        elif move_step is Down:
            initial_list[8] = initial_list[4]
            initial_list[4] = 0
    elif initial_list[9] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[9] = initial_list[10]
            initial_list[10] = 0
        elif move_step is Right:
            initial_list[9] = initial_list[8]
            initial_list[8] = 0
        elif move_step is Up:
            initial_list[9] = initial_list[13]
            initial_list[13] = 0
        elif move_step is Down:
            initial_list[9] = initial_list[5]
            initial_list[5] = 0
    elif initial_list[10] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[10] = initial_list[11]
            initial_list[11] = 0
        elif move_step is Right:
            initial_list[10] = initial_list[9]
            initial_list[9] = 0
        elif move_step is Up:
            initial_list[10] = initial_list[14]
            initial_list[14] = 0
        elif move_step is Down:
            initial_list[10] = initial_list[6]
            initial_list[6] = 0
    elif initial_list[11] == 0:
        print('Enter your move:','right-',Right,'up-',Up,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Right:
            initial_list[11] = initial_list[10]
            initial_list[10] = 0
        elif move_step is Up:
            initial_list[11] = initial_list[15]
            initial_list[15] = 0
        elif move_step is Down:
            initial_list[11] = initial_list[7]
            initial_list[7] = 0
    elif initial_list[12] == 0:
        print('Enter your move:','left-',Left,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[12] = initial_list[13]
            initial_list[13] = 0
        elif move_step is Down:
            initial_list[12] = initial_list[8]
            initial_list[8] = 0
    elif initial_list[13] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[13] = initial_list[14]
            initial_list[14] = 0
        elif move_step is Right:
            initial_list[13] = initial_list[12]
            initial_list[12] = 0
        elif move_step is Down:
            initial_list[13] = initial_list[9]
            initial_list[9] = 0
    
    elif initial_list[14] == 0:
        print('Enter your move:','left-',Left,'right-',Right,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Left:
            initial_list[14] = initial_list[15]
            initial_list[15] = 0
        elif move_step is Right:
            initial_list[14] = initial_list[13]
            initial_list[13] = 0
        elif move_step is Down:
            initial_list[14] = initial_list[10]
            initial_list[10] = 0
    else:
        print('Enter your move:','right-',Right,'down-',Down,end='')
        move_step = input(">>")
        if move_step is Right:
            initial_list[15] = initial_list[14]
            initial_list[14] = 0
        elif move_step is Down:
            initial_list[15] = initial_list[11]
            initial_list[11] = 0
    return initial_list
def fif_puzzle_game(left,right,up,down):
    count = 0
    do_you_win = None
    # left, right, up, down = enter_letter()

    initial_list = fif_puzzle_initial_table()
    while do_you_win is not True:
        moved_list = move_number2(left,right,up,down,initial_list)
        # Here we print moved table.
        fif_puzzle_moved_table(moved_list)
        # Check whether the player win.
        do_you_win = check_whether_win2(moved_list)
        count += 1
        initial_list = moved_list
    print("Congratulations!!! You solved the puzzle in", count, "moves!!!")

def main():
    print("Welcome to sliding puzzle program!")
    print("You will choose 8 or 15-puzzle to play with!")
    print("And you move the tiles with keyboard using any 4 letters of your own choice such as 'l', 'r', 'u', 'd' for left, right, up and down moves respectively.")
    left, right, up, down = enter_letter()
    # i is for looping through the game until the player end the game.
    i = 0
    while i == 0:
        pickedNum = input("Enter 1 for 8-puzzle, 2 for 15-puzzle or q to end the game:")
        if pickedNum == '1':
            eight_puzzle_game(left,right,up,down)
        elif pickedNum == '2':
            fif_puzzle_game(left,right,up,down)
        else:
            print("Thanks for playing the game! Have a nice day!!")
            break
main()