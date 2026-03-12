# ❌ Machine Coding: Scalable Tic-Tac-Toe

## 📝 Overview
Implement a standard **Tic-Tac-Toe** game for two players on a 3x3 grid. This machine coding challenge emphasizes clean object-oriented design, win-detection algorithms, and state management.

!!! info "Why This Challenge?"

    - **Algorithm Optimization:** Learning how to optimize win detection from $O(N^2)$ to $O(1)$ using incremental counters.
    - **Clean State Management:** Mastering the separation of game state (the board) from game rules (win/draw conditions).
    - **Input Validation & Safety:** Ensuring a robust user interaction layer that prevents illegal moves.

!!! abstract "Core Concepts"

    - **Grid Representation:** Using a 2D array or flat list to manage board state efficiently.
    - **Win Pattern Matching:** Checking rows, columns, and diagonals for three-in-a-row.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Grid Setup:** Initialize a 3x3 (or NxN) board for two players.
2.  **Turn Management:** Handle alternating turns between Player X and Player O.
3.  **Move Validation:** Prevent moves on already occupied cells.
4.  **Win/Draw Detection:** Accurately identify when a player wins or if the game ends in a draw.

### Technical Constraints

- **Efficiency:** The win-check algorithm should ideally be optimized for $O(1)$ performance.
- **Scalability:** The design should easily adapt to larger board sizes (e.g., 10x10) or more than two players.
- **Input Validation:** Prevent players from choosing a square that is already occupied.

## 🧠 The Engineering Story

**The Villain:** "The $O(N^2)$ Scanner." Checking the entire 3x3 (or NxN) board for a winner after every single move using nested loops. As the board grows to 100x100, the game lags.

**The Hero:** "The Incremental Counter." Maintaining arrays for row, column, and diagonal sums to detect a win in $O(1)$ time.

**The Plot:**

1. Represent the `Board` as a grid of `Cells`.
2. Assign +1 for Player X and -1 for Player O.
3. Update `row_sums`, `col_sums`, and `diagonal_sums` on every move.
4. If any sum equals `±N`, declare the winner.

**The Twist (Failure):** **The Index-out-of-Bounds.** Forgetting to handle the "Anti-Diagonal" calculation correctly (where `row + col == N - 1`).

**Interview Signal:** Mastery of **Efficient Win Detection** and clean **State Management**.

## 🚀 Thinking Process & Approach
Game logic requires a clear separation of board state and winning rules. The approach uses a 2D grid representation and a rule engine to check for row, column, or diagonal completion after every turn.

### Key Observations:

- Grid-based state management.
- Efficient win-condition checking.

## 🏗️ Design Patterns Used

- **Strategy Pattern**: For implementing different win-checking algorithms or game variants.
- **Observer Pattern**: To notify the UI or other components when the board state changes or a player wins.
- **Factory Pattern**: To create game pieces or players with different symbols.
- **Singleton Pattern**: For the Game Engine if only one game is expected to run at a time.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/games/tic_tac_toe/tic_tac_toe_game.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **N-Dimensional Tic-Tac-Toe:** How would you extend the win-detection logic to a 3D board (cube)?
- **Undo/Redo:** How would you implement an undo feature using the Command Pattern?
- **AI Opponent:** How would you integrate a basic Minimax algorithm for a single-player mode?

## 🔗 Related Challenges

- [Snake & Ladder](../snake_ladder/PROBLEM.md) — For another turn-based game on a grid.
- [Parking Lot](../../systems/parking_lot/PROBLEM.md) — For entity modeling and state management.
