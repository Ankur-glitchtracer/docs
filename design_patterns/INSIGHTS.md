# 🧠 Design Patterns: The Engineering Storybook

This document transforms dry technical patterns into memorable engineering narratives. Use this to master the "Why" behind the "How".

---

## 🟢 Creational Patterns

### 🏭 Abstract Factory

**The Villain:** "Dependency Chaos." Your client code is riddled with `if os == 'Windows': create_button()` checks. Adding a new theme requires editing 50 files.

**The Hero:** "The Kit Provider." A single interface that dispenses families of related objects without specifying their concrete classes.

**The Plot:**

1. Define an interface for creating all products (Buttons, Windows).
2. Create concrete factories for each variant (MacFactory, WinFactory).
3. Client code asks the factory for a button, never knowing if it's Mac or Windows.

**The Twist (Failure):** If ignored, you get **Inconsistent UI States** where a Mac scrollbar appears on a Windows window.

**Interview Signal:** Demonstrates ability to enforce **Consistency** across product families.

### 🏗️ Builder

**The Villain:** "The Telescoping Constructor." `new User(name, null, null, null, true, 18, null...)`.

**The Hero:** "The Step-by-Step Assembler." Constructs complex objects step-by-step.

**The Plot:**

1. Isolate the construction code from the product.
2. Allow different builder implementations to create different representations (JSON, HTML, SQL) of the same data.

**The Twist (Failure):** **Fragile Object Creation**. Adding one optional parameter breaks all existing instantiation code.

### 🧵 Singleton

**The Villain:** "The Identity Crisis." Multiple instances of a configuration manager lead to conflicting settings and race conditions across the app.

**The Hero:** "The Unique One." Ensures a class has only one instance and provides a global point of access.

**The Plot:**

1. Use a private class attribute to store the instance.
2. Override `__new__` or use a decorator to control instantiation.
3. Ensure thread safety with locks in multi-threaded environments.

**The Twist (Failure):** **Configuration Drift**. Two different "Loggers" writing to the same file but with different buffering logic, corrupting the logs.

**Interview Signal:** Demonstrates understanding of **Resource Management** and **Concurrency**.

### 🏊 Object Pool

**The Villain:** "The Exhaustion." Opening and closing database connections for every request is slow and crashes the DB due to connection overhead.

**The Hero:** "The Lending Library." Maintains a collection of initialized objects ready for use.

**The Plot:**

1. Pre-create a set of objects.
2. Clients "borrow" an object and "return" it when done.
3. Handle exhaustion (wait, grow, or fail).

**The Twist (Failure):** **Connection Leaks**. Clients borrow connections but never return them, eventually stalling the entire application.

**Interview Signal:** Critical for **Performance Optimization** in high-throughput systems.

### 🐑 Prototype

**The Villain:** "The Expensive Constructor." Creating a new object requires a heavy database call, a complex 3D render, or a computation you've already finished. Doing it again from scratch is a waste of CPU.

**The Hero:** "The Clone Machine." Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.

**The Plot:**

1. Define a `clone()` method in the base class or interface.
2. The concrete object implements `clone()` by performing a shallow or deep copy of itself.
3. The client asks an existing object to clone itself instead of calling `new`.

**The Twist (Failure):** **Deep vs. Shallow Confusion**. Cloned objects sharing the same reference to a nested list, leading to "spooky action at a distance" where changing one clone affects all others.

---

## 🟡 Structural Patterns

### 🔌 Adapter

**The Villain:** "The Square Peg." You need to use a new analytics library, but it expects data in JSON, and your legacy system outputs XML.

**The Hero:** "The Translator." Wraps an incompatible object to make it look like a compatible one.

**The Plot:**

1. Create a wrapper class that implements the *target* interface.
2. The wrapper translates calls to the *adaptee's* format.

**The Twist (Failure):** **Vendor Lock-in**. Without adapters, switching 3rd-party libraries requires rewriting your core business logic.

### 🌉 Bridge

