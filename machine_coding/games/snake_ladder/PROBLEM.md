# 🐍 Machine Coding: Modular Snake & Ladder Game

## 📝 Overview
Design and implement a classic **Snake & Ladder** game. This challenge focuses on creating a robust, extensible game engine that handles multiple players, dynamic board configurations, and fair dice mechanics.

!!! info "Why This Challenge?"

    - **Entity Modeling Mastery:** Learning how to represent real-world game components (Board, Players, Snakes, Ladders) as interacting objects.
    - **State Machine Logic:** Managing turn-based transitions and game states until a win condition is met.
    - **Extensibility:** Designing a system where new rules (e.g., special squares, multiple dice) can be added with minimal code changes.

!!! abstract "Core Concepts"

    - **Entity Modeling:** Representing the Board, Players, Snakes, and Ladders as distinct, interacting objects.
    - **Game Loop:** Managing turn-based logic and state transitions until a win condition is met.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Dynamic Board:** A 10x10 grid with configurable positions for snakes and ladders.
2.  **Multi-Player Support:** Ability to handle `N` players with unique identifiers.
3.  **Dice Mechanics:** Implement a standard 6-sided die (or a configurable $K$-sided die).
4.  **Victory Logic:** Detect and announce the winner when they reach square 100.

### Technical Constraints

- **Board Integrity:** Ensure no infinite loops (e.g., a snake leading back to the same ladder).
- **Exact Finish:** A player must roll the exact number required to land on square 100; otherwise, they remain in place.
- **Fairness:** The game must maintain a strict queue of players.

## 🧠 The Engineering Story

**The Villain:** "The God Class." Putting board layout, player turns, and dice logic into one giant 500-line `while True` loop. Adding a "Special Booster" square requires rewriting half the code.

**The Hero:** "The Entity-Component Separation."

**The Plot:**

1. `Board` handles the 10x10 grid and jump mappings.
2. `Player` tracks the current position.
3. `Game` manages the turn queue and win conditions.
4. `Dice` is a standalone utility (Strategy).

**The Twist (Failure):** **The Infinite Loop.** A snake at square 14 leads to square 7, where a ladder leads back to square 14.

**Interview Signal:** Shows ability to **Modularize Game Logic** and manage turn-based state.

## 🚀 Thinking Process & Approach
The core of Snake & Ladder is a state-driven game loop. The approach is to model the game using a `Board` that contains `Cells`, where some cells have special properties (Snakes/Ladders). A `Game` controller manages the turn-based logic, dice rolling, and player movement, ensuring that the first player to hit the final square wins.

### Key Observations:

- **Jump Logic:** Snakes and Ladders are essentially "jump" pointers to other cells.
- **Fairness:** The game must maintain a strict queue of players.

## 🏗️ Design Patterns Used

- **Strategy Pattern**: For implementing different dice rolling strategies or different board jump types.
- **Singleton Pattern**: For the Game Engine or the Dice utility if shared across multiple games.
- **Command Pattern**: To encapsulate a player's move as a command that can be logged or potentially undone.
- **Factory Pattern**: To create different types of "jumps" (Snakes, Ladders, Boosters).

## 💻 Solution Implementation

```python
--8<-- "machine_coding/games/snake_ladder/snake_ladder_full.py"
```

!!! success "Why this works"
    By decoupling the board logic from the game controller, the system becomes highly extensible. You can easily add new features like "Booster" squares, multiple dice, or different board sizes without refactoring the core movement logic.

## 🎤 Interview Follow-ups

- **Booster Squares:** How would you add a square that gives a player an extra turn?
- **Multiple Dice:** How would you modify the game to use two dice, where a double roll gives another turn?
- **Infinite Loop Detection:** How would you programmatically detect if a board configuration contains an infinite loop?

## 🔗 Related Challenges

- [Tic-Tac-Toe](../tic_tac_toe/PROBLEM.md) — For another turn-based grid game.
- [Elevator System](../../systems/elevator/PROBLEM.md) — For managing state transitions and request queues.
