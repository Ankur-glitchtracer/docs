# ⏱️ Guide: Low-Level Design Delivery Framework

## 📝 Overview

The Low-Level Design (LLD) delivery framework is a structured, step-by-step methodology for tackling object-oriented design interviews within a constrained 35-minute timeframe. It guides candidates through requirements gathering, entity relationship mapping, class API design, implementation, and extensibility—without getting bogged down in edge cases too early.

This process helps you maintain steady pacing, isolate responsibilities cleanly, and produce code that reflects disciplined, production-grade thinking.

### Why This Matters?

* **Core Skill:** Enables you to convert ambiguous problem statements into clear specifications and well-encapsulated class structures.
* **Interview Relevance:** LLD interviews move fast; poor time management is a common failure mode.
* **Real-world Use:** Mirrors actual engineering workflows—scoping, modeling, API design, and implementation.
* **Common Mistake:** Jumping straight into coding and getting lost in edge cases before defining structure.

---

## 🧠 Core Concepts

### 🔑 Step 1: Requirements

**Definition:** Turning a minimal prompt into a concrete specification.

**Key Idea:** Ask questions across four themes:

* Primary capabilities
* Rules and completion
* Error handling
* Scope boundaries

**Example:** In Tic Tac Toe, define win conditions, draw conditions, and invalid input handling.

**When to Use:** First ~5 minutes.

---

### 🔑 Step 2: Entities and Relationships

**Definition:** Extracting core nouns to define system structure.

**Key Idea:**
An entity:

* Maintains changing state, or
* Enforces rules

If it’s just data, it’s likely a field—not a class.

**Example:** `Game` (orchestrator), `Board`, and `Player`.

**When to Use:** ~3 minutes after requirements.

---

### 🔑 Step 3: Class Design

**Definition:** Defining state (data) and behavior (methods).

**Key Ideas:**

* Work top-down from the orchestrator
* Follow “Tell, Don’t Ask” (encapsulation)

**Example:**

* `Game` tracks current player
* `makeMove()` defines behavior

**When to Use:** ~10–15 minutes.

---

### 🔑 Step 4: Implementation

**Definition:** Writing core logic for key methods.

**Key Idea:**

* Start with the **happy path**
* Then handle edge cases

**Example:** Implement move logic in a board game, then add validations.

**When to Use:** ~10 minutes.

---

### 🔑 Step 5: Extensibility

**Definition:** Adapting the design for new requirements.

**Key Idea:**
Show that your system can evolve cleanly without hacks.

**Example:** Add undo functionality using a command history stack.

**When to Use:** Final ~5 minutes.

---

## 🏗️ Mental Models & Intuition

Think of:

* **System Design** → City map
* **Low-Level Design** → Blueprint of a building

You focus on how internal components interact—not large-scale traffic.

💡 **Rule of Thumb:**
Keep rules with the entity that owns the data.
If one class constantly queries another for decisions, encapsulation is weak.

---

## ⏱️ Execution Strategy

**Requirements (~5 min):**

* Lock scope
* Define what’s out of scope

**Entities (~3 min):**

* Identify orchestrator and supporting classes

**Class Design (~10–15 min):**

* Define state + behavior
* Build APIs top-down

**Implementation (~10 min):**

* Write core logic
* Trace execution step-by-step

**Extensibility (~5 min):**

* Handle “what if” scenarios

---

## 🗣️ Communication Tips

* **Guide, don’t fight:** Follow interviewer direction but maintain structure
* **Ask preferences:** Code vs pseudocode vs discussion
* **Think out loud:** Show reasoning clearly
* **Avoid formal UML:** Use simple class sketches instead

---

## 🧩 Patterns & Techniques

### Entity Filtering Technique

**Rule:**

* Has state or rules → Class
* Just data → Field

Prevents over-engineering.

---

### Verification Tracing

**What:** Mentally simulate execution

**Why:** Catches logical bugs early

**How:**

* Start from initial state
* Apply operations step-by-step
* Track transitions and outcomes

---

## ⚙️ Practical Examples

### Tic Tac Toe Mapping

**Requirement:** Players alternate moves

* **State:** Players, board, turn
* **Behavior:** `makeMove()`, `getCurrentPlayer()`

**Requirement:** Game ends on win/draw

* **State:** Game status, winner
* **Behavior:** `getGameState()`, `getWinner()`

---

### Real-World Example

**Elevator System:**

* Start with `ElevatorController` (entry point)
* Then design `Elevator` for movement logic

Focus on how components interact rather than isolated logic.

---

## ⚖️ Trade-offs

| Approach        | Pros                 | Cons                                    |
| --------------- | -------------------- | --------------------------------------- |
| Formal UML      | Structured, academic | Slow, rarely used in interviews         |
| Simple Diagrams | Fast, flexible       | Less detailed                           |
| Pseudocode      | Clear logic focus    | May not satisfy coding-heavy interviews |

---

## 🎤 Interview Focus

* **State vs Behavior clarity**
* **Ability to trace execution**
* **Clear scope boundaries**
* **Avoid premature coding**

---

## 🚀 How to Apply

1. **Clarify Requirements**
   Define capabilities, rules, and scope

2. **Identify Entities**
   Filter nouns into classes vs fields

3. **Design APIs Top-Down**
   Start with orchestrator

4. **Implement + Trace**
   Build core logic and validate

5. **Handle Extensions**
   Show flexibility in design

---

## 🔗 Related Topics

* **[Design Principles](./principles_and_oop.md):** SOLID, DRY, KISS
* **[OOP Concepts](./principles_and_oop.md):** Encapsulation, Abstraction, Polymorphism
* **[Design Patterns](../../design_patterns/ROADMAP.md):** Strategy, Observer, Factory
