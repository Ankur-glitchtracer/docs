# 🎯 Interview Playbook

Your battle-tested strategy guide for technical interviews. Use this as a pre-interview warm-up and a reference for structuring your answers.

-----

## ⏱️ The 45-Minute Framework

| Phase | Time | What To Do |
| :--- | :--- | :--- |
| **1. Clarify** | 3-5 min | Repeat the problem. Ask about edge cases, input size, constraints. *"Can the input be empty? Is it sorted?"* |
| **2. Approach** | 5-7 min | Talk through 1-2 approaches (brute force → optimized). State time/space complexity for each. Get interviewer buy-in before coding. |
| **3. Code** | 15-20 min | Write clean, modular code. Use helper functions. Name variables clearly. Narrate as you go. |
| **4. Test** | 5-7 min | Trace through with a simple example, then edge cases. Fix bugs aloud. |
| **5. Optimize** | 5-10 min | Discuss trade-offs, alternative approaches. Can you improve space? Parallelize? |

!!! tip "Golden Rule"
    **Never jump to code.** The first 10 minutes of talking are more valuable than the last 10 minutes of coding.

-----

## 🗣️ Communication Framework (REACTO)

1.  **R**epeat — Restate the problem in your own words.
2.  **E**xamples — Walk through 2-3 examples (including edge cases).
3.  **A**pproach — Describe your algorithm at a high level.
4.  **C**ode — Implement it cleanly.
5.  **T**est — Trace through your code with examples.
6.  **O**ptimize — Discuss improvements and trade-offs.

-----

## 🧠 Pattern Quick-Reference

Use the deep-dive INSIGHTS files to master specific domains:

