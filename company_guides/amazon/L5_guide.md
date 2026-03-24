# 🏢 Company Guide Template (FAANG+ / Tier-1 Optimized)

## 📝 Overview

**Company:** Amazon
**Role / Level:** Software Engineer / L5 (SDE II)
**Track:** General Software Engineering
**YOE Expected:** Mid-Level (Expected to handle both coding and design competently, unlike L4)
**Hiring Bar:** High (Enforced heavily by the dedicated Bar Raiser round)
**Process Duration:** 4–8 weeks

**Key Insight (TL;DR):**

> *To crack Amazon L5, you must balance writing clean, bug-free code in a plain-text environment without execution tools, while seamlessly weaving deeply detailed, metric-driven Leadership Principle (LP) stories into every single round.*

---

## 🔄 Interview Process Breakdown

**Typical Flow:**

1. Recruiter Screen (30 minutes; background, LP check, and timeline)
2. Online Assessment (2 hours; 90 min coding + Work Simulation evaluating LPs)
3. Technical Phone Screen (45 minutes; 1-2 coding problems + LP questions)
4. Onsite Loop (Virtual, 5 rounds):
   * Coding x 2 (60 minutes each; 20-30 min behavioral + 35-40 min coding)
   * System Design (60 minutes; High-Level Design)
   * Low-Level Design (LLD) OR Extra Coding (60 minutes; based on team needs)
   * Bar Raiser (60 minutes; pure behavioral and LP deep-dive)

---

### 🧪 Online Assessment (if applicable)

**Format:**

* 2 coding problems in ~90 minutes (HackerRank), followed by a Work Simulation and Work Style assessment.

**What They Test:**

* Algorithmic thinking and the ability to implement clean solutions under time pressure.
* Situational judgment and alignment with Amazon's core values, specifically customer-centricity, ownership, and bias for action.

**Key Strategy:**

* Focus on getting a working solution rather than spending too long perfecting the first problem and running out of time for the second.
* For the behavioral portion, answer authentically but keep Amazon's Leadership Principles front of mind.

📌 Example insight:

* Problems are medium-difficulty (occasionally hard) and unproctored, meaning no hints or clarifications from an interviewer.

---

### 💻 Coding Rounds

**Format:**

* # Questions: 1-2 problems per round.
* Time: 45 mins (Phone Screen), 60 mins (Onsite) — though Onsite includes 20-30 minutes of behavioral questions first.
* Difficulty: Medium (Phone Screen) to Medium-Hard (Onsite).

**Common Topics:**

* Arrays, Strings, Graphs, Dynamic Programming, and Tree Traversals.

**Company-Specific Style:**

* Amazon emphasizes "method and basics" over perfect LeetCode memorization, looking at your systematic problem-solving approach.
* You must code in a shared text editor (Amazon Livecode) with syntax highlighting but *no autocomplete or code execution capabilities*.
* Mental debugging is critical; you must trace through your solution with test cases manually.

📌 Example insight (Amazon-style):

* Amazon expects working, syntactically correct code that handles edge cases robustly, but interviewers will actively provide hints. How you receive and incorporate their feedback is a huge part of the evaluation.

---

### 🏗️ System Design / LLD

**Rounds:**

* ☑ LLD (Depending on team preference, you may get LLD instead of a third coding round)
* ☑ HLD (System Design is standard for all L5 loops)
* ☐ Product Design

**Focus Areas:**

* **HLD:** Breaking down complex problems, API contracts, data models, scalability, and service communication.
* **LLD:** Object-oriented modeling, applying SOLID principles, identifying entities/relationships, and choosing appropriate design patterns.

**Company Flavor:**

| Company Type | What They Emphasize |
| :--- | :--- |
| Amazon (HLD) | Practical solutions that can be built and maintained by real teams; trade-off analysis over theoretical perfection. |
| Amazon (LLD) | Extensibility, clear class responsibilities, and avoiding over-engineering; UML is not strictly required, but clean relationships are. |

📌 Example insight:

* In System Design, always start by clarifying expected traffic, data size, and consistency requirements before drawing components. In LLD, focus on class definitions and relationships rather than writing out method implementations.

---

### 🗣️ Behavioral Round

**Weightage:** निर्णायक (Decisive/Critical) - The Bar Raiser round can single-handedly veto your hire regardless of technical performance.

**What They Evaluate:**

* Leadership Principle Alignment: Deep, authentic demonstration of ownership, customer obsession, delivering results, etc.
* Overall Hiring Bar: Whether you raise the talent standard across the company.
* Adaptability: How you respond to intense follow-up probing ("What other options did you consider?", "What was the outcome six months later?").

📌 Example insight:

* The Bar Raiser round is 60 minutes of pure behavioral drilling, and interviewers are trained to spot inconsistencies and embellishments.

**Preparation:**

