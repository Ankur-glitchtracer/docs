# 🏗️ Machine Coding & System Design Insights

## 🟢 Game Systems (Snake & Ladder)

**The Villain:** "The God Class." Putting board logic, player logic, and dice logic into one giant file.

**The Hero:** "The Entity-Component Separation."

**The Plot:**

1. `Board` handles layout and jumps (Snakes/Ladders).
2. `Game` manages turns and win conditions.
3. `Dice` is a standalone utility.

**The Twist:** "The Infinite Loop." A snake leading to a ladder that leads back to the same snake.

## 🟡 Concurrency (Elevator System)

**The Villain:** "The Race Condition." Two people on different floors calling the same elevator, causing it to jitter.

**The Hero:** "The Request Queue & State Machine."

**The Plot:**

1. Collect all requests in a thread-safe queue.
2. Use a `Strategy` to decide which floor to visit next (SCAN algorithm).

**The Twist:** "The Starvation." The elevator keeps serving middle floors, leaving the top floor waiting forever.

## 🔴 Distributed Systems (Job Scheduler)

**The Villain:** "The Double Execution." Two workers picking up the same job from the DB simultaneously.

**The Hero:** "The Distributed Lock" (Redis/Zookeeper).

**The Plot:**

1. Use `SETNX` to claim a job ID.
2. Heartbeat to ensure the worker hasn't died.

**The Twist:** "The Zombie Job." A worker crashes without releasing the lock, blocking the job until it expires.
