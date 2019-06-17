import random
import sys
import threading


# Cube sides are numbered 0 - 8 starting from top left of each side's top-left and
# 8 being the center piece (never changing)
#
# Cube is always facing white side with blue on top

white_side = []
blue_side = []
orange_side = []
green_side = []
red_side = []
yellow_side = []

cube_state = [white_side, blue_side, orange_side, green_side, red_side, yellow_side]

cube_solved = True
moves = ["r", "rp", "r2", "l", "lp", "l2", "u", "up", "u2", "d", "dp", "d2", "f" , "fp", "f2", "b", "bp", "b2"]
move_counter = 0
solution = []

# Standard Rotations. No return value. They modify the lists for each side

def rotate_f(i):
    f = 0
    while f < i:
        temp_white = list.copy(cube_state[0])
        cube_state[0][0] = temp_white[6]
        cube_state[0][1] = temp_white[7]
        cube_state[0][2] = temp_white[0]
        cube_state[0][3] = temp_white[1]
        cube_state[0][4] = temp_white[2]
        cube_state[0][5] = temp_white[3]
        cube_state[0][6] = temp_white[4]
        cube_state[0][7] = temp_white[5]

        temp_blue = list.copy(cube_state[1])
        temp_orange = list.copy(cube_state[2])
        temp_green = list.copy(cube_state[3])
        temp_red = list.copy(cube_state[4])

        cube_state[1][4] = temp_orange[4]
        cube_state[1][5] = temp_orange[5]
        cube_state[1][6] = temp_orange[6]

        cube_state[4][4] = temp_blue[4]
        cube_state[4][5] = temp_blue[5]
        cube_state[4][6] = temp_blue[6]

        cube_state[3][4] = temp_red[4]
        cube_state[3][5] = temp_red[5]
        cube_state[3][6] = temp_red[6]

        cube_state[2][4] = temp_green[4]
        cube_state[2][5] = temp_green[5]
        cube_state[2][6] = temp_green[6]

        f += 1

def rotate_r(i):
    f = 0
    while f < i:
        temp_red = list.copy(cube_state[4])
        cube_state[4][0] = temp_red[6]
        cube_state[4][1] = temp_red[7]
        cube_state[4][2] = temp_red[0]
        cube_state[4][3] = temp_red[1]
        cube_state[4][4] = temp_red[2]
        cube_state[4][5] = temp_red[3]
        cube_state[4][6] = temp_red[4]
        cube_state[4][7] = temp_red[5]

        temp_blue = list.copy(cube_state[1])
        temp_yellow = list.copy(cube_state[5])
        temp_green = list.copy(cube_state[3])
        temp_white = list.copy(cube_state[0])

        cube_state[1][2] = temp_white[2]
        cube_state[1][3] = temp_white[3]
        cube_state[1][4] = temp_white[4]

        cube_state[5][2] = temp_blue[2]
        cube_state[5][3] = temp_blue[3]
        cube_state[5][4] = temp_blue[4]

        cube_state[3][6] = temp_yellow[2]
        cube_state[3][7] = temp_yellow[3]
        cube_state[3][0] = temp_yellow[4]

        cube_state[0][2] = temp_green[6]
        cube_state[0][3] = temp_green[7]
        cube_state[0][4] = temp_green[0]

        f += 1
        
