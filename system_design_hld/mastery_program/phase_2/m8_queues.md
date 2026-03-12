# Module 8: Message Queues & Event Streaming

### 🚀 Problem Statement
When a document is uploaded, the system must:

1. Extract text
2. Chunk the document
3. Generate embeddings
4. Store in vector DB
5. Notify reviewers
6. Update the search index

Performing all six steps synchronously might take 45 seconds, during which the user may see a loading spinner.

### 🧠 The Engineering Story

**The Villain:** "The Synchronous Chain." Each step waits for the previous one. If embedding generation is slow, the user waits. If the notification service is down, the entire upload fails.

**The Hero:** "The Event Pipeline." Upload returns immediately, emitting a `DocumentUploaded` event. Independent consumers handle each step at their own pace with their own retry logic.

**The Plot:**

1. Understand the difference: Message Queue (RabbitMQ — point-to-point) vs Event Stream (Kafka — pub-sub log)
2. Design event schemas with backward compatibility (Avro/Protobuf)
3. Implement idempotent consumers (same event processed twice = same result)
4. Handle ordering guarantees: partition-level ordering in Kafka

**The Twist (Failure):** **The Poison Message.** A malformed PDF causes the text extraction consumer to crash. The message is redelivered, crashes again, and creates an infinite loop while subsequent messages pile up.

**Interview Signal:** Can design a dead-letter queue strategy and explain exactly-once vs at-least-once semantics.

### 🧠 Queue vs Stream Decision

| Factor | Message Queue (RabbitMQ) | Event Stream (Kafka) |
|--------|--------------------------|---------------------|
| **Pattern** | Task distribution | Event log (replayable) |
| **Consumption** | Message deleted after processing | Consumer tracks offset |
| **Use case** | "Process this document" | "Document was uploaded" (multiple consumers) |
| **Ordering** | Per-queue FIFO | Per-partition ordering |
| **Pipeline Context** | Background job processing | Event sourcing document revision history |
