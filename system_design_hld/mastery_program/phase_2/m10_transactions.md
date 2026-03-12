# Module 10: Distributed Transactions & Saga Patterns

### 🚀 Problem Statement
Reverting a document revision must atomically:

1. Create a new document version
2. Clone all sections, tasks, risks, and control measures
3. Clone comments with remapped entity IDs
4. Update the search index
5. Invalidate caches

If step 3 fails while steps 1-2 are already committed, orphaned data remains in the system.

### 🧠 The Engineering Story

**The Villain:** "The Partial Commit." In a monolith, this was one database transaction. In microservices, each service has its own database. There's no distributed `BEGIN...COMMIT`.

**The Hero:** "The Saga Choreographer." Each step publishes an event on success. If a step fails, compensating events undo previous steps (e.g., `DocumentCreated` → on failure → `DocumentDeleted`).

**The Plot:**

1. Understand why 2PC (Two-Phase Commit) doesn't scale
2. Design Choreography-based Sagas (events trigger next step)
3. Design Orchestration-based Sagas (central coordinator)
4. Implement compensating transactions for each step

**The Twist (Failure):** **The Phantom Compensation.** A compensating action for "clone comments" might be "delete cloned comments." However, if a reply is added to one of the cloned comments before the compensation occurs, deleting the comment will orphan the reply.

**Interview Signal:** Can choose between choreography vs orchestration sagas and design compensating transactions.

### 📝 Design Exercise
> Design a Saga for the document revision workflow across 3 services (Document Service, Core Engine, Comment Service). Define the happy path, compensating actions for each step, and how to handle the case where a compensating action itself fails.
