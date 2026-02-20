from sliding_puzzle.console_view import ConsoleView

def test_draw_board(capsys):
    view = ConsoleView(max_tile=8)
    board = [1,2,3,4,5,6,7,8,0]
    view.draw_board(board)
    captured = capsys.readouterr().out
    assert "1" in captured
    assert "8" in captured
    assert "0" not in captured

def test_get_move_valid(monkeypatch):
    inputs = iter(["5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    view = ConsoleView(max_tile=8)
    move = view.get_move()
    assert move == 5

def test_get_move_quit(monkeypatch):
    inputs = iter(["q"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    view = ConsoleView(max_tile=8)
    move = view.get_move()
    assert move is None

def test_get_move_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(["x", "9", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    view = ConsoleView(max_tile=8)
    move = view.get_move()
    captured = capsys.readouterr().out
    assert "Invalid input" in captured
    assert "valid tile number" in captured
    assert move == 3
