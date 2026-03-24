# 🏗️ Guide: Design Principles & OOP Concepts

## 📝 Overview

Object-Oriented Programming (OOP) concepts and design principles are the foundational building blocks of Low-Level Design (LLD). They help structure code into clean, maintainable, and extensible systems.

In interviews, these principles guide decisions around abstraction, encapsulation, and separation of responsibilities without over-engineering.

### Why This Matters

* **Core Skill:** Translating ambiguous requirements into structured class designs
* **Interview Relevance:** Interviewers evaluate class organization, coupling, and design clarity
* **Real-world Use:** Enables scalable, maintainable production systems
* **Common Mistake:** Over-engineering or prematurely applying design patterns

---

## 🧠 Core OOP Concepts

### 🔑 Encapsulation

**Definition:** Hiding internal state and exposing controlled behavior.

**Key Idea:** External code interacts via methods, not direct state manipulation.

**Example:** `BankAccount` exposes `deposit()` and `withdraw()` instead of direct balance access.

**When to Use:** Always by default.

**When Not to Use:** Simple data containers (DTOs).

---

### 🔑 Abstraction

**Definition:** Exposing only essential behavior while hiding implementation details.

**Key Idea:** Focus on *what* not *how*.

**Example:** `PaymentMethod.process()` hides Stripe/PayPal logic.

**When to Use:** When multiple implementations or complexity exists.

**When Not to Use:** When only one implementation exists (avoid unnecessary abstraction).

---

### 🔑 Polymorphism

**Definition:** Different objects respond to the same method in different ways.

**Key Idea:** Eliminates type-checking conditionals.

**Example:** `Vehicle.park()` behaves differently for `Car` and `Truck`.

**When to Use:** When behavior varies by type.

**When Not to Use:** When it reduces clarity without real extensibility benefit.

---

### 🔑 Inheritance

**Definition:** A class derives behavior from another class.

**Key Idea:** Enables reuse but increases coupling.

**Example:** `SavingsAccount` extends `BankAccount`.

**When to Use:** Stable, shared behavior hierarchy.

**When Not to Use:** When modeling behavior differences better suited for composition.

---

## 🧱 SOLID Principles

### S — Single Responsibility Principle (SRP)

A class should have only one reason to change.

---

### O — Open/Closed Principle (OCP)

Classes should be open for extension but closed for modification.

---

### L — Liskov Substitution Principle (LSP)

Subclasses should be substitutable for their base classes.

---

### I — Interface Segregation Principle (ISP)

Prefer small, focused interfaces over large ones.

---

### D — Dependency Inversion Principle (DIP)

Depend on abstractions, not concrete implementations.

---

## 🏗️ Mental Models

### Core Idea

Treat principles as **guardrails**, not rules.

* Prefer composition over inheritance
* Prefer simplicity over premature abstraction
* Add complexity only when needed

---

### Key Heuristics

* **KISS:** Keep it simple
* **DRY:** Avoid duplication
* **YAGNI:** Don’t build future requirements early
* **Separation of Concerns:** Each component has one job
* **Law of Demeter:** Avoid deep object chains

---

### Rule of Thumb

Start simple. Introduce SOLID and patterns only when required by complexity or extensibility needs.

---

## 👃 Code Smells → Fixes

| Code Smell                     | Problem                 | Fix                          |
| ------------------------------ | ----------------------- | ---------------------------- |
| Large switch on types          | Violates polymorphism   | Use Strategy pattern         |
| Deep method chaining           | Violates Law of Demeter | Move behavior closer to data |
| Class doing multiple jobs      | Violates SRP            | Split responsibilities       |
| Interface with unused methods  | Violates ISP            | Split interfaces             |
| Inheritance misuse             | Tight coupling          | Use composition              |
| Concrete dependency in service | Violates DIP            | Inject abstractions          |

---

## ⚙️ Practical Example

### Bad Design

```python
class PaymentProcessor:
    def process(self, payment_type, amount):
        if payment_type == "credit":
            ...
        elif payment_type == "paypal":
            ...
```

---

### Good Design (Polymorphism)

```python
class PaymentMethod:
    def process(self, amount):
        pass

class CreditCard(PaymentMethod):
    def process(self, amount):
        ...

class PayPal(PaymentMethod):
    def process(self, amount):
        ...

class PaymentProcessor:
    def process(self, method: PaymentMethod, amount):
        method.process(amount)
```

---

## 🏢 Real-World Example

### Amazon Locker Design

* `Compartment` handles its own state (`occupied`, `free`, `out_of_service`)
* `AccessToken` handles expiration logic
* `LockerSystem` orchestrates components

**Key Insight:**
Each class owns its own responsibility, preventing a monolithic design.

---

## ⚖️ Trade-offs

| Concept     | Benefit          | Trade-off                  |
| ----------- | ---------------- | -------------------------- |
| Inheritance | Code reuse       | Tight coupling             |
| Composition | Flexibility      | More boilerplate           |
| Abstraction | Clean design     | Can over-engineer          |
| DRY         | Less duplication | Risk of incorrect coupling |

---

## 🔄 Key Comparisons

### DIP vs Dependency Injection

* **DIP:** Design principle
* **DI:** Technique to achieve it

---

### Principles vs Patterns

* **Principles:** Guidelines for design
* **Patterns:** Reusable solutions built using principles

---

## 🎤 Interview Focus

* Correct separation of state vs behavior
* Ability to extend design cleanly
* Avoid premature abstraction
* Prefer simplicity first

---

## 🚀 How to Apply

1. Start with simplest working design
2. Identify entities using nouns → classes
3. Apply encapsulation first
4. Introduce polymorphism when variation appears
5. Refactor toward SOLID only when needed

---

## 🔗 Related Topics

* Low-Level Design Framework
* Design Patterns (Strategy, Factory, Observer)
* System Design Fundamentals
