# ❌ Machine Coding: Scalable Tic-Tac-Toe

## 📝 Overview
Implement a standard **Tic-Tac-Toe** game for two players on a 3x3 grid. This machine coding challenge emphasizes clean object-oriented design, win-detection algorithms, and state management.

!!! abstract "Core Concepts"
    - **Grid Representation:** Using a 2D array or flat list to manage board state efficiently.
    - **Win Pattern Matching:** Checking rows, columns, and diagonals for three-in-a-row.

## 🚀 Problem Statement
Build a 2-player game where participants (X and O) take turns marking spaces in a 3x3 grid. The system must accurately detect win conditions (horizontal, vertical, or diagonal) and handle draw scenarios.

### Technical Constraints
- **Input Validation:** Prevent players from choosing a square that is already occupied.
- **Efficiency:** The win-check algorithm should ideally be optimized for $O(1)$ or $O(N)$ performance where $N$ is the board size.

## 🛠️ Requirements
1.  **Board Management:** A 3x3 grid with clear display and update methods.
2.  **Turn Management:** Toggle between Player X and Player O after each valid move.
3.  **Termination Logic:** Detect when a player wins or the board is full (Draw).

## 💻 Solution Implementation

```python
--8<-- "machine_coding/games/tic_tac_toe/tic_tac_toe_game.py"
```

!!! success "Why this works"
    The design separates the game's state (the Board) from the game's logic (the Referee). This allows the core engine to be easily extended to larger grids ($N \times N$) or different game variants with minimal changes.
