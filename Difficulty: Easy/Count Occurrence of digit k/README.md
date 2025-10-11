# Count Digit Occurrences in Array

## Problem Statement

Given an array `arr[]`, your task is to return an integer denoting the total number of times **digit `k`** appears in the array.

---

## Input

* An integer `k` (the digit to count).
* An array of integers `arr[]`.

**Constraints:**

```
1 ≤ arr.size() ≤ 20
1 ≤ arr[i] ≤ 1000
1 ≤ k ≤ 9
```

---

## Output

Return an integer representing the total number of times digit `k` appears in the array.

---

## 💡 Examples

### Example 1

**Input:**

```
k = 1, arr = [11, 12, 13, 14, 15]
```

**Output:**

```
6
```

**Explanation:**

```
Digit '1' appears 6 times across all numbers.
```

---

### Example 2

**Input:**

```
k = 3, arr = [11, 121, 15]
```

**Output:**

```
0
```

**Explanation:**

```
Digit '3' does not appear in any number.
```

---

**Expected Complexity:**

* Time Complexity: **O(n)**
* Auxiliary Space: **O(1)**

---
