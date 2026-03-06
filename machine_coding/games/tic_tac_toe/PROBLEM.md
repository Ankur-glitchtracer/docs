# ❌ Machine Coding: Scalable Tic-Tac-Toe

## 📝 Overview
Implement a standard **Tic-Tac-Toe** game for two players on a 3x3 grid. This machine coding challenge emphasizes clean object-oriented design, win-detection algorithms, and state management.

!!! abstract "Core Concepts"
    - **Grid Representation:** Using a 2D array or flat list to manage board state efficiently.
    - **Win Pattern Matching:** Checking rows, columns, and diagonals for three-in-a-row.

## 🚀 Problem Statement
Build a 2-player game where participants (X and O) take turns marking spaces in a 3x3 grid. The system must accurately detect win conditions (horizontal, vertical, or diagonal) and handle draw scenarios.

## 🧠 Thinking Process & Approach
Game logic requires a clear separation of board state and winning rules. The approach uses a 2D grid representation and a rule engine to check for row, column, or diagonal completion after every turn.

### Key Observations:
- Grid-based state management.
- Efficient win-condition checking.

### Technical Constraints
- **Input Validation:** Prevent players from choosing a square that is already occupied.
- **Efficiency:** The win-check algorithm should ideally be optimized for $O(1)$ or $O(N)$ performance where $N$ is the board size.

