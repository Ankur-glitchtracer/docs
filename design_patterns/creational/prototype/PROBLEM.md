# 🐑 Prototype Pattern: Object Cloning Registry

## 📝 Overview
The **Prototype Pattern** allows you to create new objects by copying an existing instance (the prototype) instead of creating them from scratch using a constructor. This is particularly useful when object creation is expensive or when you want to avoid a complex hierarchy of factories.

!!! abstract "Core Concepts"
    - **Cloning:** Creating a "deep copy" of an object to ensure independence.
    - **Prototype Registry:** A centralized cache of pre-configured objects that can be cloned on demand.

## 🚀 Problem Statement
Imagine a game where you need to spawn hundreds of "Soldier" or "Monster" NPCs. Each NPC has a heavy initialization process (loading assets, setting complex stats). If you use `new Soldier()` every time, the game will stutter. Instead, you should create one "Master Soldier" and clone it whenever a new one is needed.

### Technical Constraints
- **Deep vs Shallow Copy:** Ensure that nested objects (like a soldier's equipment) are cloned correctly so that changing one NPC's gear doesn't affect another.
- **Dynamic Configuration:** The system should allow cloning an object and then slightly modifying its properties (e.g., changing a soldier's color or position).

## 🛠️ Requirements
1.  **Prototype Interface:** Define a `clone()` method in a base class.
2.  **Concrete Prototypes:** Implement `Soldier` and `Monster` classes.
3.  **Registry:** Create a `ShapeRegistry` or `NPCRegistry` that stores prototypes and provides clones via a `get_prototype(type)` method.

!!! success "Why this works"
    It reduces the overhead of complex initialization. By cloning pre-configured objects, you can "spawn" complex entities instantly and maintain a flexible system where new types of objects can be added to the registry at runtime.
