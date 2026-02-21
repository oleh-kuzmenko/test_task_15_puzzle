# 15 Puzzle Game

A terminal-based Python implementation of the classic 15 Puzzle game.  

The game is represented by a 4x4 board with 15 numbered tiles and one empty space.  
To win, you need to arrange tiles in order from 1 to 15, with the empty space at the bottom-right corner.

---

## How to Run the Game

### Using Python

1. Ensure **Python 3.14+** is installed.
2. Navigate to the project directory.
3. (Optional but recommended) install the project in **editable mode**:

```bash
pip install -e .
```
This allows Python to recognize the sliding_puzzle package for imports and tests.

4. Run the main entrypoint:
```bash
python main.py
```

5. Follow the on-screen prompts:
- Enter a tile number to move.
- Enter `q` at any time to quit.

### Using Docker

1. Build the Docker image from the project root:

```bash
docker build -t 15-puzzle .
```

2. Run the game inside an interactive Docker container:

```bash
docker run -it 15-puzzle
```


## How to Run Tests

1. Install the testing framework and dependencies:

```bash
pip install -r requirements.txt
```

2. Run all tests using pytest:

```bash
pytest tests -vv
```


## Project Structure & Architecture

The application follows a **Model-View-Controller (MVC)** pattern, separating game logic, presentation, and orchestration.

### Project Structure

```text
sliding_puzzle/           # Main package
├── __init__.py           # Exposes PuzzleBoard, ConsoleView, GameController
├── puzzle_board.py       # Model
├── console_view.py       # View
└── game_controller.py    # Controller
tests/                    # Unit tests
├── test_puzzle_board.py
├── test_console_view.py
└── test_game_controller.py
main.py                   # Entry point
pyproject.toml
README.md
requirements.txt
Dockerfile
```

### Class Interaction Diagram

```text
                      +-------------------+
                      |   GameController  |
                      |  (Orchestrates)   |
                      +---------+---------+
                                |
          ----------------------+----------------------
          |                                           |
          v                                           v
 +-----------------+                          +-----------------+
 |   PuzzleBoard   |                          |   ConsoleView   |
 |-----------------|                          |-----------------|
 | - Board state   |                          | - Draw board    |
 | - Solvability   |                          | - Show message  |
 | - Move validity |                          | - Get move      |
 +-----------------+                          +-----------------+
 ```

- `GameController` orchestrates the game loop and connects the model and view.
- `PuzzleBoard` handles all game rules, move validation, and board state.
- `ConsoleView` manages console input/output and rendering.