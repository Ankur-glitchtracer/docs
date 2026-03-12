#  ⬜ Math: Detect Squares

## 📝 Description
[LeetCode 2013](https://leetcode.com/problems/detect-squares/)
Design a data structure that counts the number of ways to form an axis-aligned square with point `(x, y)` as one of the corners.

## 🛠️ Requirements/Constraints

- Numerical values fit within standard data types (int, long).
- Coordinate ranges are typically within $10^4$.

## 🧠 The Engineering Story

**The Villain:** "The Coordinate Search." Finding 3 other points to form a square. Searching all combinations is too slow.

**The Hero:** "The Diagonal Pivot." If we pick a diagonal point `(x, y)` and `(nx, ny)`, the other two points of an axis-aligned square are determined: `(x, ny)` and `(nx, y)`.

**The Plot:**

1. Store points in a HashMap (Count frequencies, as duplicates are allowed).
2. **Add:** Update count in map.
3. **Count:** Given query point `(qx, qy)`:
   - Iterate through all *other* existing points `(px, py)` in the map.
   - Check if `abs(qx - px) == abs(qy - py)` and `qx != px` (Diagonal condition).
   - If yes, look up the other two corners `(qx, py)` and `(px, qy)` in the map.
   - Add `count(px, py) * count(qx, py) * count(px, qy)` to total.

**The Twist (Failure):** **Iterating everything.** If we store points in `Map<x, Set<y>>`, we can iterate only points with same x-coordinate to optimize, but standard approach iterates all points.

**Interview Signal:** **Geometry Logic** and Hash Map usage.

## 🚀 Approach & Intuition
Iterate existing points to find diagonals.

### C++ Pseudo-Code
```cpp
class DetectSquares {
    map<pair<int, int>, int> counts;
    vector<pair<int, int>> points;
public:
    void add(vector<int> point) {
        counts[{point[0], point[1]}]++;
        points.push_back({point[0], point[1]});
    }
    
    int count(vector<int> point) {
        int qx = point[0], qy = point[1];
        int res = 0;
        
        for (auto& [px, py] : points) {
            if (abs(qx - px) != abs(qy - py) || qx == px) continue;
            
            res += counts[{qx, py}] * counts[{px, qy}];
        }
        return res;
    }
};
```

### Key Observations:

- Use modular arithmetic to prevent integer overflow and the Euclidean algorithm for GCD/LCM problems.
- In geometry, use cross products to determine orientation and the distance formula for proximity checks.

!!! info "Complexity Analysis"

    - **Time Complexity:** Add: $O(1)$, Count: $O(N)$ (where N is total points stored).
    - **Space Complexity:** $O(N)$.

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you solve this without using any arithmetic operators (+, -, *, /)?
- **Scale Question:** How do you handle bit operations on arbitrarily large integers (BigInt)?
- **Edge Case Probe:** How does your code handle signed vs unsigned integers and overflow/underflow?

## 🔗 Related Problems

- [Multiply Strings](../multiply_strings/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite: Bit Manipulation
