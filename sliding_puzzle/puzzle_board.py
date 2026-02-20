from typing import List


class PuzzleBoard:

    EMPTY = 0

    def __init__(self, size: int = 4):
        if size < 2:
            raise ValueError("Board size must be >= 2")

        self.size = size
        self._solved_board = list(range(1, size * size)) + [self.EMPTY]
        self.board: List[int] = self._generate_solvable_board()


    def is_solved(self) -> bool:
        return self.board == self._solved_board

    def move_tile(self, tile_value: int) -> bool:
        if tile_value == self.EMPTY:
            return False
        try:
            tile_idx = self.board.index(tile_value)
            empty_idx = self.board.index(self.EMPTY)
        except ValueError:
            return False

        if self._is_adjacent(tile_idx, empty_idx):
            self.board[tile_idx], self.board[empty_idx] = (
                self.board[empty_idx],
                self.board[tile_idx],
            )
            return True
        return False


    def _generate_solvable_board(self) -> List[int]:
        import random

        board = self._solved_board[:]
        while True:
            random.shuffle(board)
            if self._is_solvable(board) and board != self._solved_board:
                return board[:]

    def _is_adjacent(self, idx1: int, idx2: int) -> bool:
        r1, c1 = divmod(idx1, self.size)
        r2, c2 = divmod(idx2, self.size)
        return abs(r1 - r2) + abs(c1 - c2) == 1

    def _is_solvable(self, board: List[int]) -> bool:
        inversions = self._count_inversions(board)
        empty_row_from_bottom = self.size - (board.index(self.EMPTY) // self.size)

        if self.size % 2 == 1:
            return inversions % 2 == 0
        if empty_row_from_bottom % 2 == 0:
            return inversions % 2 == 1
        else:
            return inversions % 2 == 0

    @staticmethod
    def _count_inversions(board: List[int]) -> int:
        arr = [x for x in board if x != PuzzleBoard.EMPTY]
        inversions = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inversions += 1
        return inversions
    