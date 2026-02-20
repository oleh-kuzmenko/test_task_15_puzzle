from typing import Optional
import os
import subprocess

class ConsoleView:

    QUIT_COMMAND = "q"

    def __init__(self, max_tile: int):
        self.max_tile = max_tile

    @staticmethod
    def clear_screen():
        if os.name == "nt":
            subprocess.run("cls", shell=True)
        else:
            subprocess.run("clear")

    def draw_board(self, board, status_msg=""):
        self.clear_screen()
        size = int(len(board) ** 0.5)
        horizontal_line = "-" * (size * 5 + 1)
        print(horizontal_line)
        for i in range(size):
            row = board[i*size:(i+1)*size]
            row_str = "|"
            for val in row:
                row_str += "    |" if val == 0 else f" {val:2d} |"
            print(row_str)
            print(horizontal_line)
        if status_msg:
            print(status_msg)

    def show_message(self, msg: str):
        print(msg)

    def get_move(self) -> Optional[int]:
        while True:
            user_input = input(
                f"Enter tile number (1-{self.max_tile}) or '{self.QUIT_COMMAND}' to quit: "
            ).strip().lower()

            if user_input == self.QUIT_COMMAND:
                return None

            if not user_input.isdigit():
                print("Invalid input. Enter a number or 'q'.")
                continue

            tile = int(user_input)
            if 1 <= tile <= self.max_tile:
                return tile

            print(f"Please enter a valid tile number (1-{self.max_tile}).")