**The Villain:** "The Cartesian Product Explosion." You have `RemoteControl` and `TV` classes. If you have 2 remotes and 2 TVs, you might end up with `RemoteA_TV1`, `RemoteA_TV2`, `RemoteB_TV1`, etc.

**The Hero:** "The Connector." Decouples an abstraction from its implementation so that the two can vary independently.

**The Plot:**

1. Put the abstraction and implementation in separate class hierarchies.
2. The Abstraction contains a reference to the Implementation.
3. Abstraction delegates the work to the Implementation.

**The Twist (Failure):** **Coupled Evolution**. Changing the UI layout of the remote forces you to modify the internal circuitry of every TV.

### 🌳 Composite

**The Villain:** "The Hierarchy Headache." You are building an organisation chart. Your code has to check if an object is an `Employee` (Leaf) or a `Manager` (Composite) every time you want to calculate total salary, leading to duplicate tree-traversal logic everywhere.

**The Hero:** "The Tree Unifier." Treats individual objects and compositions of objects uniformly.

**The Plot:**

1. Define a common interface for both Leaves and Composites (e.g., `get_salary()`).
2. The Leaf implements the operation directly.
3. The Composite stores a list of children and delegates the operation to them, summing the results.

**The Twist (Failure):** **Type Safety vs. Uniformity**. If you add management-only methods (like `add_employee`) to the base interface, Leaf objects will have to throw errors or do nothing, complicating the API.

### 🎭 Decorator

**The Villain:** "Class Explosion." `CoffeeWithMilk`, `CoffeeWithSugar`, `CoffeeWithMilkAndSugar`...

**The Hero:** "The Wrapper Chain." Dynamically adds responsibilities to objects.

**The Plot:**

1. Implement the same interface as the object you're wrapping.
2. Delegate the main work to the wrapped object.
3. Add your extra behavior before or after the delegation.

**The Twist (Failure):** **Rigid Inheritance**. You can't remove features at runtime or combine them in new ways without creating a new class.

### 🧱 Facade

**The Villain:** "The Complexity Jungle." Your client code has to talk to 10 different subsystem classes (Lights, AC, Security, Music) just to run a "Watch Movie" scene.

**The Hero:** "The Front Desk." Provides a simplified interface to a library, a framework, or any other complex set of classes.

**The Plot:**

1. Create a new class that wraps the complex subsystem.
2. Provide simple methods (e.g., `watchMovie()`) that coordinate the subsystem calls.
3. Clients only talk to the Facade.

**The Twist (Failure):** **Leaky Abstractions**. Clients bypassing the Facade and talking to subsystems directly, leading to inconsistent system states.

### 🍃 Flyweight

**The Villain:** "The Memory Hog." You are simulating a forest with 1,000,000 trees. Each tree stores its coordinates (unique) AND its texture/mesh data (identical). The duplicate 3D data crashes the system.

**The Hero:** "The Resource Sharer." Minimizes memory usage by sharing as much data as possible with other similar objects.

**The Plot:**

1. Separate object state into **Intrinsic** (shared/constant, e.g., Texture) and **Extrinsic** (unique/variable, e.g., Position).
2. Store Intrinsic state in a Flyweight object.
3. Store Extrinsic state in the client or a small context object.
4. Use a Factory to ensure each unique Intrinsic state is only created once.

**The Twist (Failure):** **Performance Tradeoffs**. The time spent looking up shared Flyweights and calculating extrinsic state can sometimes outweigh the memory savings, making the app slower.

### 🛡️ Proxy

**The Villain:** "The Heavy Object." You have a `HighResImage` class that takes 5 seconds to load. Creating 100 images in a list crashes the app or freezes the UI.

**The Hero:** "The Stand-In." Provides a placeholder for another object to control access to it (lazy loading, logging, access control).

**The Plot:**

1. Create a Proxy class with the same interface as the real object.
2. The Proxy stores a reference to the real object and only creates/loads it when a method is actually called.
3. The Proxy can also handle permissions or caching.

**The Twist (Failure):** **Latency Spikes**. The user clicks an item and the app freezes because the Proxy is suddenly performing a heavy initialization on the main thread.

---

## 🟠 Behavioral Patterns

