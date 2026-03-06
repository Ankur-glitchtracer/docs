# HLD: Design a Distributed Blob Store (S3 Lite)

## 🚀 Problem Statement
Design a highly available and durable object storage service capable of storing exabytes of unstructured data (images, videos, backups) for millions of customers.

## 🛠️ Functional Requirements
1. **Object CRUD:** Upload, Download, and Delete objects via a REST API.
2. **Bucket Management:** Logical grouping of objects.
3. **Versioning:** Maintain multiple versions of an object.

## 📈 Non-Functional Requirements
1. **Durability:** 99.999999999% (11 nines) – data must never be lost.
2. **Availability:** 99.99% – system must be reachable globally.
3. **Scalability:** Scale horizontally to handle trillions of objects.

## 🧠 Key Design Challenges
- **Data Redundancy:** Replication vs. Erasure Coding. How do you handle disk or rack failures?
- **Metadata Management:** Where do you store object metadata (size, hash, owner)? Is it a SQL DB or a Key-Value store?
- **Handling Large Objects:** How to handle 5TB file uploads? (Multipart uploads).
- **Data Integrity:** Ensuring bits don't flip over 10 years (Check-summing and Scrubbing).
