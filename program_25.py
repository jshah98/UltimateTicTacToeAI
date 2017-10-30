counter = 0
pred_count = 0
prev_gamestate = []
pred_moves = []
num = 0
    

def isBoardFull(squares):
        for i in range(9):
                if squares[i]==0:
                    return False
        return True
        
def isBoardWon (gamestate, boardNum):

    #Case1
    if gamestate [(boardNum * 9) + 2] == gamestate [(boardNum * 9) + 3] and gamestate [(boardNum * 9) + 2] != 0:
        if gamestate[(boardNum * 9) + 3] == gamestate[(boardNum * 9) + 5]:
            return gamestate [(boardNum * 9) + 2]
    elif gamestate [(boardNum * 9) + 2] == gamestate [(boardNum * 9) + 5] and gamestate [(boardNum * 9) + 2] != 0:
        if gamestate[(boardNum * 9) + 5] == gamestate[(boardNum * 9) + 8]:
            return gamestate [(boardNum * 9) + 2]
    elif gamestate [(boardNum * 9) + 2] == gamestate [(boardNum * 9) + 6] and [(boardNum * 9) + 2] != 0:
        if gamestate[(boardNum * 9) + 6] == gamestate[(boardNum * 9) + 10]:
            return gamestate [(boardNum * 9) + 2]
    elif gamestate [(boardNum * 9) + 4] == gamestate [(boardNum * 9) + 6] and [(boardNum * 9) + 4] != 0:
        if gamestate[(boardNum * 9) + 6] == gamestate[(boardNum * 9) + 8]:
            return gamestate [(boardNum * 9) + 2]

    #Case 2
    elif gamestate [(boardNum * 9) + 3] == gamestate [(boardNum * 9) + 6] and [(boardNum * 3) + 3] != 0:
        if gamestate[(boardNum * 9) + 6] == gamestate[(boardNum * 9) + 9]:
            return gamestate [(boardNum * 9) + 3]
    elif gamestate [(boardNum * 9) + 5] == gamestate [(boardNum * 9) + 6] and [(boardNum * 9) + 5] != 0:
        if gamestate[(boardNum * 9) + 6] == gamestate[(boardNum * 9) + 7]:
            return gamestate [(boardNum * 9) + 5]

    #Case 3
    elif gamestate[(boardNum * 9) + 8] == gamestate[(boardNum * 9) + 9] and [(boardNum * 9) + 8] != 0:
        if gamestate[(boardNum * 9) + 9] == gamestate[(boardNum * 9) + 10]:
            return gamestate[(boardNum * 9) + 8]
    else:
        return 0

def row_2 (gamestate, boardNum):
    count_3 = 0
    count_4 = 0

    for j in range (3):
        count_1 = 0
        count_2 = 0

        for i in range (3):
            if gamestate[2 + ((boardNum * 9)+ i + (3*j))] == 1:
                count_1 = count_1 + 1
            elif gamestate[2 + ((boardNum * 9)+ i + (3*j))] == 2:
                count_2 = count_2 + 1

            #Checks for row of 2
            if count_1 == 2 and count_2 == 0:
                count_3 = count_3 + 1
            elif count_2 == 2 and count_1 == 0:
                count_4 = count_4 + 1

    for j in range(3):
        count_1 = 0
        count_2 = 0

        for i in range(3):
            if gamestate[2 + ((boardNum * 9) + 3*i + j)] == 1:
                count_1 = count_1 + 1
            elif gamestate[2 + ((boardNum * 9) + 3*i + j)] == 2:
                count_2 = count_2 + 1

            if count_1 == 2 and count_2 == 0:
                count_3 = count_3 + 1
            elif count_2 == 2 and count_1 == 0:
                count_4 = count_4 + 1

    count_1 = 0
    count_2 = 0
    for i in range(3):
        if gamestate[2 + ((boardNum * 9) + 4*i)] == 1:
            count_1 = count_1 + 1
        elif gamestate[2 + ((boardNum * 9) + 4*i)] == 2:
            count_2 = count_2 + 1

        if count_1 == 2 and count_2 == 0:
            count_3 = count_3 + 1
        elif count_2 == 2 and count_1 == 0:
            count_4 = count_4 + 1

    count_1 = 0
    count_2 = 0
    for i in range(3):
        if gamestate[2 + (((boardNum * 9) + 2) + 2 * i)] == 1:
            count_1 = count_1 + 1
        elif gamestate[2 + (((boardNum * 9) + 2) + 2 * i)] == 2:
            count_2 = count_2 + 1

        if count_1 == 2 and count_2 == 0:
            count_3 = count_3 + 1
        elif count_2 == 2 and count_1 == 0:
            count_4 = count_4 + 1

    return count_3, count_4

