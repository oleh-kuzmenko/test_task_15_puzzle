from sliding_puzzle.puzzle_board import PuzzleBoard

def test_initial_board_has_correct_structure():
    puzzle_board = PuzzleBoard(size=4)
    assert len(puzzle_board.board) == 16
    assert puzzle_board.EMPTY in puzzle_board.board

def test_known_solved_board_is_solvable():
    puzzle_board = PuzzleBoard(size=4)
    puzzle_board.board = [
        1, 2, 3, 4,
        5, 6, 7, 8,
        9,10,11,12,
        13,14,15, 0
    ]

    assert PuzzleBoard._is_solvable(puzzle_board.board, puzzle_board.size)

def test_known_unsolvable_board():
    puzzle_board = PuzzleBoard(size=4)
    puzzle_board.board = [
        1, 2, 3, 4,
        5, 6, 7, 8,
        9,10,11,12,
        13,15,14, 0
    ]

    assert not PuzzleBoard._is_solvable(puzzle_board.board, puzzle_board.size)

def test_random_initial_board_is_solvable():
    for _ in range(50):
        puzzle_board = PuzzleBoard(size=4)
        assert PuzzleBoard._is_solvable(puzzle_board.board, puzzle_board.size)

def test_move_tile_valid():
    puzzle_board = PuzzleBoard(size=3)
    empty_idx = puzzle_board.board.index(puzzle_board.EMPTY)
    r, c = divmod(empty_idx, puzzle_board.size)

    neighbors = []
    if r > 0: neighbors.append(puzzle_board.board[(r-1)*puzzle_board.size + c])
    if r < puzzle_board.size -1: neighbors.append(puzzle_board.board[(r+1)*puzzle_board.size + c])
    if c > 0: neighbors.append(puzzle_board.board[r*puzzle_board.size + (c-1)])
    if c < puzzle_board.size -1: neighbors.append(puzzle_board.board[r*puzzle_board.size + (c+1)])

    tile_to_move = neighbors[0]
    moved = puzzle_board.move_tile(tile_to_move)
    assert moved
    assert puzzle_board.board[empty_idx] == tile_to_move

def test_move_tile_invalid():
    puzzle_board = PuzzleBoard(size=3)
    empty_idx = puzzle_board.board.index(puzzle_board.EMPTY)
    non_adj_idx = (empty_idx + 2) % 9
    tile = puzzle_board.board[non_adj_idx]

    moved = puzzle_board.move_tile(tile)
    assert not moved

def test_is_solved():
    puzzle_board = PuzzleBoard(size=3)
    puzzle_board.board = list(range(1, puzzle_board.size*puzzle_board.size)) + [puzzle_board.EMPTY]
    assert puzzle_board.is_solved()
    