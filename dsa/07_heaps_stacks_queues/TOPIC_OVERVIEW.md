# 🥞 Topic Overview: Heaps, Stacks, Queues

These data structures are the workhorses of complex algorithms. Stacks provide LIFO, Queues provide FIFO, and Heaps provide Priority-based access.

## 🔑 Key Concepts Checklist
- [ ] **Monotonic Stack:** Find the next greater/smaller element in $O(N)$.
- [ ] **Monotonic Queue:** Sliding window maximum/minimum in $O(N)$.
- [ ] **Min/Max Heap:** Priority-based retrieval in $O(\log N)$.
- [ ] **Two Stacks/Queues:** Implementing one using the other (common design question).

## 🎯 Essential Problem Checklist (95% Coverage)
| Problem | Key Concept | Difficulty |
| :--- | :--- | :--- |
| **Valid Parentheses** | Stack | Easy |
| **Next Greater Element** | Monotonic Stack | Medium |
| **Daily Temperatures** | Monotonic Stack | Medium |
| **Sliding Window Maximum** | Monotonic Queue | Hard |
| **K-th Largest in Stream** | Min Heap | Easy |
| **Merge K Sorted Lists** | Min Heap | Hard |
| **Find Median from Stream** | Two Heaps (Max & Min) | Hard |
| **Task Scheduler** | Heap + Queue | Medium |

## 🚀 Key Pattern: Monotonic Stack (Next Greater Element)
```cpp
vector<int> nextGreater(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, -1);
    stack<int> st;
    for (int i = 0; i < n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i]) {
            res[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    return res;
}
```

## 📚 Recommended Reading (CP-Algorithms)
- [Minimum Stack / Minimum Queue](https://cp-algorithms.com/data_structures/stack_queue_modification.html)
- [Heaps (Priority Queue)](https://cp-algorithms.com/data_structures/heap.html)