* Prepare at least 2 stories per Leadership Principle (aim for ~10 versatile stories total).
* Structure stories with four elements: Proactive/Reactive, Data-Driven, Impact-Oriented (metrics/percentages), and Influence.
* Do not lie or inflate your individual contributions; Bar Raisers will catch it immediately.

---

## 🎯 Evaluation Criteria

### Core Dimensions

| Dimension | What It Means |
| :--- | :--- |
| Problem Solving | Breaking down problems logically and choosing appropriate data structures without dead-ending. |
| Code Quality | Writing complete, syntactically correct code without relying on execution tools. |
| System Thinking | Scalability, trade-offs, and practical component architecture for real-world scenarios. |
| Communication | Thinking out loud, clearly explaining approaches, and taking hints gracefully. |
| Leadership Principles | Concrete, data-driven examples demonstrating Amazon's core values in real workplace scenarios. |

---

## 🧠 Company-Specific Signals

### 🔍 What Gets You Hired

* Consistently mapping technical decisions and past experiences to specific Leadership Principles.
* Transitioning smoothly from intense behavioral storytelling directly into complex algorithmic problem-solving.
* Starting with basic technical approaches and collaboratively building complexity while remaining receptive to interviewer guidance.

### 🚫 What Gets You Rejected

* Faking or exaggerating your role in behavioral stories; Bar Raisers are trained to tear apart inconsistencies.
* Jumping straight into coding or system design without clarifying requirements, constraints, and edge cases.
* Failing to verbally communicate your thought process, especially in a plain-text coding environment.

---

## 🧠 Level Expectations

| Level | Expectation |
| :--- | :--- |
| Mid (L5 / SDE II) | Solid coding proficiency + independent architectural thinking (HLD/LLD) + proven behavioral depth reflecting ownership and impact. |

📌 Example:

* Unlike L4s, L5 candidates must demonstrate the ability to handle system design independently without heavy guidance, showing solid fundamentals in caching, database choices, and scale.

---

## 🧩 Question Bank (Company-Specific)

### Coding

* Arrays, Strings, Graphs, Dynamic Programming. (Expect non-standard variations rather than pure LeetCode memorization).

### LLD

* "Design a parking lot management system".
* "Design a chess game".
* "Design a library management system".

### HLD

* "Design a URL shortener like bit.ly".
* "Design a chat service for millions of users".

### Behavioral

* "Tell me about a time you had to make a decision with incomplete information".
* "Describe a situation where you had to work with a challenging team member".
* "Tell me about a time you had to make a difficult decision".

---

## 🏗️ Design Expectations Deep Dive

### LLD Expectations

* Clean class design with appropriate use of Strategy, Factory, or Observer patterns (only when they actually make sense).
* Adaptable structures that handle future changes (e.g., adding motorcycle parking or surge pricing) without massive refactoring.
* Focus on class definitions and relationships, not writing method implementation code.

### HLD Expectations

* Start broad (clarifying traffic, data size, geography) before diving deep into specific components.
* Focus on practical APIs, data models, and service communication.
* Strong emphasis on scalability and clearly justifying trade-offs for database choices and caching.

---

## ⚖️ Trade-offs & Thinking Style

**What They Expect You to Do:**

* Explain design choices while considering alternative approaches and their long-term implications.
* Build ground up: start from a simple, functioning solution and scale to optimal.
* Maintain a collaborative approach; use the whiteboard/editor as a communication tool.

**Common Prompts:**

* "How would you modify it for different constraints?"
* "How would you handle increased load or failures?"
* "What other options did you consider? What was the ultimate outcome?"

---

## 👃 Common Pitfalls

* Getting stuck polishing code for the first OA problem and running out of time for the second.
* Over-engineering system designs instead of providing practical, maintainable solutions.
* Failing to accurately track which Leadership Principles you've already covered across the 5 rounds, leading to story repetition.
* Relying on an IDE's autocomplete/execution environment during prep, leading to freezing in the Amazon Livecode plain-text environment.

---

## ⚙️ Preparation Strategy (Company-Tailored)

### Phase 1: Foundations

* Practice algorithmic coding out loud in a plain-text editor without running the code.
* Review Amazon's 16 Leadership Principles and map out 2 stories per principle.

### Phase 2: Targeted Prep

* Use the STAR framework combined with data, impact, and influence metrics for every behavioral answer.
* Study system design fundamentals (e.g., Martin Kleppmann's DDIA book) and practice scoping ambiguous problems.

### Phase 3: Mocking

* Conduct timed mock interviews mimicking the 20-minute behavioral + 40-minute technical pacing.
* Practice the mental transition from intense behavioral storytelling directly into algorithmic coding.

---

## 📊 Difficulty & Bar

| Area | Difficulty |
| :--- | :--- |
| Coding | ☐ Easy ☑ Medium ☑ Hard |
| Design | ☐ Low ☑ Medium ☑ High |
| Behavioral | ☐ Low ☐ Medium ☑ High (Bar Raiser) |
