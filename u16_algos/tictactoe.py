## stores the data representation of the tictactoe board in a variable
def init_board():
    board=[] # this is the entire board

    for j in range(3):
        row=[] # define a new row
        for i in range(3): # do this for 3 times
            row.append(' ')#3empty spaces
            # init_board.append(row)# add this row to board
        board.append(row) # add this list of empty cells to the board
        print(row)
    return board
#this function prints out the board


def print_board(arg_board):
    count=1
    print("-"*13)
    for row in arg_board:
        for cell in row:
            if cell==" ":
                print(f"| {count} ", end = "")
            else:
                print(f"| {cell} ", end = "")
            #go to the next line
            if count %3 ==0:
                print("|")
                print("-"*13)
            count+=1
def get_player_move():
    while True:
        num_choice=input("Enter a number (1-9) :")
        if num_choice.isdigit():
            num_choice=int(num_choice)
            if num_choice >=1 and num_choice <=9:
                num_choice=num_choice-1
                row=num_choice//3
                col=num_choice%3
                board[row][col]='X'
                break
        else:
            print("you must enter a valid number")

# start of main code

board = init_board()
print_board(board)
while True:
    get_player_move()
    print_board(board)