import random
import os

#Debug Vars
debug = False

#Game Vars
game = 1
turn = 1
player_wins = 0
enemy_wins = 0
game_over = False
player_ships_alive = 5
enemy_ships_alive = 5
difficulty = [["easy"], ["easy", 10], ["medium", 15], ["hard", 20]] #Current setting, easy vars, medium vars, hard vars
grid_size = difficulty[1][1] #Between 10 and 20 for screen size (max 20)

#Board
blank = "[ ]"
hit = "[X]"
sunk = "[X]"
miss = "[O]"
hidden = "[*]"
nums = ["   "]
A=["A "]
B=["B "]
C=["C "]
D=["D "]
E=["E "]
F=["F "]
G=["G "]
H=["H "]
I=["I "]
J=["J "]
K=["K "]
L=["L "]
M=["M "]
N=["N "]
O=["O "]
P=["P "]
Q=["Q "]
R=["R "]
S=["S "]
T=["T "]
U=["U "]
V=["V "]
W=["W "]
X=["X "]
Y=["Y "]
Z=["Z "]
num_rows = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
player_board =[]
enemy_board = []
player_guesses = []
enemy_guesses = []

#Ships
patrol_boat = [2]
destroyer = [3]
submarine = [3]
battleship = [4]
aircraft_carrier = [5]
ships = [patrol_boat, destroyer, submarine, battleship, aircraft_carrier]
ship_names = ["Patrol Boat", "Destroyer", "Submarine", "Battleship", "Aircraft Carrier"]
player_ships = ["player"]
enemy_ships = ["enemy"]

def set_difficulty():
    global grid_size
    loop = True
    while loop == True:
        response = input("Choose difficult: (Easy, Medium, Hard) " )
        response.lower()
        if response == "easy":
            difficulty[0][0] = difficulty[1][0]
            grid_size = difficulty[1][1]
            loop = False
        elif response == "medium":
            difficulty[0][0] = difficulty[2][0]
            grid_size = difficulty[2][1]
            loop = False
        elif response == "hard":
            difficulty[0][0] = difficulty[3][0]
            grid_size = difficulty[3][1]
            loop = False
        else:
            print("Invalid response")

def set_up():
    global num_rows
    global grid_size
    global player_board
    global enemy_board
    global ships
    global player_ships
    global enemy_ships
    #Set up number of columns
    for i in range(0, grid_size):
        space = "  "
        if i >= 9:
            space = " "
        nums.append(str(i + 1) + space)
    player_board.append(nums)
    enemy_board.append(nums)
    #Set up number of rows
    for j in range(0, grid_size):
        player_board.append(num_rows[j])
        enemy_board.append(num_rows[j])
    player_board.append("Player's Board")
    enemy_board.append("Enemy's Board ")
    #Randomly place ships
    for i in range(0, len(ships)):
        deploy_ship(ships[i], player_ships)
        deploy_ship(ships[i], enemy_ships)
    set_point_status(player_ships)
    set_point_status(enemy_ships)

#ships = [patrol_boat, destroyer, submarine, battleship, aircraft_carrier]
def deploy_ship(ship, current_player):
    global grid_size
    ymax = 0
    xmax = 0
    orientation = random.randint(1, 2) #Horizontal, Vertical
    ship_range = ship[0] - 1
    if orientation == 1: #Horizontal
        xmax = grid_size - ship_range
        ymax = grid_size
    else: #Vertical
        xmax = grid_size
        ymax = grid_size - ship_range
    loop = True
    while loop == True:
        potential_placement = []
        X = random.randint(1,xmax)
        Y = random.randint(1,ymax)
        anchor = [Y, X]
        potential_placement.append(anchor) #first point of placement
        for points in range(1, ship[0]):
            next_point = []
            if orientation == 1: #Horizontal
                X += 1
                next_point = [Y, X]
            else: #Vertical
                Y += 1
                next_point = [Y, X]
            potential_placement.append(next_point)
        occupied = False
        for a in range(1, len(current_player)): #For each Ship
            for b in range(1, len(current_player[a])): #For each ship's point
                for c in range(0, len(potential_placement)): #For each potential placement point
                    if current_player[a][b] == potential_placement[c]:
                        occupied = True
        if occupied != True:
            loop = False
    counter = 0
    placement = [ship[0]]
    for point in range(0, ship[0]):
        placement.append(potential_placement[counter])
        counter += 1
    current_player.append(placement)

