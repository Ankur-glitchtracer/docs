# 🔐 HLD: Security, Identity & Cryptography

## 📝 Overview
Senior engineers must design for security from day one. This module covers authentication, authorization, and protection against common attack vectors.

!!! abstract "Core Concepts"
    - **Identity:** OAuth2.0 (Authorization) and OIDC (Authentication).
    - **Tokens:** JWT (Stateless) vs. SessionID (Stateful).
    - **Cryptography:** Symmetric (AES) vs. Asymmetric (RSA/Diffie-Hellman) and Digital Signatures.

## 🚀 Security Fundamentals
### 1. Common Attack Vectors
- **CSRF:** Cross-Site Request Forgery (Mitigation: SameSite cookies, CSRF tokens).
- **XSS:** Cross-Site Scripting (Mitigation: Content Security Policy, escaping).
- **SQL Injection:** (Mitigation: Parameterized queries).
- **CORS:** Cross-Origin Resource Sharing (Properly configuring headers).

### 2. Distributed Identity
- **JWT:** Pros (Scalability) vs. Cons (Revocation difficulty).
- **API Gateway Auth:** Offloading security checks to the edge.
