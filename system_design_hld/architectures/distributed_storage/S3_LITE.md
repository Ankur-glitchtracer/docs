# 📦 System Design: S3 Lite

## 📝 Overview
A **Distributed Object Store** designed for durability and scale. It handles massive amounts of unstructured data (blobs) with high availability, ensuring that data remains intact even across hardware failures.

!!! abstract "Core Concepts"

    - **Erasure Coding:** Breaking data into fragments and expanding it with redundant data for high durability.
    - **Consistent Hashing:** Efficiently distributing objects across a massive cluster of storage nodes.
    - **Metadata Separation:** Decoupling object metadata from raw data storage to scale independently.

## 🛠️ Functional & Non-Functional Requirements
### Functional Requirements

1. **Object CRUD:** Upload, Download, and Delete objects via a REST API.
2. **Bucket Management:** Logical grouping of objects.
3. **Versioning:** Maintain multiple versions of an object.

### Non-Functional Requirements

1. **Durability:** 99.999999999% (11 nines) – data must never be lost.
2. **Availability:** 99.99% – system must be reachable globally.
3. **Scalability:** Scale horizontally to handle trillions of objects.

## 🧠 The Engineering Story

**The Villain:** "The Bit Rot." Over 10 years, magnetic tape or disk drives will eventually fail, flipping a `0` to a `1` and corrupting your precious family photos.

**The Hero:** "The Erasure Coding & Scrubbing." Breaking data into $K$ chunks plus $M$ parity chunks so you can lose any $M$ disks and still recover the original file.

**The Plot:**

1. **Metadata Store:** Use a KV store to map `ObjectKey` to `PhysicalLocation`.
2. **Data Nodes:** Store raw bytes in large files (blobs).
3. **Replication:** Triple-replicate small files; Erasure-code large ones.
4. **Heartbeats:** Detect node failure and trigger background re-replication.

**The Twist (Failure):** **The Metadata Hot-path.** Everyone wants to list the objects in a bucket with 1B files, crashing the metadata database.

**Interview Signal:** Mastery of **Durability Architectures**, **Distributed Storage Strategies**, and **Failure Recovery**.

## 🏗️ High-Level Architecture
Design a highly available and durable object storage service capable of storing exabytes of unstructured data (images, videos, backups) for millions of customers.

### Key Design Challenges:

- **Data Redundancy:** Replication vs. Erasure Coding. How do you handle disk or rack failures?
- **Metadata Management:** Where do you store object metadata (size, hash, owner)? Is it a SQL DB or a Key-Value store?
- **Handling Large Objects:** How to handle 5TB file uploads? (Multipart uploads).
- **Data Integrity:** Ensuring bits don't flip over 10 years (Check-summing and Scrubbing).

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

Explore the low-level implementations of distributed storage and metadata management:

* [System Design: Distributed KV Store](./KV_STORE.md)
* [System Design: Distributed Storage (GFS)](./GFS.md)
* [Machine Coding: Cache System](../../../machine_coding/systems/cache_system/PROBLEM.md)