| Domain | Quick Reference | Technical Deep Dive |
| :--- | :--- | :--- |
| **DSA Patterns** | Sliding Window, BFS/DFS, DP | [DSA Insights](https://www.google.com/search?q=./dsa/INSIGHTS.md) |
| **Design Patterns** | Creational, Structural, Behavioral | [Design Pattern Insights](https://www.google.com/search?q=./design_patterns/INSIGHTS.md) |
| **Machine Coding** | Entity separation, Concurrency | [Machine Coding Insights](https://www.google.com/search?q=./machine_coding/INSIGHTS.md) |
| **System Design** | Sharding, LSM Trees, CAP | [HLD Insights](https://www.google.com/search?q=./system_design_hld/INSIGHTS.md) |
| **Infrastructure** | Docker, Rate Limiting, Sockets | [Infra Insights](https://www.google.com/search?q=./infrastructure_challenges/INSIGHTS.md) |

-----

## 🏗️ System Design Interview Framework (35–40 min)

System design interviews are notoriously challenging due to their unstructured nature. Candidates are asked to tackle open-ended problems that lack a single standard answer, typically within a strict **35–40 minute window**. The system design interview is an **open-ended conversation**, and **you are expected to lead it**. Success relies heavily on a highly organized, structured approach.

| Step | Time | Goal |
| :--- | :--- | :--- |
| **1. Requirements** | 5 min | Clarify functional & non-functional reqs, scope, and use cases. |
| **2. API Interface** | 3 min | Define system contracts (REST/gRPC) & signatures. |
| **3. Estimation** | 3 min | Estimate QPS, storage (5yr), and bandwidth using basic math. |
| **4. Data Model** | 5 min | Identify entities, schema, and SQL vs NoSQL. |
| **5. High-Level Design** | 5 min | Draw macro architecture (Client → LB → App → DB). |
| **6. Detailed Design** | 10 min | Deep dive: Partitioning, caching, hot users, component design. |
| **7. Bottlenecks** | 5 min | Analyze SPOFs, scaling needs, and trade-offs. |

### Step 1: Requirements Clarification

Because design questions are open-ended, the very first step must be to gather requirements and strictly scope the problem.

  - **Action**: Discuss assumptions and ask boundary questions to clarify use cases and constraints:
      - Who is going to use it?
      - How are they going to use it?
      - How many users are there?
      - What exactly does the system do?
      - What are the specific inputs and outputs of the system?
      - How much data do we expect to handle?
      - How many requests per second (RPS/QPS) do we expect?
      - What is the expected read-to-write ratio?
  - **Example**: If designing Twitter, ask if we need to support push notifications, trending topics, or heavy media (photos/videos).

### Step 2: System Interface Definition

Define the exact APIs expected from the system to establish a contract.

  - **Action**: Write out API signatures (e.g., `POST /tweet`, `GET /feed`).
  - **Purpose**: Acts as a safety check to ensure you haven't misunderstood core requirements.

### Step 3: Back-of-the-Envelope Estimation

Estimate the scale to identify potential bottlenecks early. You will likely be asked to do these estimates by hand.

  - **Action**: Calculate:
      - Expected traffic (**QPS/RPS**)
      - Total storage required (over **5 years**)
      - Anticipated network bandwidth usage (**ingress/egress**)
  - **Primer Tips**: Memorize the **Powers of Two table** and **Latency numbers every programmer should know** (e.g., memory vs. disk reads) to perform and justify these calculations quickly.
  - **Purpose**: Mathematically justify decisions regarding load balancing, caching, and sharding.

### Step 4: Defining Data Model

Identify the entities and how they interact.

  - **Action**: Define the **schema**, **relationships**, and **data flow**.
  - **Purpose**: Justify whether a **Relational (MySQL / ACID)** or **NoSQL (Cassandra / AP)** database best fits the read/write patterns.

### Step 5: High-Level Design (HLD)

Draw a block diagram with **5-6 core components**.

  - **Flow**: `Client → Load Balancers → Application Servers → Databases / Caches → Blob Storage`
  - **Purpose**: Sketch the main components and connections, justifying your initial ideas before getting bogged down in details.

### Step 6: Detailed Design

Dig deeper into **2-3 specific components** based on interviewer feedback.

  - **Key Discussions**:
      - **Component Internals**: E.g., for a URL shortener, diving into MD5 vs Base62 hash collisions.
      - **Partitioning**: How to split massive data (Database Sharding strategies).
      - **Hot Users**: Handling "celebrity" problems or unevenly distributed traffic.

### Step 7: Bottlenecks, Scaling & Trade-offs

Identify and address bottlenecks given the constraints from Step 1 and Step 3.

  - **Action**: Discuss potential solutions and trade-offs. **Remember: Everything is a trade-off.**
  - **Evaluate your need for**:
      - **Load Balancers**: Distributing heavy ingress traffic.
      - **Horizontal Scaling**: Adding more stateless application servers.
      - **Caching**: Implementing memory caches (Redis/Memcached) for read-heavy flows.
      - **Database Sharding/Replication**: Scaling the persistence layer to handle massive data volumes or write-heavy operations.
      - **Single Points of Failure (SPOFs)**: Surviving server losses.
      - **Observability**: Logging, tracing, and metrics.

-----

## 🎤 Behavioral Questions (STAR Method)

| Letter | Meaning | Example Prompt |
| :--- | :--- | :--- |
| **S**ituation | Set the scene | *"On my last project, we had a monolith serving 10K RPM..."* |
| **T**ask | Your responsibility | *"I was tasked with breaking it into microservices..."* |
| **A**ction | What you did | *"I designed the service boundaries using DDD, set up a CI/CD pipeline..."* |
| **R**esult | Measurable outcome | *"Reduced deploy time from 2 hours to 15 minutes, cut P99 latency by 40%."* |

### Common Behavioral Topics

  - **Conflict resolution** — Disagreement with a teammate on architecture.
  - **Failure & learning** — A production incident you caused and how you fixed it.
  - **Leadership** — A time you mentored someone or drove a technical decision.
  - **Ambiguity** — A project with unclear requirements and how you navigated it.

-----

## 🚩 Red Flags to Avoid

| ❌ Don't | ✅ Do Instead |
| :--- | :--- |
| Jump straight into coding | Clarify, then discuss approach first |
| Stay silent while thinking | Think aloud — silence is the enemy |
| Write messy variable names (`a`, `b`, `x`) | Use descriptive names (`left_ptr`, `curr_sum`) |
| Ignore edge cases | Explicitly ask: empty input? single element? overflow? |
| Say "I don't know" and stop | Say "I haven't seen this, but here's how I'd reason about it..." |
| Over-optimize prematurely | Get a working solution first, then optimize |

-----

## 📋 Pre-Interview Checklist

  - [ ] Review the [Learning Path & Roadmap](https://www.google.com/search?q=./index.md) for architectural pillars.
  - [ ] Skim the [Engineering Mastery Dashboard](https://www.google.com/search?q=./dashboard/engineering_metrics.md) for low-confidence topics.
  - [ ] Re-solve 2-3 problems from the [Mastery Progress Tracker](https://www.google.com/search?q=./todo.md).
  - [ ] Review the relevant INSIGHTS file for the specific interview type.
  - [ ] Prepare 3 STAR-method stories for behavioral alignment.


## 🧮 Appendix: Estimation Cheat Sheet

Use the following reference tables during **Step 3: Back-of-the-envelope estimation** to quickly calculate storage requirements, network bandwidth, and system latencies without relying on a calculator.

### Powers of Two Table

| Power | Exact Value | Approx Value | Bytes |
| :--- | :--- | :--- | :--- |
| **7** | 128 | - | - |
| **8** | 256 | - | - |
| **10** | 1,024 | 1 thousand | 1 KB |
| **16** | 65,536 | - | 64 KB |
| **20** | 1,048,576 | 1 million | 1 MB |
| **30** | 1,073,741,824 | 1 billion | 1 GB |
| **32** | 4,294,967,296 | - | 4 GB |
| **40** | 1,099,511,627,776 | 1 trillion | 1 TB |

### Latency Comparison Numbers

| Operation | Time (ns) | Time (μs / ms) | Notes |
| :--- | :--- | :--- | :--- |
| **L1 cache reference** | 0.5 ns | | |
| **Branch mispredict** | 5 ns | | |
| **L2 cache reference** | 7 ns | | 14x L1 cache |
| **Mutex lock/unlock** | 25 ns | | |
| **Main memory reference** | 100 ns | | 20x L2 cache, 200x L1 cache |
| **Compress 1K bytes with Zippy** | 10,000 ns | 10 μs | |
| **Send 1 KB bytes over 1 Gbps network** | 10,000 ns | 10 μs | |
| **Read 4 KB randomly from SSD** | 150,000 ns | 150 μs | ~1 GB/sec SSD |
| **Read 1 MB sequentially from memory** | 250,000 ns | 250 μs | |
| **Round trip within same datacenter** | 500,000 ns | 500 μs | |
| **Read 1 MB sequentially from SSD** | 1,000,000 ns | 1 ms | ~1 GB/sec SSD, 4x memory |
| **HDD seek** | 10,000,000 ns | 10 ms | 20x datacenter roundtrip |
| **Read 1 MB sequentially from 1 Gbps** | 10,000,000 ns | 10 ms | 40x memory, 10x SSD |
| **Read 1 MB sequentially from HDD** | 30,000,000 ns | 30 ms | 120x memory, 30x SSD |
| **Send packet CA -> Netherlands -> CA** | 150,000,000 ns | 150 ms | |

!!! info "Handy Metrics & Conversions"
    **Time Conversions:**
    
    * 1 ns = $10^{-9}$ seconds
    * 1 μs = $10^{-6}$ seconds = 1,000 ns
    * 1 ms = $10^{-3}$ seconds = 1,000 μs = 1,000,000 ns
    
    **Throughput & Network Capabilities:**
    
    * **HDD Sequential Read:** ~30 MB/s
    * **1 Gbps Ethernet Sequential Read:** ~100 MB/s
    * **SSD Sequential Read:** ~1 GB/s
    * **Main Memory Sequential Read:** ~4 GB/s
    * **Datacenter Network:** ~2,000 round trips per second
    * **Global Network:** ~6-7 world-wide round trips per second