def set_point_status(current_player): #Current player's ships list
    for i in range(1, len(current_player)): #For each ship 
        for j in range(1, len(current_player[i])): #For each ship's point
            if current_player[0] == "player" or debug == True:
                current_player[i][j].append("hidden")
            else:
                current_player[i][j].append("blank")

def convert_y_axis(letter):
    if letter == "A":
        return 1
    elif letter == "B":
        return 2
    elif letter == "C":
        return 3
    elif letter == "D":
        return 4
    elif letter == "E":
        return 5
    elif letter == "F":
        return 6
    elif letter == "G":
        return 7
    elif letter == "H":
        return 8
    elif letter == "I":
        return 9
    elif letter == "J":
        return 10
    elif letter == "K":
        return 11
    elif letter == "L":
        return 12
    elif letter == "M":
        return 13
    elif letter == "N":
        return 14
    elif letter == "O":
        return 15
    elif letter == "P":
        return 16
    elif letter == "Q":
        return 17
    elif letter == "R":
        return 18
    elif letter == "S":
        return 19
    elif letter == "T":
        return 20
    elif letter == "U":
        return 21
    elif letter == "V":
        return 22
    elif letter == "W":
        return 23
    elif letter == "X":
        return 24
    elif letter == "Y":
        return 25
    elif letter == "Z":
        return 26
    elif letter == 1:
        return "A"
    elif letter == 2:
        return "B"
    elif letter == 3:
        return "C"
    elif letter == 4:
        return "D"
    elif letter == 5:
        return "E"
    elif letter == 6:
        return "F"
    elif letter == 7:
        return "G"
    elif letter == 8:
        return "H"
    elif letter == 9:
        return "I"
    elif letter == 10:
        return "J"
    elif letter == 11:
        return "K"
    elif letter == 12:
        return "L"
    elif letter == 13:
        return "M"
    elif letter == 14:
        return "N"
    elif letter == 15:
        return "O"
    elif letter == 16:
        return "P"
    elif letter == 17:
        return "Q"
    elif letter == 18:
        return "R"
    elif letter == 19:
        return "S"
    elif letter == 20:
        return "T"
    elif letter == 21:
        return "U"
    elif letter == 22:
        return "V"
    elif letter == 23:
        return "W"
    elif letter == 24:
        return "X"
    elif letter == 25:
        return "Y"
    elif letter == 26:
        return "Z"
    else:
        return "Invalid input"

