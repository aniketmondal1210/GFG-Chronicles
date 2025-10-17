# AND Gate Output

## Problem Statement

Given **N bits** as input to an **AND gate**, find the output that will be produced.

### AND Gate Truth Table

| Input A | Input B | Output |
| ------- | ------- | ------ |
| 1       | 1       | 1      |
| 1       | 0       | 0      |
| 0       | 1       | 0      |
| 0       | 0       | 0      |

---

## 📥 Input

* An integer `N` — the number of bits.
* An array `arr[]` containing `N` bits (0 or 1).

**Constraints:**

```
1 ≤ N ≤ 1000
```

---

## Output

Return the final output after applying AND operation on all N bits.

---

## Examples

### Example 1

**Input:**

```
N = 4
arr = [1, 1, 1, 0]
```

**Output:**

```
0
```

**Explanation:**

```
1 & 1 = 1
1 & 1 = 1
1 & 0 = 0
Final output = 0
```

---

### Example 2

**Input:**

```
N = 4
arr = [0, 0, 1, 0]
```

**Output:**

```
0
```

**Explanation:**

```
0 & 0 = 0
0 & 1 = 0
0 & 0 = 0
Final output = 0
```

---

**Expected Complexity:**

* Time Complexity: **O(N)**
* Space Complexity: **O(1)**

---
