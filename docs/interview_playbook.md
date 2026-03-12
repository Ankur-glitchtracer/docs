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

Use the INSIGHTS files as deep-dives for each domain:

| Domain | Quick Reference | Deep Dive |
| :--- | :--- | :--- |
| **DSA Patterns** | Sliding Window, Two Pointers, BFS/DFS, DP | [DSA Insights](./dsa/INSIGHTS.md) |
| **Design Patterns** | Creational, Structural, Behavioral (GoF) | [Design Pattern Insights](./design_patterns/INSIGHTS.md) |
| **Machine Coding** | Entity separation, State machines, Concurrency | [Machine Coding Insights](./machine_coding/INSIGHTS.md) |
| **System Design** | Sharding, Pub/Sub, LSM Trees, CAP | [HLD Insights](./system_design_hld/INSIGHTS.md) |
| **Infrastructure** | Docker, Rate Limiting, Sockets, Heartbeats | [Infra Insights](./infrastructure_challenges/INSIGHTS.md) |

---

## 🏗️ System Design Interview Framework (30-40 min)

| Phase | Time | What To Do |
| :--- | :--- | :--- |
| **1. Requirements** | 5 min | Functional vs. Non-functional. _"How many users? Read-heavy or write-heavy?"_ |
| **2. Estimation** | 3 min | Back-of-the-envelope: QPS, storage, bandwidth. |
| **3. High-Level Design** | 10 min | Draw the major components (API Gateway, DB, Cache, Queue). |
| **4. Deep Dive** | 10 min | Interviewer picks 1-2 components. Go deep: schema, API contracts, failure modes. |
| **5. Trade-offs** | 5 min | Discuss CAP, consistency vs. availability, scaling bottlenecks. |

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

- [ ] Review the [DSA Roadmap](./dsa/ROADMAP.md) for topic dependencies
- [ ] Skim the [Engineering Dashboard](./docs_portal.md) for low-confidence topics
- [ ] Re-solve 2-3 problems from the [TODO list](./todo.md) marked as low confidence
- [ ] Review the relevant INSIGHTS file for the interview type
- [ ] Practice explaining one problem using the REACTO method aloud
- [ ] Prepare 3 STAR stories for behavioral questions
