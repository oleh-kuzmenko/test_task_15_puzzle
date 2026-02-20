from .puzzle_board import PuzzleBoard
from .console_view import ConsoleView


class GameController:

    def __init__(self, size: int = 4):
        self.board = PuzzleBoard(size)
        self.view = ConsoleView(max_tile=size*size - 1)

    def run(self):
        self.view.show_message("Welcome to the Sliding Puzzle!")
        status_msg = ""
        while True:
            self.view.draw_board(self.board.board, status_msg)
            status_msg = ""
            if self.board.is_solved():
                self.view.show_message("Congratulations! Puzzle solved.")
                break
            move = self.view.get_move()
            if move is None:
                self.view.show_message("Game quit.")
                break
            if not self.board.move_tile(move):
                status_msg = f"Cannot move tile {move}. Try again."