def print_grid(players_board, players_ships):
    global grid_size
    global blank
    global hit
    global miss
    global sunk
    global hidden
    global nums
    #Draw Board Header
    player = players_board[-1]
    print("----------------------")
    print(" " + player + "     /")
    print("--------------------")
    #Check Ships
    hits = []
    misses = []
    hide = []
    sunken = []
    #Check Ships
    for ship in range(1, len(players_ships)): #For each ship
        for point in range(1, len(players_ships[ship])): #For each ship's point
            if players_ships[ship][point][-1] != "blank":
                location = []
                if players_ships[ship][point][-1] == "hit":
                    location.append(players_ships[ship][point][0])
                    location.append(players_ships[ship][point][1])
                    hits.append(location)
                elif players_ships[ship][point][-1] == "sunk":
                    location.append(players_ships[ship][point][0])
                    location.append(players_ships[ship][point][1])
                    sunken.append(location)
                else: #hidden
                    location.append(players_ships[ship][point][0])
                    location.append(players_ships[ship][point][1])
                    hide.append(location)
    #Check Misses
    guesses = []
    if players_ships[0] == "player":
        guesses = enemy_guesses
    else:
        guesses = player_guesses
    for guess in range(0, len(guesses)):
        if guesses[guess][-1] == "miss":
            location = [guesses[guess][0], guesses[guess][1]]
            misses.append(location)
    #Draw Grid
    header = ""
    for num in range(0, grid_size +1):
        row = nums[num]
        header = header + row
    Asquares = ""
    Bsquares = ""
    Csquares = ""
    Dsquares = ""
    Esquares = ""
    Fsquares = ""
    Gsquares = ""
    Hsquares = ""
    Isquares = ""
    Jsquares = ""
    Ksquares = ""
    Lsquares = ""
    Msquares = ""
    Nsquares = ""
    Osquares = ""
    Psquares = ""
    Qsquares = ""
    Rsquares = ""
    Ssquares = ""
    Tsquares = ""
    Usquares = ""
    Vsquares = ""
    Wsquares = ""
    Xsquares = ""
    Ysquares = ""
    Zsquares = ""
    gridrows =[header, Asquares, Bsquares, Csquares, Dsquares, Esquares, Fsquares, Gsquares, Hsquares, Isquares, Jsquares, Ksquares, Lsquares,
               Msquares, Nsquares, Osquares, Psquares, Qsquares, Rsquares, Ssquares, Tsquares, Usquares, Vsquares, Wsquares, Xsquares, Ysquares,
               Zsquares]
    hits.append("hit")
    misses.append("miss")
    hide.append("hidden")
    sunken.append("sunk")
    not_blanks = [hits, misses, hide, sunken]
    counter = 0
    for a in range (1, grid_size +1): #Rows previously 11
        row = str(players_board[a][0])
        for b in range(1, grid_size +1): #Columns previously 11
            not_blank_detected = False
        #Check non-blanks
            for c in range(0, len(not_blanks)): #For each not blank
                for d in range(0, len(not_blanks[c])): #For each point in each set of not-blanks
                    point_check = [a, b]
                    if point_check == not_blanks[c][d]: #If not-blank detected
                        not_blank_detected = True
                        if not_blanks[c][-1] == "hit":
                            row = row + hit
                        elif not_blanks[c][-1] == "miss":
                            row = row + miss
                        elif not_blanks[c][-1] == "sunk":
                            row = row + sunk
                        else:
                            row = row + hidden
            if not_blank_detected == False:
                row = row + blank
        gridrows[a] = gridrows[a] + row
    for rows in range(0, grid_size +1):
        print(gridrows[rows])

def player_guess():
    loop = True
    while loop == True:
        response = input("Where will you fire missiles? " )
        if len(response) > 3:
            print("Invalid response")
        else:
            check_row = response[0].upper()
            check_column = ""
            for i in range(1, len(response)):
                check_column += response[i]
            guess = []
            if check_row.isalpha() and int(convert_y_axis(check_row)) <= grid_size and check_column.isdigit() and (int(check_column) <= grid_size):
                guess.append(convert_y_axis(check_row))
                guess.append(int(check_column))
                check_prev_guess = False
                for a in range(0, len(player_guesses)):
                    prev_guess = [player_guesses[a][0], player_guesses[a][1]]
                    if prev_guess == guess:
                        print("Location already guessed")
                        check_prev_guess = True
                if check_prev_guess == False:
                    loop = False
            else:
                print("Invalid response")
    check_guess(guess, enemy_ships)

def check_guess(guess, enemy): #point guessed [Y, X], enemy's ships list
    successful_attack = False
    ship_num = 0
    for a in range(1, len(enemy)): #for each ship in the other player's board
        for b in range(1, len(enemy[a])): #for each point the ship has
            ship_point = [enemy[a][b][0], enemy[a][b][1]]
            if guess == ship_point:
                enemy[a][b][2] = "hit"
                successful_attack = True
                ship_num = a
                print("Target hit!")
    if successful_attack == False:
        guess.append("miss")
        print("Target missed!")
    else:
        guess.append("hit")
    if enemy[0] == "player":
        enemy_guesses.append(guess)
    else:
        player_guesses.append(guess)
    if enemy[0] == "player": #enemy is guessing
        check_ship_status(enemy_ships, enemy[ship_num], ship_num, enemy_guesses)
    else:
        check_ship_status(player_ships, enemy[ship_num], ship_num, player_guesses)

