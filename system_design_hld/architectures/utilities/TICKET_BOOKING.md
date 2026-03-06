# HLD: High-Concurrency Ticket Booking (Thundering Herd)

## 🚀 Problem Statement
Design a system like Ticketmaster or IRCTC that handles extreme traffic spikes during a "flash sale" (e.g., world tour tickets).

## 🧠 Key Design Challenges
- **Thundering Herd Effect:** Thousands of requests hitting the same DB record simultaneously.
- **Locking Strategies:** Optimistic vs. Pessimistic locks for seat allocation.
- **Queueing:** Implementing a virtual "Waiting Room" to throttle traffic to the backend.
- **Idempotency:** Ensuring a user isn't charged twice if they click "Pay" twice.
- **Resilience:** Using the Circuit Breaker pattern to protect the payment service.
