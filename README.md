# 🧠 DSA-Practice

> Structured Data Structures & Algorithms practice in Python — built around a 5-month METI internship preparation roadmap.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-Month%201%20of%205-orange)
![Problems](https://img.shields.io/badge/Problems%20Solved-23%2B-brightgreen)
![Roadmap](https://img.shields.io/badge/Goal-METI%20Internship%202026-red)

---

## 📌 About This Repository

This repo documents my daily DSA practice as part of a structured **5-month METI internship preparation roadmap**. Every problem is solved with a focus on:

- **Understanding the pattern**, not just the solution
- **Time & Space complexity** analysis for every approach
- **Brute-force → Optimized** thinking progression
- **Interview-ready** explanations

**Daily target:** 5 problems/day | 2 hours/day | 35 problems/week

---

## 🗺️ 5-Month Roadmap

| Month | Topics | Status |
|-------|--------|--------|
| **M1** | Arrays, Two Pointers, Sliding Window, Binary Search & Sorting | 🟡 In Progress |
| **M2** | Hashing, Stack, Queue / BFS, Heap | ⬜ Upcoming |
| **M3** | Binary Trees, BST, Graphs | ⬜ Upcoming |
| **M4** | Backtracking, Greedy, Mixed, Interview Mode | ⬜ Upcoming |
| **M5** | 1D DP, 2D DP, Mixed Practice, Final Mock | ⬜ Upcoming |

---

## 📁 Folder Structure

```
DSA-Practice/
│
├── Arrays/               ✅ Active
│   ├── basics.py
│   ├── two_sum.py
│   └── ...
│
├── Two-Pointers/         🔜 Coming Soon
├── Sliding-Window/       🔜 Coming Soon
├── Binary-Search/        🔜 Coming Soon
├── Hashing/              🔜 Coming Soon
├── Stack/                🔜 Coming Soon
├── Graphs/               🔜 Coming Soon
└── Dynamic-Programming/  🔜 Coming Soon
```

---

## 📊 Weekly Problem Log

| Week | Core Problems | Unseen | LeetCode Pattern | Interview Mixed | Total |
|------|:---:|:---:|:---:|:---:|:---:|
| Week 1 | 20 | 5 | 5 | 5 | **35** |
| Week 2 | 20 | 5 | 5 | 5 | **35** |
| ... | ... | ... | ... | ... | ... |

---

## 🧩 Problem Format

Each problem file follows this structure:

```python
"""
Problem: Two Sum
Difficulty: Easy
Pattern: Hash Map / Array
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
  Brute Force → O(n²): nested loops checking all pairs
  Optimized   → O(n):  hash map for complement lookup

Real-world analogy:
  Like scanning a guest list — instead of checking every pair,
  you remember who you've seen and instantly spot their match.
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

---

## 🎯 Goal

> Land a **METI-sponsored internship in Japan** (2026) and ultimately join a top Japanese tech company as an **AI Engineer** by 2028.

This repo is one pillar of a larger self-study plan that includes Python/AI, Data Science, and Japanese (JLPT N4 → N1).

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Practice Platforms:** LeetCode, HackerRank
- **Tools:** VS Code, Git

---

## 📬 Connect

- GitHub: [@Prashant-4527](https://github.com/Prashant-4527)
- Location: Jaipur, India 🇮🇳 → Tokyo, Japan 🇯🇵 (target)

---

*Updated regularly. Consistency > Perfection. 毎日練習！*
