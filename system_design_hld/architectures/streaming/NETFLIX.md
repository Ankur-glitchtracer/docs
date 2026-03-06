# HLD: Design a Video Streaming Service (Netflix/YouTube)

## 🚀 Problem Statement
Design a platform capable of ingesting, processing, and streaming high-quality video to a global audience.

## 🛠️ Functional Requirements
1. **Video Upload:** Fast and reliable ingestion.
2. **Streaming:** Adaptive bitrate streaming based on user bandwidth.
3. **Search:** Real-time search across millions of videos.

## 📈 Non-Functional Requirements
1. **Reliability:** No buffering during peak hours.
2. **Scalability:** Handle massive spikes (e.g., a viral video release).
3. **Cost Optimization:** Blob storage and egress costs are astronomical.

## 🧠 Key Design Challenges (5YOE Focus)
- **The Transcoding Pipeline:** How do you handle thousands of simultaneous uploads without bottlenecking? (DAG-based workflows).
- **CDN Strategy:** When to use a public CDN (Cloudflare) vs building your own (Netflix Open Connect).
- **Video Storage:** Managing tiered storage (S3 Standard vs Glacier) for old/rarely watched content.
