import random                                           #Importing random module 

import time                                              #Importing time module


def create_grid(size):
    
    symbols = [chr(65 + i) for i in range((size * size)//2)] 
    
    pairs = symbols * 2
    
    random.shuffle(pairs)                                        #Using shuffle method from random module
    
    grid = [pairs[i : i+size] for i in range(0, len(pairs), size)]

    return grid


def display_grid(visible_grid):
    
    for row in visible_grid:

        print(' '.join(row))

    print()

def is_game_complete(visible_grid):
    
    return all(cell != "-" for row in visible_grid for cell in row)        


def main_game(size, time_limit):

    grid = create_grid(size)                                                   #Initializing the grid

    visible_grid = [["_"] * size for _ in range(size)]                         #Hidden grid for the player 
    
    print("\n === Welcome to Memory Puzzle game! ===")

    print("f Match all pairs in {time_limit} seconds.\n")

    
    start_time = time.time()                                                    #Start the timer

    end_time = start_time + time_limit                                        # calculate when the time limit will be reached 

    moves = 0 

    while time.time() < end_time:
        
        display_grid(visible_grid)

        if is_game_complete(visible_grid):
            print("f Congratulations! you completed the game in {moves} moves!")
            return 
        
        try:

            print("Enter coordinates of two cards to flip (row an dcolumn, space separated):")
            r1, c1 = map(int, input("Card1 (row col): ").split())
            r2, c2 = map(int, input("Card2 (row, col): ").split())

            if (r1 == r2 and c1 == c2) or not (0 <= r1 < size and 0 <= c1 <size and 0 <= r2 < size and 0 <= c2 < size ):

                print("invalid input! Coordinates must be distinct anad within the grid.\n")

                continue 

            if visible_grid[r1][c1] != "_" or visible_grid[r2][c2] != "_":

                print("One or both cards are already flipped! Try again.\n")

                continue 

            visible_grid[r1][c1] = grid[r1][c1]
            visible_grid[r2][c2] = grid[r2][c2]
            display_grid(visible_grid)

            if grid[r1][c1] != grid[r2][c2]:
                print("No match ! cards will be flipped back,\n")
                time.sleep(1)
                visible_grid[r1][c1] = "_"
                visible_grid[r2][c2] = "_"

            else:
                print("Match Found!\n")

            moves += 1    
        
        except Exception as e:
            print("f Invalid input! please enter valid coordinates. ({e})\n")


    print("\n time is up! Game over.")
    print("Here was the full grid:")

    for row in grid:
        print(" ".join(row))
    print("Better luck next time!")

if __name__ == "__ main__":
    grid_size = 4 
    time_limit = 60
    main_game(grid_size, time_limit)                 