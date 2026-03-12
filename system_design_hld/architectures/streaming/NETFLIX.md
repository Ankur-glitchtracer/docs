# 🍿 System Design: Video Streaming Service (Netflix/YouTube)

## 📝 Overview
A **Global Video Streaming Platform** designed to deliver high-quality content to millions of concurrent users worldwide. It focuses on low-latency content delivery via CDNs and utilizes adaptive bitrate streaming to ensure a smooth viewing experience across varying network conditions.

!!! abstract "Core Concepts"

    - **CDN/Edge Caching:** Placing content closer to users within ISP networks to reduce latency and backbone congestion.
    - **Adaptive Bitrate (ABR):** Dynamically adjusting video quality (HLS/DASH) in real-time based on the user's available bandwidth.
    - **Transcoding DAGs:** Using Directed Acyclic Graphs to manage complex video processing pipelines for thousands of device formats.

## 🛠️ Functional & Non-Functional Requirements
### Functional Requirements

1. **Video Upload:** Fast and reliable ingestion of high-resolution source files.
2. **Adaptive Streaming:** Seamless playback that adjusts quality based on network speed.
3. **Global Search:** Low-latency search across a massive library of titles.

### Non-Functional Requirements

1. **High Availability:** 99.99% uptime for the playback service.
2. **Low Latency:** Minimal startup time (Time to First Frame) and no mid-stream buffering.
3. **Storage Efficiency:** Utilizing intelligent tiering to manage petabytes of data cost-effectively.

## 🧠 The Engineering Story

**The Villain:** "The Buffering Circle." 100M users try to watch "Squid Game" at the same time. If they all hit your central data center in Virginia, the internet backbone melts, and everyone sees a 404.

**The Hero:** "The Global CDN Architecture." Pre-distributing video chunks to edge servers (Open Connect) located inside the ISP's own office.

**The Plot:**

1. **Ingestion:** Upload high-res source files to S3.
2. **Transcoding:** Generate 1,000 variants (4K, 1080p, 720p for different devices/bandwidths).
3. **Storage:** Tiered storage (Standard for hot movies, Glacier for 1920s docs).
4. **Streaming:** Adaptive Bitrate (ABR) using HLS/DASH.

**The Twist (Failure):** **The Metadata Storm.** The video streams fine, but the "Play" button takes 10 seconds to load because the recommendation engine is down.

**Interview Signal:** Mastery of **Heavy Asset Delivery**, **Microservices**, and **Global Content Distribution**.

## 🏗️ High-Level Architecture
Design a platform capable of ingesting, processing, and streaming high-quality video to a global audience.

### Key Design Challenges:

- **The Transcoding Pipeline:** How do you handle thousands of simultaneous uploads without bottlenecking? (DAG-based workflows).
- **CDN Strategy:** When to use a public CDN (Cloudflare) vs building your own (Netflix Open Connect).
- **Video Storage:** Managing tiered storage (S3 Standard vs Glacier) for old/rarely watched content.

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

## 🔗 Related Architectures

- [S3 Lite](../distributed_storage/S3_LITE.md) — For video storage patterns.
