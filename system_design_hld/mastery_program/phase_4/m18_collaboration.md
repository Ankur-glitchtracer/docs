# Module 18: Real-Time Collaborative Systems

### 🚀 Problem Statement
Three system architects are editing the same enterprise document simultaneously. Each adds comments, modifies data records, and updates control measures. Without real-time collaboration, they overwrite each other's work. The last save wins, and two hours of work is lost.

### 🧠 The Engineering Story

**The Villain:** "The Last-Write-Wins." Two engineers load the same document. Both edit different sections. Both save. The second save overwrites the first entirely.

**The Hero:** "The Operational Transform / CRDT." Concurrent edits are captured as operations that can be merged deterministically, regardless of arrival order.

**The Plot:**

1. Understand OT (Operational Transform) vs CRDT (Conflict-free Replicated Data Types)
2. Design presence awareness: show who's viewing/editing which section
3. Implement optimistic locking with conflict resolution UI
4. Real-time sync via WebSocket with event ordering

**The Twist (Failure):** **The CRDT Semantics Gap.** CRDTs guarantee convergence but not intent. Engineer A deletes a risk because it's irrelevant. Engineer B adds a control measure to the same risk. CRDT merges both: the risk exists with the new control but was "deleted." Neither engineer's intent is preserved.

**Interview Signal:** Can compare OT vs CRDT and explain when simpler approaches (pessimistic locking per section) are more appropriate.

### 🔗 Case Study References
- [Socket Chat App](../../../infrastructure_challenges/socket_chat_app/PROBLEM.md) — For real-time state synchronization using WebSockets.