def board_score (board_no, gamestate):
    score = 0
    multiplier = 0

    if isBoardFull (gamestate [(board_no*9+2):(board_no*9 + 11)]) == True:
        return 0
    winner = isBoardWon (gamestate, board_no)
    if winner != 0:
        if board_no == 4:
            return 300
        elif board_no == 0 or board_no == 2 or board_no == 6 or board_no == 8:
            return 200
        else:
            return 100
    a = row_2 (gamestate, board_no)
    if gamestate [0] == 1:
        score += a[0]
        score -= a[1]
    else:
        score += a[1]
        score -= a[0]
    
    for i in range (9):
        if gamestate [board_no*9 + i] == 0:
            continue
        if i == 4:
            if gamestate [board_no*9 + i] == gamestate [0]:
                score += 3
            else:
                score -= 3
        elif i == 0 or i == 2 or i == 6 or i == 8:
            if gamestate [board_no*9 + i] == gamestate [0]:
                score += 2
            else:
                score -= 2
        else:
            if gamestate [board_no*9 + i] == gamestate [0]:
                score += 1
            else:
                score -= 1
                
    return score   
    
def game_score (gamestate):
    sum = 0
    for i in range (9):
        sum += board_score (i, gamestate)
    return sum


def set_prev_gamestate (gamestate):
    global prev_gamestate
    prev_gamestate = gamestate

def get_valid_moves (gamestate):
    valid_moves = []
    if gamestate [1] == 9:
        for i in range (2, 83, 1):
            if gamestate [i] == 0:
                valid_moves.append (i-2)
        return valid_moves
    for i in range (9*gamestate [1]+2, 9*gamestate [1]+11, 1):
        if gamestate [i] == 0:
            valid_moves.append (i-2)
    return valid_moves

def get_board_no (sq_no, gamestate):
    if isBoardWon != 0 and isBoardFull (gamestate [int (sq_no/9)+2: int (sq_no/9)+11]) == False:
        return int (sq_no/9)   
    return 9
    
def average_opp_score (sq_no, temp_gamestate):
    global num
    temp_gamestate2 = temp_gamestate
    player = temp_gamestate [0]
    if temp_gamestate2 [0] == 1:
        opp = 2
    else:
        opp = 1
    temp_gamestate2 [1] = get_board_no (sq_no, temp_gamestate)
    sum = 0
    valid_moves2 = get_valid_moves (temp_gamestate)
    num -= len (valid_moves2)
    for i in range (len (valid_moves2)):
         temp_gamestate2 [valid_moves2[i] + 2] = opp
         sum += game_score (temp_gamestate2)         
         temp_gamestate2 [valid_moves2[i] + 2] = 0
    return sum/len (valid_moves2)

def get_changed_pos (gamestate):
    for i in range (len (gamestate)):
        if prev_gamestate [i] != gamestate [i]:
            return i
    return -1

def store_pred_moves (sq_no, temp_gamestate):
    global num, pred_moves
    temp_gamestate2 = temp_gamestate
    player = temp_gamestate [0]
    if temp_gamestate2 [0] == 1:
        opp = 2
    else:
        opp = 1
    temp_gamestate2 [1] = get_board_no (sq_no, temp_gamestate)
    valid_moves2 = get_valid_moves (temp_gamestate)
    num -= len (valid_moves2)
    for i in range (len (valid_moves2)):
        d = {}
        d[valid_moves2[i]] = pred_next_mov (temp_gamestate2)
        d ["gamestate"] = temp_gamestate2
        d["next_moves"] = []
        pred_moves.append (d)
        temp_gamestate2 [valid_moves2[i] + 2] = opp
        temp_gamestate2 [valid_moves2[i] + 2] = 0
    

def pred_next_mov (gamestate):
    global num
    temp_gamestate = gamestate
    max = -1000000000
    valid_moves = get_valid_moves (gamestate)
    num -= len (valid_moves)
    sq_no = valid_moves [0]
    for i in range (len (valid_moves)):
        temp_gamestate [valid_moves[i]+2] = gamestate [1]
        temp_score = game_score (temp_gamestate)
        temp_score += average_opp_score (valid_moves[i]+2, temp_gamestate)
        if temp_score > max:
            max = temp_score
            sq_no = valid_moves[i]
        temp_gamestate [valid_moves[i]+2] = 0
    return sq_no
    

# def think_ahead (max, n, next_moves):
#     global num, pred_moves, pred_count
#     if max != n:
#         for i in range (next_moves):
#             if len (next_moves[i] ["next_moves"]) == 0
#         think_ahead (max, n+1, 
    

def get_move (T, gamestate):
    gs_c = []
    for i in range (83):
        gs_c.append (int (gamestate[i]))
    global num, counter, pred_count, pred_moves
    num = T*20
    sq_no = get_valid_moves (gs_c) [0]
    if counter == 0: 
        sq_no = pred_next_mov (gs_c)
    
    store_pred_moves (sq_no, gs_c)
    set_prev_gamestate (gs_c)
    counter += 1
    changed_sq = get_changed_pos (gs_c)
    for i in range (len(pred_moves)):
        try:
            ans = pred_moves[i][changed_sq]
            pred_moves = pred_moves[i]["next_moves"]
            pred_count -= 1
            return ans
        except KeyError:
            pass
    sq_no = get_valid_moves (gs_c) [0]
    return sq_no
    
    