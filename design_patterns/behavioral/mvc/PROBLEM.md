# 🏗️ MVC Pattern: CLI Task Manager

## 📝 Overview
The **Model-View-Controller (MVC)** pattern separates an application into three main logical components: the Model (Data), the View (UI), and the Controller (Logic). This separation helps manage complexity and promotes organized, testable code.

!!! abstract "Core Concepts"
    - **Separation of Concerns:** Keeping data logic, user interface logic, and coordination logic in distinct layers.
    - **Independent Evolution:** You should be able to change the View (e.g., CLI to GUI) without touching the Model.

## 🚀 Problem Statement
Design a command-line To-Do application. If you mix user input handling, task storage, and display logic in a single file, the app becomes a "God Object" that is impossible to maintain or unit test.

### Technical Constraints
- **Unidirectional Flow:** The Model should never know about the View.
- **Mediation:** The View should never update the Model directly; all changes must pass through the Controller.

## 🛠️ Requirements
1.  **Model:** A `TaskModel` that manages a list of tasks (name, status, timestamp).
2.  **View:** A `TaskView` for rendering the list and capturing user input.
3.  **Controller:** A `TaskController` that bridges the two, handling commands like `add`, `delete`, and `complete`.

!!! success "Why this works"
    It makes the application modular and highly testable. Because the `Model` is pure data logic, it can be tested without any UI. Because the `View` is pure display, it can be swapped for a web or mobile interface without changing a single line of business logic.
