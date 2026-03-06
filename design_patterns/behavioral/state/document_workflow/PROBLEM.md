# 📑 State Pattern: Enterprise Document Workflow

## 📝 Overview
The **State Pattern** allows an object to alter its behavior when its internal state changes. This is particularly useful for managing complex lifecycles where the same action (e.g., `publish()`) has completely different outcomes depending on the current stage.

!!! abstract "Core Concepts"
    - **State Transition:** Logic for moving between stages (Draft -> Review -> Published) is encapsulated within state objects.
    - **Context Delegation:** The `Document` remains a simple wrapper that delegates all behavior to its current `State`.

## 🚀 Problem Statement
Imagine a document editor where a file can be in `Draft`, `Moderation`, or `Published` states. Using a giant `switch` or `if-else` block to handle permissions and transitions for each state makes the code brittle and hard to test as new states are added.

### Technical Constraints
- **Admin Overrides:** Transitions in the `Moderation` state should only proceed to `Published` if the user has admin privileges.
- **Action Idempotency:** Calling `publish()` on a document that is already `Published` should have no effect.

## 🛠️ Requirements
1.  **Context Class:** A `Document` that maintains a reference to a `State` object.
2.  **State Interface:** Define common methods like `render()` and `publish()`.
3.  **Concrete States:** Implement `DraftState`, `ModerationState`, and `PublishedState`.
4.  **Transition Logic:** Ensure states can trigger transitions back to the `Document` context.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/state/document_workflow/document_workflow.py"
```

!!! success "Why this works"
    It localizes state-specific behavior. If the business decides to add an `Archived` state, you simply create a new `ArchivedState` class without touching the logic for `Draft` or `Published`, adhering to the Open/Closed Principle.
