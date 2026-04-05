# 🐍 Python + Cybersecurity Learning Roadmap

> A structured self-learning path from Python basics to security-oriented development — built around real projects, not just theory.

---

## 📍 Current Status

| Phase | Topic | Status |
|-------|-------|--------|
| Phase 1 | Practical Python + Linux Foundation | ✅ Done |
| Phase 2 | Networking + HTTP + Backend Basics | ✅ Done |
| Phase 3 | Python Backend (Flask) | ✅ Done |
| Phase 4 | Security Fundamentals | ✅ Done |
| Phase 5 | Python + Security Combined | 🔄 In Progress |
| Phase 6 | DSA for Placement | 🔄 Running in Parallel |

---

## Phase 1 — Practical Python + Linux Foundation
**Goal:** Become comfortable writing useful Python scripts and working in Linux.

### Python
File handling, exceptions, modules, requests, JSON/CSV, regex, logging, virtual environments, argparse, SQLite basics

### Linux
Terminal navigation, files/folders, grep/find/cat/tail/head, chmod, processes, package install, environment variables, cron basics, SSH basics

### Projects Built
- **Auto-Commit Solutions** — Fetches accepted LeetCode/Codeforces submissions and auto-commits them to GitHub using requests, file handling, subprocess, argparse, logging, and cron

---

## Phase 2 — Networking + HTTP + Backend Basics
**Goal:** Understand how real applications communicate.

### Topics
IP, DNS, ports, TCP vs UDP, client-server model, HTTP/HTTPS, request/response cycle, status codes, headers, cookies, sessions, REST APIs, authentication basics

### Practice
Used `curl`, called public APIs in Python, inspected headers, made GET/POST requests, understood login flows

---

## Phase 3 — Python Backend (Flask)
**Goal:** Build actual backend projects.

### Topics
Routing, GET/POST/PUT/DELETE, JSON responses, forms and request body, CRUD operations, SQLite/MySQL, auth basics, validation, error handling, environment variables, basic deployment

---

## Phase 4 — Security Fundamentals
**Goal:** Understand security from a practical and defensive angle.

### Topics
CIA triad, authentication vs authorization, hashing vs encryption, common cyber attack types, OWASP Top 10, SQL injection, XSS, broken auth, insecure APIs, brute force, logging and monitoring, SOC basics, alerts/IOC/false positives/triage, secure coding basics

### Practice Platforms
TryHackMe · PortSwigger Web Security Academy · OverTheWire Bandit

---

## Phase 5 — Python + Security Combined ← *Currently Here*
**Goal:** Build security-oriented tools using Python.

### Projects Planned
- Log analysis and suspicious login detector
- Website security headers checker
- File integrity monitor
- URL/IP checker using threat reputation APIs
- Incident dashboard (Flask + login + severity tracking)

---

## Phase 6 — DSA for Placement (Parallel)
Arrays, strings, hashing, two pointers, sliding window, linked list, stack/queue, binary search, recursion, trees, heaps, graphs, DP basics — practiced daily alongside all other phases.

---

## 🛠️ Projects

### Auto-Commit Solutions
> Automatically fetches accepted LeetCode and Codeforces submissions and pushes them to GitHub every 10 minutes via cron.

**Tech used:** `requests`, `subprocess`, `argparse`, `logging`, file handling, REST API, GraphQL API, cron  
**Repo:** [auto-commit-solutions](https://github.com/YOUR_USERNAME/auto-commit-solutions)

---

## 📚 Resources Used

- YouTube (searched topic-by-topic per phase)
- TryHackMe — hands-on security labs
- PortSwigger Web Security Academy — web vulnerability practice
- OverTheWire Bandit — Linux + security wargames
- LeetCode / Codeforces — DSA practice