def rotate_l(i):
    f = 0
    while f < i:
        temp_orange = list.copy(cube_state[2])
        cube_state[2][0] = temp_orange[6]
        cube_state[2][1] = temp_orange[7]
        cube_state[2][2] = temp_orange[0]
        cube_state[2][3] = temp_orange[1]
        cube_state[2][4] = temp_orange[2]
        cube_state[2][5] = temp_orange[3]
        cube_state[2][6] = temp_orange[4]
        cube_state[2][7] = temp_orange[5]

        temp_blue = list.copy(cube_state[1])
        temp_yellow = list.copy(cube_state[5])
        temp_green = list.copy(cube_state[3])
        temp_white = list.copy(cube_state[0])

        cube_state[0][0] = temp_blue[0]
        cube_state[0][7] = temp_blue[7]
        cube_state[0][6] = temp_blue[6]

        cube_state[1][0] = temp_yellow[0]
        cube_state[1][7] = temp_yellow[7]
        cube_state[1][6] = temp_yellow[6]

        cube_state[5][0] = temp_green[4]
        cube_state[5][7] = temp_green[3]
        cube_state[5][6] = temp_green[2]

        cube_state[3][4] = temp_white[0]
        cube_state[3][3] = temp_white[7]
        cube_state[3][2] = temp_white[6]

        f += 1

def rotate_u(i):
    f = 0
    while f < i:
        temp_blue = list.copy(cube_state[1])
        cube_state[1][0] = temp_blue[6]
        cube_state[1][1] = temp_blue[7]
        cube_state[1][2] = temp_blue[0]
        cube_state[1][3] = temp_blue[1]
        cube_state[1][4] = temp_blue[2]
        cube_state[1][5] = temp_blue[3]
        cube_state[1][6] = temp_blue[4]
        cube_state[1][7] = temp_blue[5]

        temp_red = list.copy(cube_state[4])
        temp_yellow = list.copy(cube_state[5])
        temp_orange = list.copy(cube_state[2])
        temp_white = list.copy(cube_state[0])

        cube_state[2][2] = temp_white[0]
        cube_state[2][3] = temp_white[1]
        cube_state[2][4] = temp_white[2]

        cube_state[5][4] = temp_orange[2]
        cube_state[5][5] = temp_orange[3]
        cube_state[5][6] = temp_orange[4]

        cube_state[4][6] = temp_yellow[4]
        cube_state[4][7] = temp_yellow[5]
        cube_state[4][0] = temp_yellow[6]

        cube_state[0][0] = temp_red[6]
        cube_state[0][1] = temp_red[7]
        cube_state[0][2] = temp_red[0]

        f += 1
        
def rotate_d(i):
    f = 0
    while f < i:
        temp_green = list.copy(cube_state[3])
        cube_state[3][0] = temp_green[6]
        cube_state[3][1] = temp_green[7]
        cube_state[3][2] = temp_green[0]
        cube_state[3][3] = temp_green[1]
        cube_state[3][4] = temp_green[2]
        cube_state[3][5] = temp_green[3]
        cube_state[3][6] = temp_green[4]
        cube_state[3][7] = temp_green[5]

        temp_red = list.copy(cube_state[4])
        temp_yellow = list.copy(cube_state[5])
        temp_orange = list.copy(cube_state[2])
        temp_white = list.copy(cube_state[0])

        cube_state[4][2] = temp_white[4]
        cube_state[4][3] = temp_white[5]
        cube_state[4][4] = temp_white[6]

        cube_state[5][0] = temp_red[2]
        cube_state[5][1] = temp_red[3]
        cube_state[5][2] = temp_red[4]

        cube_state[2][6] = temp_yellow[0]
        cube_state[2][7] = temp_yellow[1]
        cube_state[2][0] = temp_yellow[2]

        cube_state[0][4] = temp_orange[6]
        cube_state[0][5] = temp_orange[7]
        cube_state[0][6] = temp_orange[0]

        f += 1
        
