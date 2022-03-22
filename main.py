board = ["-", "-", "-", "-",
         "-", "-", "-", "-",
         "-", "-", "-", "-",
         "-", "-", "-", "-"]
gamerunning = True
player1 = 0
player2 = 0
currentplayer = "player1"
a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
j = 1
k = 1
l = 1
m = 1
n = 1
s = 1
t = 1
q = 1
w = 1
r = 1
z = 1
y = 1
v = 1
x = 1
p = 1
i = 1
u = 1
o = 1

# printing the game board


def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2]+" | "+board[3])
    print("---------------")
    print(board[4]+" | "+board[5]+" | "+board[6]+" | "+board[7])
    print("---------------")
    print(board[8]+" | "+board[9]+" | "+board[10]+" | "+board[11])
    print("---------------")
    print(board[12]+" | "+board[13]+" | "+board[14]+" | "+board[15])

# take player input


def playerinput(board):
    global currentplayer
    inp = int(input(str(currentplayer)+" ,enter a number 1:16 "))
    so = input(str(currentplayer)+" ,enter S or O: ")
    if inp >= 1 and inp <= 16 and board[inp-1] == "-" and (so == "S" or so == "O"):
        board[inp-1] = so
    else:
        print("player is already in the spot!")
        switch()
# check
# horizontally


def checkh(board):
    global a, b, c, d, e, f, j, k
    if board[0] == board[2] == "S" != board[1] and board[1] != "-" and a == 1:
        a = 0
        return True
    elif board[4] == board[6] == "S" != board[5] and board[5] != "-" and b == 1:
        b = 0
        return True
    elif board[8] == board[10] == "S" != board[9] and board[9] != "-" and c == 1:
        c = 0
        return True
    elif board[12] == board[14] == "S" != board[13] and board[13] != "-" and d == 1:
        d = 0
        return True
    elif board[1] == board[3] == "S" != board[2] and board[2] != "-" and e == 1:
        e = 0
        return True
    elif board[5] == board[7] == "S" != board[6] and board[6] != "-" and f == 1:
        f = 0
        return True
    elif board[9] == board[11] == "S" != board[10] and board[10] != "-" and j == 1:
        j = 0
        return True
    elif board[13] == board[15] == "S" != board[14] and board[14] != "-" and k == 1:
        k = 0
        return True

# vertically


def checkr(board):
    global l, m, n, s, t, q, w, r
    if board[0] == board[8] == "S" != board[4] and board[4] != "-" and l == 1:
        l = 0
        return True
    elif board[1] == board[9] == "S" != board[5] and board[5] != "-" and m == 1:
        m = 0
        return True
    elif board[2] == board[10] == "S" != board[6] and board[6] != "-" and n == 1:
        n = 0
        return True
    elif board[3] == board[11] == "S" != board[7] and board[7] != "-" and s == 1:
        s = 0
        return True
    elif board[4] == board[12] == "S" != board[8] and board[8] != "-" and t == 1:
        t = 0
        return True
    elif board[5] == board[13] == "S" != board[9] and board[9] != "-" and q == 1:
        q = 0
        return True
    elif board[6] == board[14] == "S" != board[10] and board[10] != "-" and w == 1:
        w = 0
        return True
    elif board[7] == board[15] == "S" != board[11] and board[11] != "-" and r == 1:
        r = 0
        return True

# diagonally


def checkd(board):
    global z, y, v, x, p, i, u, o
    if board[2] == board[8] == "S" != board[5] and board[5] != "-" and z == 1:
        z = 0
        return True
    elif board[1] == board[11] == "S" != board[6] and board[6] != "-" and y == 1:
        y = 0
        return True
    elif board[4] == board[14] == "S" != board[9] and board[9] != "-" and p == 1:
        p = 0
        return True
    elif board[6] == board[12] == "S" != board[9] and board[9] != "-" and i == 1:
        i = 0
        return True
    elif board[0] == board[10] == "S" != board[5] and board[5] != "-" and u == 1:
        u = 0
        return True
    elif board[5] == board[15] == "S" != board[10] and board[10] != "-" and o == 1:
        o = 0
        return True
    elif board[3] == board[9] == "S" != board[6] and board[6] != "-" and v == 1:
        v = 0
        return True
    elif board[7] == board[13] == "S" != board[10] and board[10] != "-" and x == 1:
        x = 0
        return True

# stop game


def stop(board):
    global gamerunning
    if"-"not in board:
        gamerunning = False

# check win


def win():
    global player1
    global player2
    global currentplayer
    if checkd(board) or checkh(board) or checkr(board):
        if currentplayer == "player1":
            player1 += 1
            if checkd(board) or checkh(board) or checkr(board):
                player1 += 1
        elif currentplayer == "player2":
            player2 += 1
            if checkd(board) or checkh(board) or checkr(board):
                player2 += 1
        switch()


# switch player

def switch():
    global currentplayer
    if currentplayer == "player1":
        currentplayer = "player2"
    else:
        currentplayer = "player1"


while gamerunning:
    printBoard(board)
    playerinput(board)
    win()
    stop(board)
    switch()
    print("player 1 ", player1)
    print("player 2 ", player2)

if player1 > player2:
    print("player 1 is winner ")
elif player2 > player1:
    print("player 2 is winner ")
else:
    print("It is a tie! ")
