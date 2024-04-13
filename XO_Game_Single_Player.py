import random

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
        
def enter_move(player):
        count, bot_move = 1,5 #bot's initial move always 5
        victory=False
        #Set the options available for the bot's move selection
        #Note:"5" is excluded because the bot consistently takes the first turn, marking it with "X" as its initial move.
        bot_options=[1,2,3,4,6,7,8,9]
        display_board()

        #Loop iterates 4 times, with player and bot updating the board each time, ensuring all values are filled
        #Ensuring a total of 4 moves
        while count<=4:

            print("Bot(X) Choose "+str(bot_move))    
            player_move = input("\n"+player+"(O) Enter your move (enter number 1 to 9): ")

            #If the input is not a digit or is not within the range 1 to 9, prompt the user again for a valid move
            while not(player_move.isdigit() and 1 <= int(player_move) <= 9): 
                player_move = input("\n"+player+"(O) Invalid input! Enter your move (enter number 1 to 9): ")

            player_move = int(player_move)

            #Check if the position on the board is not already occupied by "X" or "O"
            if board[player_move] !="X" and board[player_move]!="O":

                #If the position is not occupied by "X" or "O", update the board with the player's character (O)
                board[player_move] = 'O'
                count+=1 #Increment the move count

                #Check if the player has won after the player's move
                if find_winner('O'): 
                    victory=True;
                    display_board()
                    print(player+" WON")
                    break

                bot_options.remove(player_move) #Remove the player's move from the available options
                bot_move=random.choice(bot_options) #Randomly select a move from the remaining options
                board[bot_move] = 'X' #Place 'X' for the bot's selected move on the board
                bot_options.remove(bot_move) #Remove the bot's move from the available options

                #Check if the bot has won after the bot's move
                if find_winner('X'):
                    victory=True;
                    display_board()
                    print("Bot(X) Choose "+str(bot_move))   
                    print("Bot WON")
                    break
            else:
                print("That place is already filled\n")
            
            display_board()
            
        #If the count exceeds 4 (indicating all moves are exhausted) and there is no victory, print "MATCH DRAW"
        if count>4 and (not victory): 
            print("MATCH DRAW")    
                  
def main():
    global board
    #Define the initial board state with "5" as the bot's first move
    board={ 1:"1",2:"2",3:"3",4:"4",5:"X",6:"6",7:"7",8:"8",9:"9" }
    player = input("Enter your name: ")
    enter_move(player)  

if __name__ == "__main__":
    main()