def rotate_b(i):
    f = 0
    while f < i:
        temp_yellow = list.copy(cube_state[5])
        cube_state[5][0] = temp_yellow[6]
        cube_state[5][1] = temp_yellow[7]
        cube_state[5][2] = temp_yellow[0]
        cube_state[5][3] = temp_yellow[1]
        cube_state[5][4] = temp_yellow[2]
        cube_state[5][5] = temp_yellow[3]
        cube_state[5][6] = temp_yellow[4]
        cube_state[5][7] = temp_yellow[5]

        temp_red = list.copy(cube_state[4])
        temp_green = list.copy(cube_state[3])
        temp_orange = list.copy(cube_state[2])
        temp_blue = list.copy(cube_state[1])

        cube_state[4][0] = temp_green[0]
        cube_state[4][1] = temp_green[1]
        cube_state[4][2] = temp_green[2]

        cube_state[1][0] = temp_red[0]
        cube_state[1][1] = temp_red[1]
        cube_state[1][2] = temp_red[2]

        cube_state[2][0] = temp_blue[0]
        cube_state[2][1] = temp_blue[1]
        cube_state[2][2] = temp_blue[2]

        cube_state[3][0] = temp_orange[0]
        cube_state[3][1] = temp_orange[1]
        cube_state[3][2] = temp_orange[2]

        f += 1
        
# Inverse Rotations. No return value. They modify the lists for each side

def rotate_fp(i):
    f = 0
    while f < i:
        temp_white = list.copy(cube_state[0])
        cube_state[0][0] = temp_white[2]
        cube_state[0][1] = temp_white[3]
        cube_state[0][2] = temp_white[4]
        cube_state[0][3] = temp_white[5]
        cube_state[0][4] = temp_white[6]
        cube_state[0][5] = temp_white[7]
        cube_state[0][6] = temp_white[0]
        cube_state[0][7] = temp_white[1]

        temp_blue = list.copy(cube_state[1])
        temp_orange = list.copy(cube_state[2])
        temp_green = list.copy(cube_state[3])
        temp_red = list.copy(cube_state[4])

        cube_state[1][4] = temp_red[4]
        cube_state[1][5] = temp_red[5]
        cube_state[1][6] = temp_red[6]

        cube_state[4][4] = temp_green[4]
        cube_state[4][5] = temp_green[5]
        cube_state[4][6] = temp_green[6]

        cube_state[3][4] = temp_orange[4]
        cube_state[3][5] = temp_orange[5]
        cube_state[3][6] = temp_orange[6]

        cube_state[2][4] = temp_blue[4]
        cube_state[2][5] = temp_blue[5]
        cube_state[2][6] = temp_blue[6]

        f += 1


def rotate_rp(i):
    f = 0
    while f < i:
        temp_red = list.copy(cube_state[4])
        cube_state[4][0] = temp_red[2]
        cube_state[4][1] = temp_red[3]
        cube_state[4][2] = temp_red[4]
        cube_state[4][3] = temp_red[5]
        cube_state[4][4] = temp_red[6]
        cube_state[4][5] = temp_red[7]
        cube_state[4][6] = temp_red[0]
        cube_state[4][7] = temp_red[1]

        temp_blue = list.copy(cube_state[1])
        temp_yellow = list.copy(cube_state[5])
        temp_green = list.copy(cube_state[3])
        temp_white = list.copy(cube_state[0])

        cube_state[1][2] = temp_yellow[2]
        cube_state[1][3] = temp_yellow[3]
        cube_state[1][4] = temp_yellow[4]

        cube_state[5][2] = temp_green[6]
        cube_state[5][3] = temp_green[7]
        cube_state[5][4] = temp_green[0]

        cube_state[3][6] = temp_white[2]
        cube_state[3][7] = temp_white[3]
        cube_state[3][0] = temp_white[4]

        cube_state[0][2] = temp_blue[2]
        cube_state[0][3] = temp_blue[3]
        cube_state[0][4] = temp_blue[4]

        f += 1