### ⛓️ Chain of Responsibility

**The Villain:** "The Hardcoded Hand-off." Your request handling logic is a giant `if-elif-else` block checking permissions, validation, and rate limiting. Adding a new check means risky edits to a 1,000-line function.

**The Hero:** "The Relay Race." Passes a request along a chain of handlers. Each handler decides either to process the request or pass it to the next handler.

**The Plot:**

1. Define a base handler class with a `set_next()` method.
2. Each concrete handler implements its logic and calls `super().handle()` to pass it on.
3. The client kicks off the chain at the first handler.

**The Twist (Failure):** **The Black Hole**. A request reaches the end of the chain without being handled, and no one is notified, leading to silent failures.

### 👮 Command

**The Villain:** "Hardwired Requests." A UI button directly calls business logic. You can't undo, queue, or log the action.

**The Hero:** "The Request Object." Encapsulates a request as an object.

**The Plot:**

1. Turn a method call (`light.turnOn()`) into an object (`TurnOnCommand(light)`).
2. The Invoker (Button) just calls `execute()`.
3. You can now store these objects in a list for **Undo/Redo**.

**The Twist (Failure):** **Loss of History**. You cannot replay actions to recover from a crash or audit user activity.

### 🧩 Interpreter

**The Villain:** "The Hardcoded Parser." You need to support dynamic business rules like `(A AND B) OR C`, but your code is a mess of nested `if` statements.

**The Hero:** "The Language Builder." Defines a representation for a grammar along with an interpreter to evaluate it.

**The Plot:**

1. Create a class for each terminal and non-terminal symbol.
2. Build an abstract syntax tree (AST).
3. Recursively call `interpret()` on the AST nodes.

**The Twist (Failure):** **Performance Bottlenecks**. For complex grammars, the overhead of the AST can significantly slow down evaluation.

### 🔄 Iterator

**The Villain:** "The Exposed Structure." Your `Menu` uses a `List`, but another `Menu` uses an `Array`. Clients have to write different loops for each, breaking when you change the underlying collection.

**The Hero:** "The Uniform Walker." Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

**The Plot:**

1. Define an Iterator interface (`hasNext()`, `next()`).
2. Each collection provides its own concrete Iterator.
3. Clients use the Iterator interface to loop through any collection.

**The Twist (Failure):** **Concurrent Modification**. Changing the collection while iterating leads to unpredictable behavior or crashes.

### 🕊️ Mediator

**The Villain:** "The Hub-and-Spoke Chaos." Every UI component (Buttons, Checkboxes, Textfields) knows about every other component. Changing a checkbox requires notifying 5 other objects directly, creating a tangled "Spaghetti" graph.

**The Hero:** "The Air Traffic Controller." Defines an object that encapsulates how a set of objects interact.

**The Plot:**

1. Create a Mediator class that manages interactions.
2. Components notify the Mediator of events instead of talking to each other.
3. The Mediator decides which components need to react.

**The Twist (Failure):** **The God Mediator**. The Mediator class becomes too complex and hard to maintain because it contains all the application logic.

### 💾 Memento

**The Villain:** "The Broken State." You want to implement 'Undo', but directly exposing private object state to the "History" manager breaks encapsulation.

**The Hero:** "The Time Capsule." Captures and externalizes an object's internal state so it can be restored later without violating encapsulation.

**The Plot:**

1. The `Originator` creates a `Memento` containing its state.
2. The `Caretaker` (History) stores the `Memento`.
3. The `Originator` restores its state from the `Memento` when requested.

**The Twist (Failure):** **Memory Bloat**. Storing full state snapshots for every minor change can quickly consume all available RAM.

### 🚫 Null Object

**The Villain:** "The NullPointerException Minefield." Your code is 50% `if object is not None: ... else: ...`. Forgetting one check crashes the production environment.

**The Hero:** "The Active Nothing." Provides an object as a surrogate for the lack of an object of a given type. It provides "do nothing" behavior.

**The Plot:**

1. Create a subclass or implement the interface with empty/default methods.
2. Return this "Null Object" instead of `None`.
3. Client code calls methods without checking for null.

