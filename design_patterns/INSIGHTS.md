# 🧠 Design Patterns Insights

Use this file to document your learning and key takeaways for each design pattern.

## 🟢 Creational Patterns
### AI Insights:
- **Singleton Pattern:** Ensure thread safety using `threading.Lock` if the application will be multi-threaded.
- **Factory/Abstract Factory:** Excellent for decoupling object creation from business logic, making the code highly testable.
- **Object Pool:** Crucial for managing expensive resources like DB connections to prevent overhead.

### 💡 Manual Insights:
- [Add your thoughts here...]

---

## 🟡 Structural Patterns
### AI Insights:
- **Facade Pattern:** Your `smart_home_facade.py` is a great example of simplifying a complex subsystem for the client.
- **Decorator Pattern:** Perfect for "Build Your Own" scenarios (like the pizza builder) where combinations are dynamic.
- **Proxy Pattern:** Use this for lazy loading of heavy objects to improve initial startup time.

### 💡 Manual Insights:
- [Add your thoughts here...]

---

## 🟡 Behavioral Patterns
### AI Insights:
- **Observer Pattern:** Your use of an `EventBus` and `Subscriber` protocol shows good use of modern Python typing and decoupling.
- **State Pattern:** Effective for systems with complex lifecycles like document workflows or gumball machines to avoid nested `if-else` blocks.
- **Strategy Pattern:** Ideal for interchangeable algorithms (like sprinkler schedules) that can vary at runtime.

### 💡 Manual Insights:
- [Add your thoughts here...]
