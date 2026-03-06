# HLD: Design a Global Instant Messenger (WhatsApp Lite)

## 🚀 Problem Statement
Design a real-time messaging system that supports millions of users, global message delivery, and persistent chat history.

## 🛠️ Functional Requirements
1. **One-to-One Chat:** Instant delivery (< 200ms).
2. **Last Seen / Presence:** Real-time online/offline status.
3. **Sent/Delivered/Read Receipts:** Reliable state tracking.
4. **Group Chats:** Scaling to 500+ users per group.

## 📈 Non-Functional Requirements
1. **Low Latency:** Crucial for user experience.
2. **High Availability:** System must never go down.
3. **Consistency:** Messages must arrive in the correct order.

## 🧠 Key Design Challenges (5YOE Focus)
- **Websocket vs Polling:** Which one and why? How to handle 10 million concurrent connections?
- **Data Partitioning:** How do you shard chat history? By `user_id` or `chat_id`?
- **Global Routing:** How does a user in NYC send a message to a user in Tokyo with minimal lag?
