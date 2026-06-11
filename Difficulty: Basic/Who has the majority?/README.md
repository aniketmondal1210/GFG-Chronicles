# More Frequent Element

## Problem

Given an array `arr[]` and two elements `x` and `y`, return:

- The element that occurs more frequently in the array.
- If both elements have the same frequency, return the smaller element.

---

## Examples

### Example 1

**Input**

```text
arr[] = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]
x = 4
y = 5
```

**Output**

```text
4
```

**Explanation**

```text
Frequency of 4 = 4
Frequency of 5 = 1
```

Since `4` occurs more frequently, return `4`.

---

### Example 2

**Input**

```text
arr[] = [1, 2, 3, 4, 5, 6, 7, 8]
x = 1
y = 7
```

**Output**

```text
1
```

**Explanation**

```text
Frequency of 1 = 1
Frequency of 7 = 1
```

Both frequencies are equal, so return the smaller element, `1`.

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^6
- 0 ≤ arr[i] , x , y ≤ 10^8

---
