# Module 14: ML Model Serving Infrastructure

### 🚀 Problem Statement
An embedding model might serve 500 QPS during business hours and only 5 QPS at night. Running 10 GPU instances 24/7 can be costly (e.g., $72K/month). During bulk-upload events, latency can spike if GPUs become saturated. It is necessary to scale resources up for spikes and down for idle periods to maintain efficiency and performance.

### 🧠 The Engineering Story

**The Villain:** "The Static Deployment." One model, one container, one size. The same infrastructure serves both a 100-token classification and a 4000-token document embedding — inefficiently for both.

**The Hero:** "The Adaptive Serving Platform." Dynamic batching, auto-scaling based on queue depth, model versioning with canary rollouts, and hardware-aware scheduling.

**The Plot:**

1. Design model serving with dynamic batching (group small requests into GPU-efficient batches)
2. Implement auto-scaling based on queue depth + latency, not just CPU
3. Set up A/B testing and canary deployment for model updates
4. Handle model versioning: roll back embeddings when model changes

**The Twist (Failure):** **The Embedding Drift.** Updating an embedding model from v1 to v2 while 50M existing embeddings remain as v1 can cause issues. Queries embedded with v2 might have low cosine similarity with v1 vectors, causing the RAG system to degrade silently.

**Interview Signal:** Can design a model serving system that handles versioning, batching, and graceful degradation.

### 📝 Design Exercise
> Design a model serving infrastructure that handles: 3 models (embedding, re-ranker, LLM), auto-scaling 0→50 GPUs, model versioning with zero-downtime rollout, and graceful degradation when GPU quota is exhausted.
