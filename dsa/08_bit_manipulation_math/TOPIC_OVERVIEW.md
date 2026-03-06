# 🔢 Topic Overview: Bit Manipulation & Math

Bit manipulation allows for high-speed constant-time operations, while Math (Number Theory) is essential for cryptography and large-scale computations.

## 🔑 Key Concepts Checklist
- [ ] **Bitwise Ops:** AND, OR, XOR, NOT, Left/Right Shift.
- [ ] **Bitmasks:** Representing sets or states using an integer.
- [ ] **Sieve of Eratosthenes:** Finding all primes up to $N$ in $O(N \log \log N)$.
- [ ] **Binary Exponentiation:** Computing $a^b \pmod m$ in $O(\log b)$.
- [ ] **GCD/LCM:** Euclidean algorithm for Greatest Common Divisor.

## 🎯 Essential Problem Checklist (95% Coverage)
| Problem | Key Concept | Difficulty |
| :--- | :--- | :--- |
| **Number of 1 Bits** | `n & (n-1)` trick | Easy |
| **Single Number** | XOR property ($a \oplus a = 0$) | Easy |
| **Counting Bits** | Dynamic Programming + Bits | Medium |
| **Sum of Two Integers** | Bitwise addition (carry logic) | Medium |
| **Reverse Bits** | Bit shifting | Easy |
| **Binary Exponentiation** | $O(\log N)$ power | Medium |
| **Count Primes** | Sieve of Eratosthenes | Medium |
| **Missing Number** | XOR or Gauss Summation | Easy |

## 🚀 Key Pattern: The `n & (n-1)` Trick
This operation removes the lowest set bit of $n$. It is used to count set bits or check if a number is a power of 2.
```cpp
int countSetBits(int n) {
    int count = 0;
    while (n > 0) {
        n &= (n - 1);
        count++;
    }
    return count;
}
```

## 📚 Recommended Reading (CP-Algorithms)
- [Binary Exponentiation](https://cp-algorithms.com/algebra/binary-exp.html)
- [Euclidean algorithm for GCD](https://cp-algorithms.com/algebra/euclid-algorithm.html)
- [Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)
- [Bit Manipulation Tricks](https://cp-algorithms.com/algebra/bit-manipulation.html)
