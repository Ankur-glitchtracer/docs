# 🏗️ MVC Pattern: CLI Task Manager

## 📝 Overview
The **Model-View-Controller (MVC)** pattern separates an application into three main logical components: the Model (Data), the View (UI), and the Controller (Logic). This separation helps manage complexity and promotes organized, testable code.

!!! abstract "Core Concepts"

    - **Separation of Concerns:** Keeping data logic, user interface logic, and coordination logic in distinct layers.
        - **Independent Evolution:** You should be able to change the View (e.g., CLI to GUI) without touching the Model.

!!! info "Why Use This Pattern?"

    - **Separates data, logic, and presentation**
    - **Allows independent development of components**
    - **Supports multiple views for the same data**

## 🚀 Problem Statement
Design a command-line To-Do application. If you mix user input handling, task storage, and display logic in a single file, the app becomes a "God Object" that is impossible to maintain or unit test.

## 🛠️ Requirements

1.  **Model:** A `TaskModel` that manages a list of tasks (name, status, timestamp).
2.  **View:** A `TaskView` for rendering the list and capturing user input.
3.  **Controller:** A `TaskController` that bridges the two, handling commands like `add`, `delete`, and `complete`.

### Technical Constraints

- **Unidirectional Flow:** The Model should never know about the View.
- **Mediation:** The View should never update the Model directly; all changes must pass through the Controller.

## 🧠 Thinking Process & Approach
(To be detailed...)

## 💻 Solution Implementation

```python
# (To be detailed...)
```

!!! success "Why this works"
    It makes the application modular and highly testable. Because the `Model` is pure data logic, it can be tested without any UI. Because the `View` is pure display, it can be swapped for a web or mobile interface without changing a single line of business logic.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Observer](../observer/basic_observer/PROBLEM.md) — The Model-View relationship in MVC is often implemented using Observer.
- [Strategy](../strategy/sprinkler_system/PROBLEM.md) — The Controller in MVC is often a Strategy for the View.
- [Composite](../../structural/composite/organisation_chart/PROBLEM.md) — The View in MVC is often a Composite tree.
