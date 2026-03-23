---
impact: "Low"
nr: false
confidence: 5
---
# ↔️ Two Pointers: Valid Palindrome

## 📝 Overview
The "Valid Palindrome" problem asks us to determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases. This is a classic application of the **Two Pointers** technique, enabling string verification in linear time with constant space efficiency.

!!! abstract "Core Concepts"
    - **Two Pointers:** Using indices at both ends of a sequence to compare elements moving inwards.
    - **In-Place Traversal:** Processing data without allocating significant auxiliary memory.
    - **ASCII Handling:** Efficiently checking character types (alphanumeric) and case conversion.

---

## 🏭 The Engineering Story & Problem

### 😡 The Villain (The Naive Approach)
The straightforward way to solve this is to "clean" the string first. You might create a completely new string containing only the lowercase alphanumeric characters and then compare it to its reverse.
While intuitive, this doubles the memory usage. In memory-constrained environments or with massive strings (like DNA sequences or log streams), allocating a new filtered string for every check is wasteful and can lead to memory exhaustion.

### 🦸 The Hero (Two Pointers)
Enter the **Two Pointers** technique. Instead of creating a copy, we employ two "scouts" (pointers): one starting at the beginning (`left`) and one at the end (`right`). They move towards each other, skipping non-alphanumeric trash. They only compare when both find a valid character. If they meet in the middle without finding a mismatch, the string is a palindrome.
This approach uses **$\mathcal{O}(1)$ space**, treating the input string as a read-only resource.

### 📜 Requirements & Constraints
1.  **Input:** A string `s` containing printable ASCII characters.
2.  **Output:** Boolean `true` if palindrome, `false` otherwise.
3.  **Constraints:** $1 \le s.length \le 2 \cdot 10^5$.
4.  **Edge Cases:** Empty strings, strings with only symbols (e.g., `",."` $\rightarrow$ `true`), mixed case (`"A man..."`).

---

## 🏗️ Structure & Blueprint

### Algorithmic Flow (Sequence)
```mermaid
graph TD
    Start([Start]) --> Init[Init L=0, R=len-1]
    Init --> CheckCondition{L < R?}
    CheckCondition -- No --> True([Return True])
    CheckCondition -- Yes --> CheckL{Is s[L] alnum?}
    
    CheckL -- No --> IncL[L++] --> CheckCondition
    CheckL -- Yes --> CheckR{Is s[R] alnum?}
    
    CheckR -- No --> DecR[R--] --> CheckCondition
    CheckR -- Yes --> Compare{lower(s[L]) == lower(s[R])?}
    
    Compare -- No --> False([Return False])
    Compare -- Yes --> Next[L++, R--] --> CheckCondition
```

---

## 💻 Implementation & Code

### 🧠 Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ — We traverse the string exactly once (each character is visited by either L or R).
- **Space Complexity:** $\mathcal{O}(1)$ — No new strings or data structures are allocated; only two integer variables are used.

### 🐍 The Code

??? failure "The Villain's Code (Naive - O(N) Space)"
    ```python
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            # 1. Filter out non-alphanumeric chars and convert to lower case
            filtered_chars = [char.lower() for char in s if char.isalnum()]
            
            # 2. Join back to string (creates new memory)
            filtered_s = "".join(filtered_chars)
            
            # 3. Compare with reverse (creates another string copy)
            return filtered_s == filtered_s[::-1]
    ```

???+ success "The Hero's Code (Two Pointers - O(1) Space)"
    ```python
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            l, r = 0, len(s) - 1
            
            while l < r:
                # 1. Move Left pointer forward until alphanumeric
                if not s[l].isalnum():
                    l += 1
                    continue
                
                # 2. Move Right pointer backward until alphanumeric
                if not s[r].isalnum():
                    r -= 1
                    continue
                
                # 3. Compare characters (case-insensitive)
                if s[l].lower() != s[r].lower():
                    return False
                
                # 4. Move pointers inward
                l += 1
                r -= 1
                
            return True
    ```

---

## ⚖️ Trade-offs & Testing

| Strategy | Pros (Why it works) | Cons (The Twist / Pitfalls) |
| :--- | :--- | :--- |
| **Naive Filtering** | Extremely readable, one-liner in Python. | Uses $\mathcal{O}(N)$ extra memory. Two passes (one to filter, one to reverse). |
| **Two Pointers** | $\mathcal{O}(1)$ Memory. Single pass. Efficient. | Slightly more complex code. Must handle index out-of-bounds carefully if implementing raw loops. |

### 🧪 Testing Strategy
- **Empty/Blank:** `""` or `"   "` should return `true`.
- **Symbols Only:** `",.:"` should return `true`.
- **Mixed Case:** `"RaceCar"` should return `true`.
- **Almost Palindrome:** `"race a car"` should return `false`.

---

## 🎤 Interview Toolkit

- **Interview Signal:** Demonstrates understanding of memory efficiency and ability to manipulate array indices without "off-by-one" errors.
- **When to Use:** Keywords like "in-place", "constant space", "compare ends", or "palindrome".
- **Scalability Probe:** "How would this handle a 10GB file stream?" (The Two Pointer approach allows streaming if we can seek, but usually implies loading chunks. Naive approach crashes memory immediately.)
- **Design Alternatives:** Recursion could work (check outer, recurse inner), but it adds $\mathcal{O}(N)$ stack depth, risking stack overflow.

## 🔗 Related Problems
- [Two Sum II](../two_sum_ii/PROBLEM.md) — Another classic Two Pointer problem.
- [Container With Most Water](../container_with_most_water/PROBLEM.md)
- [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) — Palindrome allowing one deletion.
