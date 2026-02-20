from sliding_puzzle.game_controller import GameController
from sliding_puzzle.console_view import ConsoleView
from sliding_puzzle.puzzle_board import PuzzleBoard

class MockView(ConsoleView):
    def __init__(self, moves):
        super().__init__(max_tile=8)
        self.moves = iter(moves)
        self.messages = []
        self.draw_calls = 0

    def draw_board(self, board, status_msg=""):
        self.draw_calls += 1

    def show_message(self, msg):
        self.messages.append(msg)

    def get_move(self):
        return next(self.moves, None)

def test_controller_solve():
    controller = GameController(size=3)
    controller.board.board = [1,2,3,4,5,6,7,0,8]
    controller.view = MockView(moves=[8])
    controller.run()
    assert any("Congratulations" in m for m in controller.view.messages)

def test_controller_quit():
    controller = GameController(size=3)
    controller.view = MockView(moves=[None])
    controller.run()
    assert any("quit" in m.lower() for m in controller.view.messages)
