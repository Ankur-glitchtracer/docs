# 🐍 Machine Coding: Modular Snake & Ladder Game

## 📝 Overview
Design and implement a classic **Snake & Ladder** game. This challenge focuses on creating a robust, extensible game engine that handles multiple players, dynamic board configurations, and fair dice mechanics.

!!! abstract "Core Concepts"
    - **Entity Modeling:** Representing the Board, Players, Snakes, and Ladders as distinct, interacting objects.
    - **Game Loop:** Managing turn-based logic and state transitions until a win condition is met.

## 🚀 Problem Statement
The goal is to build a functional Snake & Ladder game on a 10x10 board. Players move based on dice rolls, navigating through ladders (shortcuts) and snakes (setbacks) to be the first to reach exactly square 100.

## 🧠 Thinking Process & Approach
The core of Snake & Ladder is a state-driven game loop. The approach is to model the game using a `Board` that contains `Cells`, where some cells have special properties (Snakes/Ladders). A `Game` controller manages the turn-based logic, dice rolling, and player movement, ensuring that the first player to hit the final square wins.

### Key Observations:
- **Jump Logic:** Snakes and Ladders are essentially "jump" pointers to other cells.
- **Fairness:** The game must maintain a strict queue of players.

### Technical Constraints
- **Board Integrity:** Ensure no infinite loops (e.g., a snake leading back to the same ladder).
- **Exact Finish:** A player must roll the exact number required to land on square 100; otherwise, they remain in place.

## 🛠️ Requirements
1.  **Dynamic Board:** A 10x10 grid with configurable positions for snakes and ladders.
2.  **Multi-Player Support:** Ability to handle `N` players with unique identifiers.
3.  **Dice Mechanics:** Implement a standard 6-sided die (or a configurable $K$-sided die).
4.  **Victory Logic:** Detect and announce the winner when they reach square 100.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/games/snake_ladder/snake_ladder_full.py"
```

!!! success "Why this works"
    By decoupling the board logic from the game controller, the system becomes highly extensible. You can easily add new features like "Booster" squares, multiple dice, or different board sizes without refactoring the core movement logic.
