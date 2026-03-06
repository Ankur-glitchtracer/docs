# HLD: Design an API Rate Limiter

## 🚀 Problem Statement
Design a rate limiter that can be deployed at the edge (API Gateway) to protect services from being overwhelmed.

## 🛠️ Algorithms to Evaluate
1. **Token Bucket:** Allows bursts, simple to implement.
2. **Leaky Bucket:** Constant output rate, smooths traffic.
3. **Fixed Window Counter:** Simple but has "edge" problems (double traffic at window borders).
4. **Sliding Window Logs:** Precise but memory-heavy.
5. **Sliding Window Counter:** Best trade-off between precision and memory.

## 🧠 Distributed Challenges
- **Shared State:** Using Redis for centralized counting.
- **Performance:** Minimizing latency added to every request.
- **Race Conditions:** Using Lua scripts in Redis for atomic "check-and-increment."
