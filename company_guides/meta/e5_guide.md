# 🏢 Company Guide Template (FAANG+ / Tier-1 Optimized)

## 📝 Overview

**Company:** Meta
**Role / Level:** Software Engineer / E5 (Senior)
**Track:** Software Engineer, Product (Fullstack) / Software Engineer, Infrastructure (Backend)
**YOE Expected:** 5+ years (Senior)
**Hiring Bar:** Extremely High (Behavioral and Design rounds dictate the level and can easily result in down-leveling)

**Process Duration:** 3 to 4 weeks (Team matching occurs after passing the loop)

**Key Insight (TL;DR):**

> *To crack Meta E5, you must prioritize speed and problem-solving agility over perfect implementations in coding, while demonstrating extreme depth in System Design and measurable, individual ownership in Behavioral rounds to avoid getting down-leveled.*

---

## 🔄 Interview Process Breakdown

**Typical Flow:**

1. Online Assessment (OA)
2. Technical Phone Screen (Coding)
3. Onsite Loop (4 rounds):
   * Traditional Coding (1 round)
   * AI-Enabled Coding (1 round)
   * System Design OR Product Architecture (1 round)
   * Behavioral (1 round)

---

### 🧪 Online Assessment (if applicable)

**Format:**

* 90 minutes via CodeSignal, with full video and microphone monitoring.
* A single complex problem divided into 4 progressive stages (e.g., in-memory DB or cloud file storage).

**What They Test:**

* Stage 1: Basic core features and corner cases.
* Stage 2: Additional constraints (e.g., TTL expiration).
* Stage 3: Advanced capabilities (e.g., point-in-time queries).
* Stage 4: Performance-intensive operations (e.g., concurrency handling).

**Key Strategy:**

* Focus on correctness first; minor inefficiencies are acceptable.
* Do not panic if you don't finish Stage 4, as most candidates do not complete all stages within the time limit.

📌 Example insight (Meta-style):

* Problems focus on practical system implementation (designing working systems with multiple components) rather than traditional algorithmic puzzles.

---

### 💻 Coding Rounds

**Format:**

* # Questions: Typically 2 medium-to-hard LeetCode problems per round.
* Time: 45 minutes.
* Difficulty: Medium to Hard (Hards are becoming increasingly common).

**Common Topics:**

* Arrays, strings, linked lists, binary trees, graphs, sorting, and searching.
* Pure Dynamic Programming (DP) is officially discouraged, but recursion + memoization or combinatorial problems still appear.

**Company-Specific Style:**

* **No code execution:** You will use CoderPad without the ability to run or execute your code.
* Speed and agility: Meta values quick, working solutions that you can iterate on over perfectly polished code on the first try.
* Manual verification: You must test your code line-by-line and check corner cases yourself.

📌 Example insight:

* Meta interviewers prioritize getting to a working solution quickly; a brute-force solution that you can explain how to optimize is better than an unfinished optimal one.

---

### 🏗️ System Design / LLD

**Rounds:**

* ☐ LLD
* ☑ HLD (System Design for Infrastructure roles)
* ☑ Product Design (Product Architecture for Product roles)

**Focus Areas:**

* **System Design:** Backend architecture, distributed caches, rate limiters, database sharding, and deep scalability challenges.
* **Product Architecture:** API design, user experience flows, data modeling, client-server interactions (e.g., designing Instagram or News Feed).

**Company Flavor:**

| Company Type | What They Emphasize                |
| ------------ | ---------------------------------- |
| Meta         | Concrete scaling numbers, specific throughput calculations, and aggressive cache invalidation strategies. |

📌 Example insight:

* Meta interviewers will constantly challenge your design: "But what if you have 100x more users?" Be prepared to redesign your sharding strategy on the fly.

---

### 🗣️ Behavioral Round

**Weightage:** निर्णायक (Decisive/Critical) - This round heavily dictates your final level and can result in an E4 down-level.

**What They Evaluate (5 Core Competencies):**

* Resolving Conflicts
* Driving Results
* Embracing Ambiguity
* Growing Continuously
* Communicating Effectively

📌 Example insight:

* The interviewer (often the loop lead) will spend 45 minutes on just two stories to uncover exactly what *you* personally did, not what your team accomplished.

**Preparation:**

* Have 8-10 polished stories ready (2 per core competency).
* Focus heavily on quantified impact (e.g., "I reduced latency by 200ms for 50M daily users").
* Highlight cross-functional collaboration and navigating ambiguous situations.

---

## 🎯 Evaluation Criteria