def rotate_lp(i):
    f = 0
    while f < i:
        temp_orange = list.copy(cube_state[2])
        cube_state[2][0] = temp_orange[2]
        cube_state[2][1] = temp_orange[3]
        cube_state[2][2] = temp_orange[4]
        cube_state[2][3] = temp_orange[5]
        cube_state[2][4] = temp_orange[6]
        cube_state[2][5] = temp_orange[7]
        cube_state[2][6] = temp_orange[0]
        cube_state[2][7] = temp_orange[1]

        temp_blue = list.copy(cube_state[1])
        temp_yellow = list.copy(cube_state[5])
        temp_green = list.copy(cube_state[3])
        temp_white = list.copy(cube_state[0])

        cube_state[0][0] = temp_green[4]
        cube_state[0][7] = temp_green[3]
        cube_state[0][6] = temp_green[2]

        cube_state[1][0] = temp_white[0]
        cube_state[1][7] = temp_white[7]
        cube_state[1][6] = temp_white[6]

        cube_state[5][0] = temp_blue[0]
        cube_state[5][7] = temp_blue[7]
        cube_state[5][6] = temp_blue[6]

        cube_state[3][4] = temp_yellow[0]
        cube_state[3][3] = temp_yellow[7]
        cube_state[3][2] = temp_yellow[6]

        f += 1


def rotate_up(i):
    f = 0
    while f < i:
        temp_blue = list.copy(cube_state[1])
        cube_state[1][0] = temp_blue[2]
        cube_state[1][1] = temp_blue[3]
        cube_state[1][2] = temp_blue[4]
        cube_state[1][3] = temp_blue[5]
        cube_state[1][4] = temp_blue[6]
        cube_state[1][5] = temp_blue[7]
        cube_state[1][6] = temp_blue[0]
        cube_state[1][7] = temp_blue[1]

        temp_red = list.copy(cube_state[4])
        temp_yellow = list.copy(cube_state[5])
        temp_orange = list.copy(cube_state[2])
        temp_white = list.copy(cube_state[0])

        cube_state[2][2] = temp_yellow[4]
        cube_state[2][3] = temp_yellow[5]
        cube_state[2][4] = temp_yellow[6]

        cube_state[5][4] = temp_red[6]
        cube_state[5][5] = temp_red[7]
        cube_state[5][6] = temp_red[0]

        cube_state[4][6] = temp_white[0]
        cube_state[4][7] = temp_white[1]
        cube_state[4][0] = temp_white[2]

        cube_state[0][0] = temp_orange[2]
        cube_state[0][1] = temp_orange[3]
        cube_state[0][2] = temp_orange[4]

        f += 1


def rotate_dp(i):
    f = 0
    while f < i:
        temp_green = list.copy(cube_state[3])
        cube_state[3][0] = temp_green[2]
        cube_state[3][1] = temp_green[3]
        cube_state[3][2] = temp_green[4]
        cube_state[3][3] = temp_green[5]
        cube_state[3][4] = temp_green[6]
        cube_state[3][5] = temp_green[7]
        cube_state[3][6] = temp_green[0]
        cube_state[3][7] = temp_green[1]

        temp_red = list.copy(cube_state[4])
        temp_yellow = list.copy(cube_state[5])
        temp_orange = list.copy(cube_state[2])
        temp_white = list.copy(cube_state[0])

        cube_state[4][2] = temp_yellow[0]
        cube_state[4][3] = temp_yellow[1]
        cube_state[4][4] = temp_yellow[2]

        cube_state[5][0] = temp_orange[6]
        cube_state[5][1] = temp_orange[7]
        cube_state[5][2] = temp_orange[0]

        cube_state[2][6] = temp_white[4]
        cube_state[2][7] = temp_white[5]
        cube_state[2][0] = temp_white[6]

        cube_state[0][4] = temp_red[2]
        cube_state[0][5] = temp_red[3]
        cube_state[0][6] = temp_red[4]

        f += 1


