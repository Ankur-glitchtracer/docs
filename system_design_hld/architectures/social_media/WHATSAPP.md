# 💬 System Design: Global Instant Messenger (WhatsApp Lite)

## 📝 Overview
A **Real-Time Messaging Platform** designed for instantaneous communication across millions of concurrent users. It prioritizes low-latency message delivery, real-time presence tracking, and reliable message ordering in a globally distributed environment.

!!! abstract "Core Concepts"

    - **WebSockets:** Maintaining persistent, bi-directional connections to enable real-time server-side pushes.
    - **Presence Tracking:** Using high-performance TTL-based stores (Redis) to monitor user online/offline status at scale.
    - **Fan-out Architecture:** Efficiently distributing messages to multiple recipients in large group chats using Pub/Sub models.

## 🛠️ Functional & Non-Functional Requirements
### Functional Requirements

1. **One-to-One Chat:** Instant message delivery with sub-200ms latency.
2. **Presence Management:** Real-time "Last Seen" and online/offline status updates.
3. **Message Reliability:** Support for Sent, Delivered, and Read receipts.
4. **Group Chats:** Scaling message delivery to groups with hundreds or thousands of members.

### Non-Functional Requirements

1. **Low Latency:** Ensuring a seamless, real-time conversational experience.
2. **High Availability:** 99.99% uptime; messaging is a critical utility for users.
3. **Message Ordering:** Guaranteeing that messages arrive and are displayed in the correct chronological order.

## 🧠 The Engineering Story

**The Villain:** "The Polling Storm." 100M users asking the server "Got any new messages?" every 5 seconds. The API Gateway melts under the weight of 20M requests/sec.

**The Hero:** "The Persistent WebSocket." A bi-directional pipe that lets the server *push* messages to the user the instant they arrive.

**The Plot:**

1. **Gateway:** Maintain 10M+ open TCP connections using a non-blocking I/O model (like Netty or Go routines).
2. **Presence:** Use a TTL-based KV store (Redis) to track who is online.
3. **Message Store:** Use a NoSQL DB (Cassandra) optimized for heavy writes and chronological retrieval.
4. **Group Chat:** Use a Pub/Sub model to fan-out messages to multiple recipients.

**The Twist (Failure):** **The Fan-out Explosion.** Sending a message to a group with 5,000 members during a global event like the World Cup.

**Interview Signal:** Mastery of **Real-time Networking**, **State Management (Presence)**, and **Write-Heavy DB Design**.

## 🏗️ High-Level Architecture
Design a real-time messaging system that supports millions of users, global message delivery, and persistent chat history.

### Key Design Challenges:

- **WebSocket vs Polling:** Choosing the right protocol to handle 10 million concurrent connections efficiently.
- **Data Partitioning:** Sharding chat history by `chat_id` or `user_id` to balance load and query performance.
- **Global Routing:** Minimizing cross-region latency when routing messages between users in different parts of the world.

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

## Practical Implementation

Explore the real-time networking and data modeling of global messaging platforms:

* [System Design: Facebook Capacity](./FACEBOOK_CAPACITY.md)
* [Machine Coding: Kafka Lite](../distributed_storage/KAFKA_DEEP_DIVE.md)
* [Infrastructure: Socket Chat App](../../../infrastructure_challenges/socket_chat_app/PROBLEM.md)
