from sliding_puzzle.puzzle_board import PuzzleBoard

def test_initial_board_is_solvable():
    board = PuzzleBoard(size=4)
    assert len(board.board) == 16
    assert board.EMPTY in board.board

def test_move_tile_valid():
    board = PuzzleBoard(size=3)
    empty_idx = board.board.index(board.EMPTY)
    r, c = divmod(empty_idx, board.size)

    neighbors = []
    if r > 0: neighbors.append(board.board[(r-1)*board.size + c])
    if r < board.size -1: neighbors.append(board.board[(r+1)*board.size + c])
    if c > 0: neighbors.append(board.board[r*board.size + (c-1)])
    if c < board.size -1: neighbors.append(board.board[r*board.size + (c+1)])

    tile_to_move = neighbors[0]
    moved = board.move_tile(tile_to_move)
    assert moved
    assert board.board[empty_idx] == tile_to_move

def test_move_tile_invalid():
    board = PuzzleBoard(size=3)
    empty_idx = board.board.index(board.EMPTY)
    non_adj_idx = (empty_idx + 2) % 9
    tile = board.board[non_adj_idx]

    moved = board.move_tile(tile)
    assert not moved

def test_is_solved():
    board = PuzzleBoard(size=3)
    board.board = list(range(1, board.size*board.size)) + [board.EMPTY]
    assert board.is_solved()
    