def rotate_bp(i):
    f = 0
    while f < i:
        temp_yellow = list.copy(cube_state[5])
        cube_state[5][0] = temp_yellow[2]
        cube_state[5][1] = temp_yellow[3]
        cube_state[5][2] = temp_yellow[4]
        cube_state[5][3] = temp_yellow[5]
        cube_state[5][4] = temp_yellow[6]
        cube_state[5][5] = temp_yellow[7]
        cube_state[5][6] = temp_yellow[0]
        cube_state[5][7] = temp_yellow[1]

        temp_red = list.copy(cube_state[4])
        temp_green = list.copy(cube_state[3])
        temp_orange = list.copy(cube_state[2])
        temp_blue = list.copy(cube_state[1])

        cube_state[4][0] = temp_blue[0]
        cube_state[4][1] = temp_blue[1]
        cube_state[4][2] = temp_blue[2]

        cube_state[1][0] = temp_orange[0]
        cube_state[1][1] = temp_orange[1]
        cube_state[1][2] = temp_orange[2]

        cube_state[2][0] = temp_green[0]
        cube_state[2][1] = temp_green[1]
        cube_state[2][2] = temp_green[2]

        cube_state[3][0] = temp_red[0]
        cube_state[3][1] = temp_red[1]
        cube_state[3][2] = temp_red[2]

        f += 1

# Scrambling method which returns a array of moves for scramble

def scramble_gen(i):
    # global moves
    f = 1
    scram = []
    while f <= i:
        loctest = True
        move = random.choice(moves)
        if (len(scram) > 0):
            locP = moves.index(scram[-1])
            loc = moves.index(move)
            if ((loc == 0 or loc == 1 or loc == 2) and (locP == 0 or locP == 1 or locP == 2) or
                    ((loc == 3 or loc == 4 or loc == 5) and (locP == 3 or locP == 4 or locP == 5)) or
                    ((loc == 6 or loc == 7 or loc == 8) and (locP == 6 or locP == 7 or locP == 8)) or
                    ((loc == 9 or loc == 10 or loc == 11) and (locP == 9 or locP == 10 or locP == 11)) or
                    ((loc == 12 or loc == 13 or loc == 14) and (locP == 12 or locP == 13 or locP == 14)) or
                    ((loc == 15 or loc == 16 or loc == 17) and (locP == 15 or locP == 16 or locP == 17))):
                f -= 1
                loctest = False
        if (loctest == True):
            scram.append(move)
        f += 1
    return scram

# Scramble the cube using standard and inverse rotations. No return value. Prints success if successful

def scramble_cube(scramble):
    global cube_solved
    for i in scramble:
        if (i == "r"):
            rotate_r(1)
            #print(cube_state)
        elif (i == "rp"):
            rotate_rp(1)
            #print(cube_state)
        elif (i == "r2"):
            rotate_r(2)
            #print(cube_state)
        elif (i == "l"):
            rotate_l(1)
            #print(cube_state)
        elif (i == "lp"):
            rotate_lp(1)
            #print(cube_state)
        elif (i == "l2"):
            rotate_l(2)
            #print(cube_state)
        elif (i == "u"):
            rotate_u(1)
            #print(cube_state)
        elif (i == "up"):
            rotate_up(1)
            #print(cube_state)
        elif (i == "u2"):
            rotate_u(2)
            #print(cube_state)
        elif (i == "d"):
            rotate_d(1)
            #print(cube_state)
        elif (i == "dp"):
            rotate_dp(1)
            #print(cube_state)
        elif (i == "d2"):
            rotate_d(2)
            #print(cube_state)
        elif (i == "f"):
            rotate_f(1)
            #print(cube_state)
        elif (i == "fp"):
            rotate_fp(1)
            #print(cube_state)
        elif (i == "f2"):
            rotate_f(2)
            #print(cube_state)
        elif (i == "b"):
            rotate_b(1)
            #print(cube_state)
        elif (i == "bp"):
            rotate_bp(1)
            #print(cube_state)
        elif (i == "b2"):
            rotate_b(2)
            #print(cube_state)
        else:
            print("error")
            return
    # print("Success")
    cube_solved = False

# Reset Cube to Solved state. locP refers location of previous move. loc refers to location of current move