### Core Dimensions

| Dimension       | What It Means                            |
| --------------- | ---------------------------------------- |
| Problem Solving | Breaking down complex problems logically and critically to arrive at effective solutions. |
| Code Quality    | Writing clean, maintainable code while demonstrating deep understanding of algorithms and data structures. |
| Verification    | Writing comprehensive tests and manually walking through code to ensure functionality and reliability. |
| Communication   | Clearly articulating thought processes, design decisions, and collaborating effectively. |

📌 These dimensions are explicitly evaluated in top companies.

---

## 🧠 Company-Specific Signals

### 🔍 What Gets You Hired

* Memorizing realistic numbers (database read/write speeds, cache latencies, network bandwidth) to make logical capacity estimates.
* Producing quick, working code and adapting well to hints ("What if the input is huge?").
* Having strong, metric-driven opinions on trade-offs (e.g., "Why Redis over Memcached?").

### 🚫 What Gets You Rejected

* Coding in silence. Explaining what you are considering is mandatory, even when stuck.
* Spending too long optimizing the first coding solution instead of finishing both problems.
* Sharing behavioral stories where you were just a contributor rather than leading without authority.

---

## 🧠 Level Expectations

| Level             | Expectation                            |
| ----------------- | -------------------------------------- |
| Senior (E5)       | Ownership of projects impacting entire teams (3+ people), proactive initiatives driven from conception to completion, and leading without authority. |

📌 Example:

* E5 candidates must proactively anticipate challenges, suggest solutions to resolve them, and independently drive the system design discussion.

---

## 🧩 Question Bank (Company-Specific)

### Coding

* Practice "Meta-tagged" questions heavily. Meta has a predictable pool of questions and prioritizes arrays, strings, linked lists, trees, graphs, and sorting.

### HLD (System Design / Product Architecture)

* Ticketmaster, Uber, Instagram, Facebook News Feed.

### Behavioral

* Deep probes into conflict resolution and project ownership ("Tell me exactly what you personally did to resolve this cross-team blocker").

---

## 🏗️ Design Expectations Deep Dive

### HLD Expectations

* Use Excalidraw effectively (practice beforehand).
* Know your napkin math. Meta expects you to design with actual throughput, bandwidth, and latency numbers in mind.
* Be prepared for intense follow-ups challenging every decision you make (e.g., redesigning your database strategy for massive scale multipliers).

---

## ⚖️ Trade-offs & Thinking Style

**What They Expect You to Do:**

* Vocalize your thought process constantly.
* Provide concrete reasoning based on experience, not just textbook knowledge, when choosing technologies.
* Trace through your logic verbally mid-interview ("What happens when we run this with input X?").

**Common Prompts:**

* "But what if you have 100x more users?"
* "Why REST over GraphQL?"
* "How would this behave in X scenario?"

---

## 👃 Common Pitfalls

* Trying to write perfectly optimized code on the first pass and running out of time for the second question.
* Giving "we" answers in the behavioral round instead of "I" answers (failing to highlight individual impact).
* Freezing up because you cannot run or execute your code in CoderPad.

---

## ⚙️ Preparation Strategy (Company-Tailored)

### Phase 1: Foundations

* Drill Meta-tagged LeetCode problems strictly.
* Practice coding in plain text editors to simulate the CoderPad environment without syntax checking or execution.

### Phase 2: Targeted Prep

* Build 8-10 behavioral stories using the STAR method, focusing heavily on specific numbers, metrics, and cross-team influence.
* Memorize realistic system design numbers (latencies, speeds) for capacity planning.

### Phase 3: Mocking

* Conduct mock interviews focusing on mental code tracing and verification.
* Do guided system design practice on Excalidraw to get comfortable with the back-and-forth, challenging nature of Meta interviews.

---

## 📊 Difficulty & Bar

| Area       | Difficulty             |
| ---------- | ---------------------- |
| Coding     | ☐ Easy ☐ Medium ☑ Hard |
| Design     | ☐ Low ☐ Medium ☑ High  |
| Behavioral | ☐ Low ☐ Medium ☑ High  |

---

## 🧾 Personalization Section

## **My Strengths:**

## **My Weaknesses:**

## **Focus Areas Before Interview:**

---

## 🚀 Final Revision Checklist

* ☐ 50–100 Meta-tagged DSA problems practiced without an IDE
* ☐ 8-10 behavioral stories mapped to the 5 core competencies with quantified metrics
* ☐ Realistic scaling numbers memorized for System Design
* ☐ Excalidraw practice completed for architectural diagramming
