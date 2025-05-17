# Import random module for computer's random moves
import random

# Function to display the game board
def show_grid(grid_data):
    """Displays the current game grid"""
    # Loop through each row (3 rows total)
    for row in range(3):
        # Print each cell in the row with borders
        print(f" {grid_data[row*3]} | {grid_data[row*3+1]} | {grid_data[row*3+2]} ")
        # Print horizontal line between rows (but not after last row)
        if row < 2:
            print("-----------")

# Function to check game status (win/draw/continue)
def find_winner(grid_data):
    """Checks if the game has been won or tied"""
    
    # Check horizontal wins (rows)
    for r in range(0, 9, 3):  # Start at 0, 3, 6
        if grid_data[r] == grid_data[r+1] == grid_data[r+2] != " ":
            return grid_data[r]  # Return the winning symbol (X or O)
    
    # Check vertical wins (columns)
    for c in range(3):  # Columns 0, 1, 2
        if grid_data[c] == grid_data[c+3] == grid_data[c+6] != " ":
            return grid_data[c]
    
    # Check diagonal wins
    # Top-left to bottom-right
    if grid_data[0] == grid_data[4] == grid_data[8] != " ":
        return grid_data[0]
    # Top-right to bottom-left
    if grid_data[2] == grid_data[4] == grid_data[6] != " ":
        return grid_data[2]
    
    # Check for draw (no empty spaces left)
    if " " not in grid_data:
        return "Draw"
    
    # No winner yet
    return None

# Function to get and validate human player's move
def get_human_choice(grid_data):
    """Gets and validates human player's move"""
    while True:
        try:
            # Get input (1-9) and convert to 0-based index
            choice = int(input("Select position (1-9): ")) - 1
            # Check if move is valid (within range and empty space)
            if 0 <= choice <= 8 and grid_data[choice] == " ":
                return choice
            print("Invalid selection. Try again.")
        except ValueError:  # Handle non-number input
            print("Please input a number from 1 to 9.")

# Function to determine computer's move
def make_computer_play(grid_data):
    """Determines computer's move strategy"""
    
    # First check if computer can win immediately
    for pos in range(9):
        if grid_data[pos] == " ":
            grid_data[pos] = "O"  # Try move
            if find_winner(grid_data) == "O":
                grid_data[pos] = " "  # Undo test move
                return pos  # Return winning move
            grid_data[pos] = " "  # Undo test move
    
    # Then check if human is about to win (block them)
    for pos in range(9):
        if grid_data[pos] == " ":
            grid_data[pos] = "X"  # Test human move
            if find_winner(grid_data) == "X":
                grid_data[pos] = " "  # Undo test move
                return pos  # Return blocking move
            grid_data[pos] = " "  # Undo test move
    
    # Prefer center position if available
    if grid_data[4] == " ":
        return 4
    
    # Choose random corner if available
    corner_positions = [0, 2, 6, 8]
    random.shuffle(corner_positions)  # Randomize corner selection
    for corner in corner_positions:
        if grid_data[corner] == " ":
            return corner
    
    # If all else fails, choose any open spot
    open_spots = []
    for pos in range(9):
        if grid_data[pos] == " ":
            open_spots.append(pos)
    return random.choice(open_spots)

# Main game function
def run_game():
    """Main game controller"""
    # Initialize empty board (list with 9 spaces)
    grid_data = [" "] * 9
    # Human plays first (X), computer is O
    current_turn = "X"  
    
    # Game introduction and instructions
    print("Tic Tac Toe Game!")
    print("Positions are numbered 1-9 left to right, top to bottom")
    show_grid([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Show position reference
    print("\nGame starts now!\n")
    
    # Main game loop
    while True:
        show_grid(grid_data)  # Display current board
        
        # Human player's turn
        if current_turn == "X":
            position = get_human_choice(grid_data)
            grid_data[position] = "X"
        # Computer's turn
        else:
            print("\nComputer is thinking...")
            position = make_computer_play(grid_data)
            grid_data[position] = "O"
            print(f"Computer picked position {position + 1}")
        
        # Check game status after each move
        game_result = find_winner(grid_data)
        if game_result:
            show_grid(grid_data)  # Show final board
            if game_result == "Draw":
                print("\nGame ended in a draw!")
            else:
                print(f"\n{'You' if game_result == 'X' else 'Computer'} won!")
            break  # Exit game loop
        
        # Switch turns
        current_turn = "O" if current_turn == "X" else "X"

# Entry point of the program
if __name__ == "__main__":
    # Main game loop (allows playing multiple games)
    while True:
        run_game()  # Start a new game
        # Ask if player wants to play again
        restart = input("\nPlay another game? (y/n): ").lower()
        if restart != 'y':
            print("Game over. Thanks for playing!")
            break  # Exit program