# 🎯 Interview Playbook

Your battle-tested strategy guide for technical interviews. Use this as a pre-interview warm-up and a reference for structuring your answers.

---

## ⏱️ The 45-Minute Framework

| Phase | Time | What To Do |
| :--- | :--- | :--- |
| **1. Clarify** | 3-5 min | Repeat the problem. Ask about edge cases, input size, constraints. _"Can the input be empty? Is it sorted?"_ |
| **2. Approach** | 5-7 min | Talk through 1-2 approaches (brute force → optimized). State time/space complexity for each. Get interviewer buy-in before coding. |
| **3. Code** | 15-20 min | Write clean, modular code. Use helper functions. Name variables clearly. Narrate as you go. |
| **4. Test** | 5-7 min | Trace through with a simple example, then edge cases. Fix bugs aloud. |
| **5. Optimize** | 5-10 min | Discuss trade-offs, alternative approaches. Can you improve space? Parallelize? |

!!! tip "Golden Rule"
    **Never jump to code.** The first 10 minutes of talking are more valuable than the last 10 minutes of coding.

---

## 🗣️ Communication Framework (REACTO)

1. **R**epeat — Restate the problem in your own words.
2. **E**xamples — Walk through 2-3 examples (including edge cases).
3. **A**pproach — Describe your algorithm at a high level.
4. **C**ode — Implement it cleanly.
5. **T**est — Trace through your code with examples.
6. **O**ptimize — Discuss improvements and trade-offs.

---

## 🧠 Pattern Quick-Reference

Use the deep-dive INSIGHTS files to master specific domains:

| Domain | Quick Reference | Technical Deep Dive |
| :--- | :--- | :--- |
| **DSA Patterns** | Sliding Window, BFS/DFS, DP | [DSA Insights](./dsa/INSIGHTS.md) |
| **Design Patterns** | Creational, Structural, Behavioral | [Design Pattern Insights](./design_patterns/INSIGHTS.md) |
| **Machine Coding** | Entity separation, Concurrency | [Machine Coding Insights](./machine_coding/INSIGHTS.md) |
| **System Design** | Sharding, LSM Trees, CAP | [HLD Insights](./system_design_hld/INSIGHTS.md) |
| **Infrastructure** | Docker, Rate Limiting, Sockets | [Infra Insights](./infrastructure_challenges/INSIGHTS.md) |

---

## 🏗️ System Design Interview Framework (35–40 min)

System design interviews are notoriously challenging due to their unstructured nature. Candidates are asked to tackle open-ended problems that lack a single standard answer, typically within a strict **35–40 minute window**. Success relies heavily on a highly organized, structured approach.

| Step | Time | Goal |
| :--- | :--- | :--- |
| **1. Requirements** | 5 min | Clarify functional & non-functional reqs (scale, scope). |
| **2. API Interface** | 3 min | Define system contracts (REST/gRPC) & signatures. |
| **3. Estimation** | 3 min | Estimate QPS, storage (5yr), bandwidth. |
| **4. Data Model** | 5 min | Identify entities, schema, and SQL vs NoSQL. |
| **5. High-Level Design** | 5 min | Draw macro architecture (Client → LB → App → DB). |
| **6. Detailed Design** | 10 min | Deep dive: Partitioning, caching, hot users. |
| **7. Bottlenecks** | 5 min | Analyze SPOFs, replication, observability. |

### Step 1: Requirements Clarification
Because design questions are open-ended, the very first step must be to clarify ambiguities and define the exact scope.
- **Action**: Ask specific boundary questions.
- **Example**: If designing Twitter:
    - Are we building the frontend and backend?
    - Will tweets contain heavy media (photos/videos)?
    - Do we need to support push notifications or trending topics?

### Step 2: System Interface Definition
Define the exact APIs expected from the system to establish a contract.
- **Action**: Write out API signatures (e.g., `POST /tweet`, `GET /feed`).
- **Purpose**: Acts as a safety check to ensure you haven't misunderstood core requirements.

### Step 3: Back-of-the-Envelope Estimation
Estimate the scale to identify potential bottlenecks early.
- **Action**: Calculate:
    - Expected traffic (**QPS**)
    - Total storage required (over **5 years**)
    - Anticipated network bandwidth usage (**ingress/egress**)
- **Purpose**: Mathematically justify decisions regarding load balancing, caching, and sharding.

### Step 4: Defining Data Model
Identify the entities and how they interact.
- **Action**: Define the **schema**, **relationships**, and **data flow**.
- **Purpose**: Justify whether a **Relational (MySQL / ACID)** or **NoSQL (Cassandra / AP)** database best fits the read/write patterns.

### Step 5: High-Level Design (HLD)
Draw a block diagram with **5-6 core components**.
- **Flow**: `Client → Load Balancers → Application Servers → Databases / Caches → Blob Storage`
- **Purpose**: Establish macro-architecture before getting bogged down in details.

### Step 6: Detailed Design
Dig deeper into **2-3 specific components** based on interviewer feedback.
- **Key Discussions**:
    - **Partitioning**: How to split massive data (Sharding strategies).
    - **Hot Users**: Handling "celebrity" problems.
    - **Caching**: Eviction policies (LRU/LFU) to speed up reads.

### Step 7: Bottlenecks & Trade-offs
Analyze the design for breaking points.
- **Action**: Discuss:
    - **Single Points of Failure (SPOFs)**.
    - **Replication**: Strategies to survive server losses.
    - **Observability**: Logging, tracing, and metrics.

---

## 🎤 Behavioral Questions (STAR Method)

| Letter | Meaning | Example Prompt |
| :--- | :--- | :--- |
| **S**ituation | Set the scene | _"On my last project, we had a monolith serving 10K RPM..."_ |
| **T**ask | Your responsibility | _"I was tasked with breaking it into microservices..."_ |
| **A**ction | What you did | _"I designed the service boundaries using DDD, set up a CI/CD pipeline..."_ |
| **R**esult | Measurable outcome | _"Reduced deploy time from 2 hours to 15 minutes, cut P99 latency by 40%."_ |

### Common Behavioral Topics
- **Conflict resolution** — Disagreement with a teammate on architecture.
- **Failure & learning** — A production incident you caused and how you fixed it.
- **Leadership** — A time you mentored someone or drove a technical decision.
- **Ambiguity** — A project with unclear requirements and how you navigated it.

---

## 🚩 Red Flags to Avoid

| ❌ Don't | ✅ Do Instead |
| :--- | :--- |
| Jump straight into coding | Clarify, then discuss approach first |
| Stay silent while thinking | Think aloud — silence is the enemy |
| Write messy variable names (`a`, `b`, `x`) | Use descriptive names (`left_ptr`, `curr_sum`) |
| Ignore edge cases | Explicitly ask: empty input? single element? overflow? |
| Say "I don't know" and stop | Say "I haven't seen this, but here's how I'd reason about it..." |
| Over-optimize prematurely | Get a working solution first, then optimize |

---

## 📋 Pre-Interview Checklist

- [ ] Review the [Learning Path & Roadmap](./index.md) for architectural pillars.
- [ ] Skim the [Engineering Mastery Dashboard](./dashboard/engineering_metrics.md) for low-confidence topics.
- [ ] Re-solve 2-3 problems from the [Mastery Progress Tracker](./todo.md).
- [ ] Review the relevant INSIGHTS file for the specific interview type.
- [ ] Prepare 3 STAR-method stories for behavioral alignment.