def reset_cube():
    global white_side
    global blue_side
    global orange_side
    global green_side
    global red_side
    global yellow_side
    global cube_state
    white_side = ["white", "white", "white", "white", "white", "white", "white", "white", "white"]
    blue_side = ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"]
    orange_side = ["orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange"]
    green_side = ["green", "green", "green", "green", "green", "green", "green", "green", "green"]
    red_side = ["red", "red", "red", "red", "red", "red", "red", "red", "red"]
    yellow_side = ["yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow"]
    cube_state = [white_side, blue_side, orange_side, green_side, red_side, yellow_side]
    global cube_solved
    cube_solved = True

# Check is cube is solved. Returns true if it is solved. Returns false if cube is not solved

def check_solved():
    for i in cube_state[0]:
        if (i != "white"):
            return False
    for i in cube_state[1]:
        if (i != "blue"):
            return False
    for i in cube_state[2]:
        if (i != "orange"):
            return False
    for i in cube_state[3]:
        if (i != "green"):
            return False
    for i in cube_state[4]:
        if (i != "red"):
            return False
    for i in cube_state[5]:
        if (i != "yellow"):
            return False
    return True

# Function to constantly rotate the cube using different rotations until it reaches a solved state
# Returns true if cube is solved

def solve_cube():
    global cube_solved
    global move_counter
    global solution
    global moves
    global cube_state
    global scramble_state
    global temp
    if (cube_solved):
        print("Cube is solved")
        return True
    while (cube_solved != True):
        move = random.choice(moves)
        solution.append(move)
        if (move == "r"):
            # print("inside if statement")
            rotate_r(1)
        elif (move == "rp"):
            # print("inside if statement")
            rotate_rp(1)
        elif (move == "r2"):
            # print("inside if statement")
            rotate_r(2)
        elif (move == "l"):
            # print("inside if statement")
            rotate_l(1)
        elif (move == "lp"):
            # print("inside if statement")
            rotate_lp(1)
        elif (move == "l2"):
            # print("inside if statement")
            rotate_l(2)
        elif (move == "u"):
            # print("inside if statement")
            rotate_u(1)
        elif (move == "up"):
            # print("inside if statement")
            rotate_up(1)
        elif (move == "u2"):
            # print("inside if statement")
            rotate_u(2)
        elif (move == "d"):
            # print("inside if statement")
            rotate_d(1)
        elif (move == "dp"):
            # print("inside if statement")
            rotate_dp(1)
        elif (move == "d2"):
            # print("inside if statement")
            rotate_d(2)
        elif (move == "f"):
            # print("inside if statement")
            rotate_f(1)
        elif (move == "fp"):
            # print("inside if statement")
            rotate_fp(1)
        elif (move == "f2"):
            # print("inside if statement")
            rotate_f(2)
        elif (move == "b"):
            # print("inside if statement")
            rotate_b(1)
        elif (move == "bp"):
            # print("inside if statement")
            rotate_bp(1)
        elif (move == "b2"):
            # print("inside if statement")
            rotate_b(2)
        else:
            print("fail check")
        move_counter += 1
        # print(move)
        # # print(move_counter)
        # print(cube_state)
        # print(solution)
        cube_solved = check_solved()
        if(cube_solved):
            print("bool is true")

        if(check_solved()):
            print("method is true")
        if (move_counter > 30):
            # print(solution)
            solution = []
            move_counter = 0
            # cube_state = list.copy(scramble_state)
            reset_cube()
            scramble_cube(temp)
            # print(solution)
            # print(cube_state)
            # print(scramble_state)
    print("Cube solved")
    return True


reset_cube()
print(cube_state)

temp = scramble_gen(5)
print(["b", "b"])

scramble_cube(["b", "b"])
print(cube_state)
scramble_state = [list.copy(cube_state[0]), list.copy(cube_state[1]), list.copy(cube_state[2]), list.copy(cube_state[3]), list.copy(cube_state[4]), list.copy(cube_state[5])]
print(scramble_state)


if (solve_cube()):
    print(solution)