# 🗺️ Design Patterns Roadmap

A high-level guide to mastering GoF design patterns and architectural best practices.

```mermaid
flowchart TD

subgraph Creational
    direction TB
    C1[Factory]
    C2[Singleton]
    C3[Builder]
    C4[Prototype]
    C5[Abstract Factory]
    C6[Object Pool]
end

subgraph Structural
    direction TB
    S1[Adapter]
    S2[Bridge]
    S3[Composite]
    S4[Decorator]
    S5[Facade]
    S6[Flyweight]
    S7[Proxy]
end

subgraph Behavioral
    direction TB
    B1[Strategy]
    B2[Observer]
    B3[Command]
    B4[State]
    B5[Template]
    B6[Iterator]
    B7[Mediator]
    B8[Memento]
    B9[Chain Of Responsibility]
    B10[Visitor]
    B11[Interpreter]
    B12[MVC]
    B13[Null Object]
end

Creational --> Structural
Structural --> Behavioral
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
