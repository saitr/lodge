import chess
import random

# Function to display the chessboard
def display_board(board):
    print(board)

# Function to get the user's move
def get_user_move(board):
    while True:
        move_str = input("Enter your move (in algebraic notation, e.g., e2e4): ")
        try:
            move = chess.Move.from_uci(move_str)
            if move in board.legal_moves:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid move format. Try again.")

# Function to get the AI's move (with alpha-beta pruning)
def get_ai_move(board, depth, alpha=float('-inf'), beta=float('inf')):
    best_move = None
    best_score = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(board, depth-1, -beta, -alpha)
        board.pop()
        if score > best_score:
            best_score = score
            best_move = move
        alpha = max(alpha, score)
    return best_move

# Alpha-beta pruning algorithm
def alphabeta(board, depth, alpha, beta):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if board.turn:
        max_score = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            score = alphabeta(board, depth - 1, alpha, beta)
            board.pop()
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = float('inf')
        for move in board.legal_moves:
            board.push(move)
            score = alphabeta(board, depth - 1, alpha, beta)
            board.pop()
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score

# Evaluation function
def evaluate_board(board):
    # Add your evaluation logic here
    return random.randint(-100, 100)

# Function to play versus AI game
def play_vs_ai():
    depth = int(input("Enter AI depth level (1-3): "))
    board = chess.Board()
    display_board(board)

    while not board.is_game_over():
        # Get user's move
        move = get_user_move(board)
        board.push(move)
        display_board(board)

        if not board.is_game_over():
            # Get AI's move with specified depth
            ai_move = get_ai_move(board, depth)
            board.push(ai_move)
            print("AI's move: " + ai_move.uci())
            display_board(board)

    result = board.result()
    print("Game over. Result: " + result)

# Main menu
def main_menu():
    while True:
        print("1. Play versus AI")
        print("2. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            play_vs_ai()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
main_menu()
