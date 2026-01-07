#!/usr/bin/env python3
"""
Simple Tic-Tac-Toe (3x3) console game for two local players.

Usage:
    python tic_tac_toe.py
"""

from typing import List, Optional

WIN_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def print_board(board: List[str]) -> None:
    """Print the board in a human-friendly 3x3 layout."""
    cells = [c if c != " " else str(i + 1) for i, c in enumerate(board)]
    print("\n")
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print("\n")


def check_winner(board: List[str]) -> Optional[str]:
    """Return 'X' or 'O' if there is a winner, otherwise None."""
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def is_draw(board: List[str]) -> bool:
    """Return True if the board is full and there is no winner."""
    return all(cell != " " for cell in board) and check_winner(board) is None


def get_move(board: List[str], player: str) -> int:
    """Prompt the player for a move and return the chosen index (0-8)."""
    while True:
        try:
            choice = input(f"Player {player}, enter a move (1-9): ").strip()
            if not choice:
                print("Please enter a number between 1 and 9.")
                continue
            pos = int(choice) - 1
            if pos < 0 or pos > 8:
                print("Invalid position. Choose a number from 1 to 9.")
                continue
            if board[pos] != " ":
                print("That cell is already taken. Pick another one.")
                continue
            return pos
        except ValueError:
            print("Please enter a valid integer from 1 to 9.")
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted. Exiting game.")
            raise SystemExit


def play_game() -> None:
    board = [" "] * 9
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1 to 9 as shown on the board.")
    print_board(board)

    while True:
        move = get_move(board, current_player)
        board[move] = current_player
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins! Congratulations!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


def main() -> None:
    try:
        while True:
            play_game()
            again = input("Play again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                print("Thanks for playing. Goodbye!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
