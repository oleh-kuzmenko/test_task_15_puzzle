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

        if PuzzleBoard._is_adjacent(tile_idx, empty_idx, self.size):
            self.board[tile_idx], self.board[empty_idx] = self.board[empty_idx], self.board[tile_idx]
            return True
        return False


    def _generate_solvable_board(self) -> List[int]:
        import random

        board = self._solved_board[:]
        while True:
            random.shuffle(board)
            if PuzzleBoard._is_solvable(board, self.size) and board != self._solved_board:
                return board[:]

    @staticmethod
    def _is_adjacent(idx1: int, idx2: int, size: int) -> bool:
        x1, y1 = divmod(idx1, size)
        x2, y2 = divmod(idx2, size)
        # Manhattan distance = 1 → adjacent
        return abs(x1 - x2) + abs(y1 - y2) == 1

    @staticmethod
    def _is_solvable(board: List[int], size: int) -> bool:
        inversions = PuzzleBoard._count_inversions(board)
        empty_row_from_bottom = size - (board.index(PuzzleBoard.EMPTY) // size)

        if size % 2 == 1:
            # For odd-sized boards: solvable if inversions count is even
            return inversions % 2 == 0
        if empty_row_from_bottom % 2 == 0:
            # Empty tile on an even row from bottom → inversions must be odd
            return inversions % 2 == 1
        else:
            # Empty tile on an odd row from bottom → inversions must be even
            return inversions % 2 == 0

    @staticmethod
    def _count_inversions(board: List[int]) -> int:
        # Count all pairs where a larger tile comes before a smaller one
        inversions = 0
        for i in range(len(board)):
            if board[i] == PuzzleBoard.EMPTY:
                continue
            for j in range(i + 1, len(board)):
                if board[j] == PuzzleBoard.EMPTY:
                    continue
                if board[i] > board[j]:
                    inversions += 1
        return inversions
    