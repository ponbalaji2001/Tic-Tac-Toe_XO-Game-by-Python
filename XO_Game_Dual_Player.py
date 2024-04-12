def display_board():
    num=1
    for i in range(3):
        print("+","+","+","+",sep="-------")
        print("|","|","|","|",sep="       ")
        print("|",board[num],"|",board[num+1],"|",board[num+2],"|",sep="   ")
        print("|","|","|","|",sep="       ")
        num+=3
    
    print("+","+","+","+",sep="-------")


def find_winner(char):

    if board[1] == board[2] == board[3] == char or board[4] == board[5] == board[6] == char or \
       board[7] == board[8] == board[9] == char or board[1] == board[4] == board[7] == char or \
       board[2] == board[5] == board[8] == char or board[3] == board[6] == board[9] == char or \
       board[1] == board[5] == board[9] == char or board[3] == board[5] == board[7] == char :
            return True
        

def enter_move(player1, player2):
        count = 1
        victory=False
        display_board()

        #Loop iterates 9 times to update the board with 'X' and 'O' values, ensuring only 9 moves are made
        while count<=9:

            #Determine the player's name and their respective value (char: 'X' or 'O') based on the count
            #If count is even, it's player 2's turn (char: 'O'), otherwise it's player 1's turn (char: 'X')
            char = "O" if count%2==0 else "X"
            name = player2 if count%2==0 else player1
               
            move = input("\n"+name+"("+char+") Enter your move (enter number 1 to 9): ")

            #If the input is not a digit or is not within the range 1 to 9, prompt the user again for a valid move
            while not(move.isdigit() and 1 <= int(move) <= 9): 
                move = input("\n"+name+"("+char+") Invalid input! Enter your move (enter number 1 to 9): ")

            move = int(move)

            #Check if the position on the board is not already occupied by "X" or "O"
            if board[move] !="X" and board[move]!="O":

                #If the position is not occupied by "X" or "O", update the board with the current player's character
                board[move] = char
                count+=1 #Increment the move count

                #Check if the current player has won
                if find_winner(char): 
                    victory=True;
                    display_board()
                    print(name+" WON")
                    break

            else:
                print("That place is already filled\n")
       
            display_board()
            
        #If the count exceeds 9 (indicating all moves are exhausted) and there is no victory, print "MATCH DRAW"
        if count>9 and (not victory): 
            print("MATCH DRAW")
          
                  
def main():
    global board
    board={ 1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9" }
    player1 = input("Player 1 Enter the name: ")
    player2 = input("Player 2 Enter the name: ")
    enter_move(player1, player2)  

if __name__ == "__main__":
    main()
