# Sort Elements by Frequency

## Problem Description

Given an array of integers `arr[]`, sort the array according to the frequency of elements, i.e., elements that have higher frequencies come first. If the frequencies of two elements are the same, the smaller number comes first.

---

## Examples

### Example 1
- **Input:** `arr[] = [5, 5, 4, 6, 4]`
- **Output:** `[4, 4, 5, 5, 6]`
- **Explanation:** The highest frequency is `2`. Both `5` and `4` have that frequency. Since frequencies are the same, the smaller element (`4`) comes first. Thus, `4 4` comes before `5 5`, followed by `6`.

### Example 2
- **Input:** `arr[] = [9, 9, 9, 2, 5]`
- **Output:** `[9, 9, 9, 2, 5]`
- **Explanation:** Element `9` has the highest frequency (`3`) and comes first. Both `2` and `5` have a frequency of `1`, so the smaller element (`2`) comes before `5`.

---

## Constraints

- $1 \le \text{arr.size()}, \text{arr}[i] \le 10^5$

---