def check_ship_status(player, ship, ship_num, guesses): #Player or enemy ships, individual ship list, the ship in order of ships list, player or enemy guesses
    global game_over
    global player_wins
    global enemy_wins
    global player_ships_alive
    global enemy_ships_alive
    current_player = ""
    enemy = ""
    hits = 0
    for point in range(1, len(ship)):
        if ship[point][-1] == "hit":
            hits +=1
    if hits == ship[0]:
        for a in range(1, len(ship)):
            ship[a][-1] = "sunk"
        #Convert AI guesses for ship to sunk
        for b in range(0, len(guesses)):
            for c in range(1, len(ship)):
                ship_point = [ship[c][0], ship[c][1]]
                guessed_point = [guesses[b][0], guesses[b][1]]
                if guessed_point == ship_point:
                    guesses[b][-1] = "sunk"
        if player[0] == "player":
            current_player = "Player"
            enemy = "Enemy"
            enemy_ships_alive -= 1
            if enemy_ships_alive == 0:
                game_over = True
        else:
            current_player = "Enemy"
            enemy = "Player"
            player_ships_alive -=1
            if player_ships_alive == 0:
                game_over = True
        print(current_player + " sunk " + enemy + "'s " + ship_names[ship_num -1] + "!")
        if game_over == True:
            print("Game Over! " + current_player + " wins!")
            if current_player == "player":
                player_wins += 1
            else:
                enemy_wins += 1

def set_window_size():
    os.system('mode con: cols=120 lines=45')

def enemy_guess():
    global enemy_guesses
    global player_ships
    unsunken_ship = False
    known_hits = []
    fire_at = []
    for a in range(0, len(enemy_guesses)):
        if enemy_guesses[a][-1] == "hit":
            unsunken_ship = True
            known_hit = [enemy_guesses[a][0], enemy_guesses[a][1]]
            known_hits.append(known_hit)
    if unsunken_ship == True:
        #Knows there is an unsunken ship and will aim for points around those hits
        loop1 = True
        while loop1 == True:
            randomizer = random.randint(0, len(known_hits)-1)
            aim_at = [known_hits[randomizer][0], known_hits[randomizer][1]]
            previously_guessed = False
            compass = random.randint(0, 4)
            next_guess = []
            if compass == 0 and aim_at[0] +1 <= grid_size: #North Y+1
                next_guess = [aim_at[0] +1, aim_at[1]]
            elif compass == 1 and aim_at[0] -1 >= 1: #South
                next_guess = [aim_at[0] -1, aim_at[1]]
            elif compass == 2 and aim_at[1] -1 >= 1: #West
                next_guess = [aim_at[0], aim_at[1] -1]
            elif compass == 3 and aim_at[1] +1 <= grid_size: #east
                next_guess = [aim_at[0], aim_at[1] +1]
            else:
                next_guess = known_hits[0]
            for b in range(0, len(enemy_guesses)):
                guessed_point = [enemy_guesses[b][0], enemy_guesses[b][1]]
                if guessed_point == next_guess:
                    previously_guessed = True
            if previously_guessed == False: #Should only occur after all points are checked
                fire_at = next_guess
                loop1 = False
    else:
        #pick a random point
        loop = True
        while loop == True:
            previously_guessed = False
            next_guess = []
            X = random.randint(1,grid_size)
            Y = random.randint(1,grid_size)
            next_guess = [Y, X]
            if len(enemy_guesses) > 0:
                for b in range(0, len(enemy_guesses)):
                    guessed_point = [enemy_guesses[b][0], enemy_guesses[b][1]]
                    if guessed_point == next_guess:
                        previously_guessed = True
                if previously_guessed == False:
                    fire_at = next_guess
                    loop = False
            else:
                fire_at = next_guess
                loop = False
    print("The Enemy fires missiles at " + convert_y_axis(fire_at[0]) + str(fire_at[1]) + "!")
    check_guess(fire_at, player_ships)

def version():
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                        Battleship - Code by Daniel Navarro                                   ver: 1.00")
    print("-----------------------------------------------------------------------------------------------------------------------")
        
def take_turn():
    global turn
    global game_over
    while game_over == False:
        print("----------------------------------------------------")
        print(" Turn: " + str(turn) + "      Ships Remaining: P:" + str(player_ships_alive) + "  E:" + str(enemy_ships_alive) + "           /")
        print("--------------------------------------------------")
        print_grid(enemy_board, enemy_ships)
        print_grid(player_board, player_ships)
        player_guess()
        if game_over == False:
            enemy_guess()
        turn += 1

set_window_size()
version()
set_difficulty()
set_up()
take_turn()


