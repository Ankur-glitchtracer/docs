# 🗺️ Design Patterns Roadmap

A high-level guide to mastering GoF design patterns and architectural best practices.

```mermaid
flowchart TD
    DP[Design Patterns]

    DP --> CRE[Creational Patterns]
    DP --> STR[Structural Patterns]
    DP --> BEH[Behavioral Patterns]
```

---

```mermaid
flowchart TD
    CRE[Creational Patterns]

    CRE --> C1[Factory]
    CRE --> C2[Singleton]
    CRE --> C3[Builder]
    CRE --> C4[Prototype]
    CRE --> C5[Abstract Factory]
    CRE --> C6[Object Pool]
```

---

```mermaid
flowchart TD
    STR[Structural Patterns]

    STR --> S1[Adapter]
    STR --> S2[Bridge]
    STR --> S3[Composite]
    STR --> S4[Decorator]
    STR --> S5[Facade]
    STR --> S6[Flyweight]
    STR --> S7[Proxy]
```

---

```mermaid
flowchart TB
    BEH1[Behavioral Patterns - Core]

    BEH1 --> B1[Strategy]
    BEH1 --> B2[Observer]
    BEH1 --> B3[Command]
    BEH1 --> B4[State]
    BEH1 --> B5[Template Method]
```
```mermaid
flowchart TB
    BEH2[Behavioral Patterns - Interaction]

    BEH2 --> B6[Mediator]
    BEH2 --> B7[Chain Of Responsibility]
    BEH2 --> B8[Visitor]
    BEH2 --> B9[Iterator]
```
```mermaid
flowchart TB
    BEH3[Behavioral Patterns - State & Language]

    BEH3 --> B10[Memento]
    BEH3 --> B11[Interpreter]
    BEH3 --> B12[MVC]
    BEH3 --> B13[Null Object]
```



## 📊 Topic Progress

1.  **Creational Patterns**
    *   [Abstract Factory](./creational/abstract_factory/ui_toolkit/PROBLEM.md)
    *   [Builder](./creational/builder/custom_pc_builder/PROBLEM.md)
    *   [Factory](./creational/factory/coupon_factory/PROBLEM.md)
    *   [Prototype](./creational/prototype/PROBLEM.md)
    *   [Singleton](./creational/singleton/singleton_pattern/PROBLEM.md)
    *   [Object Pool](./creational/object_pool/db_connection_pool/PROBLEM.md)

2.  **Structural Patterns**
    *   [Adapter](./structural/adapter/format_translator/PROBLEM.md)
    *   [Bridge](./structural/bridge/remote_control/PROBLEM.md)
    *   [Composite](./structural/composite/organisation_chart/PROBLEM.md)
    *   [Decorator](./structural/decorator/pizza_builder_decorator/PROBLEM.md)
    *   [Facade](./structural/facade/smart_home_facade/PROBLEM.md)
    *   [Flyweight](./structural/flyweight/forest_simulator/PROBLEM.md)
    *   [Proxy](./structural/proxy/lazy_loading_proxy/PROBLEM.md)

3.  **Behavioral Patterns**
    *   [Strategy](./behavioral/strategy/sprinkler_system/PROBLEM.md)
    *   [Observer](./behavioral/observer/basic_observer/PROBLEM.md)
    *   [Command](./behavioral/command/smart_home_hub/PROBLEM.md)
    *   [State](./behavioral/state/document_workflow/PROBLEM.md)
    *   [Template](./behavioral/template/data_exporter/PROBLEM.md)
    *   [Iterator](./behavioral/iterator/menu_iterator/PROBLEM.md)
    *   [Mediator](./behavioral/mediator/PROBLEM.md)
    *   [Memento](./behavioral/memento/text_editor_history/PROBLEM.md)
    *   [Chain of Responsibility](./behavioral/chain_of_responsibility/PROBLEM.md)
    *   [Visitor](./behavioral/visitor/PROBLEM.md)
    *   [Interpreter](./behavioral/interpreter/rule_engine/PROBLEM.md)
    *   [MVC](./behavioral/mvc/PROBLEM.md)
    *   [Null Object](./behavioral/null_object/discount_system/PROBLEM.md)

Refer to [repo_index.md](../repo_index.md) for a complete list of all implementations.