**The Twist (Failure):** **Hidden Failures**. The system continues running silently even when a critical component is missing, making debugging difficult.

### 📡 Observer

**The Villain:** "The Polling Loop." Components constantly asking "Are we there yet?" or tight coupling where the `User` class directly calls `EmailService`, `PushNotification`, and `Analytics`.

**The Hero:** "The News Station." Define a subscription mechanism to notify multiple objects about events.

**The Plot:**

1. The `Subject` maintains a list of `Observers`.
2. When state changes, the `Subject` iterates and calls `update()` on all `Observers`.

**The Twist (Failure):** **Cascading Updates**. One event triggers a listener that triggers another event, creating an infinite loop or "Notification Storm."

**Interview Signal:** Critical for designing **Event-Driven Architectures**.

### 🚦 State

**The Villain:** "The State Machine Chaos." A `Document` object with `if status == 'DRAFT': ... elif status == 'PUBLISHED': ...` logic that grows exponentially with every new status.

**The Hero:** "The Dynamic Persona." Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

**The Plot:**

1. Extract state-specific behaviors into separate state classes.
2. The main object (Context) delegates work to its current state object.
3. State objects handle transitions to the next state.

**The Twist (Failure):** **Transition Spaghetti**. If state objects are too tightly coupled to each other, adding a new state requires changing existing ones.

### 🚦 Strategy

**The Villain:** "The Massive Switch Statement." A 500-line function calculating discounts based on `if type == 'BLACK_FRIDAY': ... elif type == 'VIP': ...`.

**The Hero:** "The Plug-and-Play Algorithm." Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

**The Plot:**

1. Define a common interface for the algorithm.
2. Extract each algorithm into its own class.
3. Context class holds a reference to a Strategy object and delegates the work.

**The Twist (Failure):** **Rigidity**. Changing a discount rule requires redeploying the entire billing service.

### 📋 Template Method

**The Villain:** "The Duplicate Workflow." You have `DataExporterCSV` and `DataExporterPDF`. Both have identical logic for "Fetch Data", "Filter Data", and "Cleanup", but only the "Format" step differs. You keep fixing bugs in one and forgetting the other.

**The Hero:** "The Skeleton Blueprint." Defines the skeleton of an algorithm in an operation, deferring some steps to subclasses.

**The Plot:**

1. Create a base class with a final "template method" that calls several other methods.
2. Implement common logic in the base class.
3. Subclasses override only the specific "hook" or "abstract" methods they need to change.

**The Twist (Failure):** **The Inverted Control Trap**. Subclasses may break the algorithm's internal contract if the base class doesn't strictly define which steps are optional vs. mandatory.

### 👁️ Visitor

**The Villain:** "The Modification Fear." You have a complex object structure (like a File System or an AST). You want to add a new feature (like "Calculate Size" or "Export to JSON") without touching the classes of the elements themselves because they are stable or third-party.

**The Hero:** "The Visiting Specialist." Represents an operation to be performed on the elements of an object structure.

**The Plot:**

1. Add an `accept(visitor)` method to all element classes.
2. Create a Visitor interface with `visitElementA()`, `visitElementB()` methods.
3. The element calls the specific visit method on the visitor (`visitor.visitElementA(this)`).

**The Twist (Failure):** **The Double Dispatch Tax**. Every time you add a new Element type, you must update the Visitor interface and all its concrete implementations.

---

## 🎨 Architectural Patterns

### 🏛️ Model-View-Controller (MVC)

**The Villain:** "The God Class." Your UI logic, business logic, and database queries are all in one file. Changing a button's color requires careful navigation around SQL strings.

**The Hero:** "The Trinity." Divides the application into three interconnected components: Model (Data), View (UI), and Controller (Logic).

**The Plot:**

1. **Model** manages the data and business rules.
2. **View** displays the data.
3. **Controller** listens to user input and updates the Model or View.

**The Twist (Failure):** **Massive Controller**. The Controller grows into a "Fat Controller" that handles too much logic, becoming the very God Class you tried to avoid.
