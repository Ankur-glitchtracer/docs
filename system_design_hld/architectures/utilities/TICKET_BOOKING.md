# 🎫 System Design: High-Concurrency Ticket Booking (Thundering Herd)

## 📝 Overview
A **High-Concurrency Ticket Booking** platform designed to handle extreme traffic spikes during flash sales, such as world tour concerts or major sporting events. It utilizes advanced locking strategies, virtual waiting rooms, and idempotent payment processing to ensure reliable seat allocation and prevent system collapse under a "thundering herd" of requests.

!!! abstract "Core Concepts"

    - **Thundering Herd Effect:** A massive, simultaneous spike in requests hitting the same resource (e.g., a popular concert's seat map).
    - **Virtual Waiting Rooms:** Implementing a queue-based entry system to throttle traffic to the core booking engine.
    - **Optimistic vs. Pessimistic Locking:** Balancing performance and consistency when reserving highly contested resources.

## 🛠️ Functional & Non-Functional Requirements
### Functional Requirements

1. **Seat Reservation:** Implement a temporary lock (TTL) on a seat for 10-15 minutes while the user completes the payment.
2. **Dynamic Inventory Updates:** Provide real-time feedback on seat availability to users in the waiting room.
3. **Secure Transaction Processing:** Complete ticket purchases via integrated payment gateways with high reliability.

### Non-Functional Requirements

1. **Extreme Scalability:** System must handle 100x-1000x normal load during flash sale windows.
2. **Data Integrity:** Zero tolerance for double-booking; every seat must be sold to exactly one person.
3. **Low Latency:** The seat selection and reservation flow must be highly responsive to minimize abandonment.

## 🧠 The Engineering Story

**The Villain:** "The Thundering Herd." 1M Taylor Swift fans hitting the "Buy" button at 10:00:00 AM, instantly melting your database with row-level locks on the same 1,000 seats.

**The Hero:** "The Virtual Waiting Room." A message queue or gateway that throttles traffic, only letting 5,000 users into the booking flow at a time.

**The Plot:**

1. **Waiting Room:** Queue users at the entry point and issue session-based tokens to control flow.
2. **Seat Selection:** Use Redis-based distributed locks or DB optimistic locking to reserve a seat temporarily.
3. **Payment:** Hand off to a reliable payment service with unique idempotent keys to prevent double charging.

**The Twist (Failure):** "The Phantom Seat." A user locks a seat, goes to pay, their internet dies, and the seat is "stuck" in a locked state for 15 minutes while other fans can't buy it.

**Interview Signal:** Mastery of **Concurrency Control**, **Message Queuing**, and **Failure-Mode Analysis**.

## 🏗️ High-Level Architecture
Design a system like Ticketmaster or IRCTC that handles extreme traffic spikes during a "flash sale" (e.g., world tour tickets) while ensuring data integrity and a fair user experience.

### Key Design Challenges:

- **Thundering Herd Effect:** Managing thousands of requests hitting the same DB record simultaneously.
- **Locking Strategies:** Choosing between Optimistic (high performance) vs. Pessimistic (high safety) locks for seat allocation.
- **Queueing Architecture:** Implementing a robust waiting room to manage user expectations and system load.
- **Idempotency:** Ensuring a user isn't charged twice if they click "Pay" multiple times due to slow responses.
- **Resilience:** Using the Circuit Breaker pattern to protect the internal services when third-party payment gateways become unstable.

## 🔍 Deep Dives
(To be detailed...)

## 📊 Data Modeling & API Design
### Data Model

- **(To be detailed...)**: (To be detailed...)

### API Design

- **(To be detailed...)**: (To be detailed...)

## 📈 Scalability & Bottlenecks
(To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** (To be detailed...)
- **Scale Question:** (To be detailed...)
- **Edge Case Probe:** (To be detailed...)

## 🔗 Related Architectures

- [Rate Limiter](./RATE_LIMITER.md) — For traffic control and thundering herd mitigation.
