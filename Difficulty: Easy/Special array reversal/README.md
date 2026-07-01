# Reverse String Without Affecting Special Characters

## Problem

Given a string **S** containing alphabets and special characters, reverse **only the alphabetic characters** while keeping all special characters in their original positions.

---

## Examples

### Example 1

**Input**

```text
S = "A&B"
```

**Output**

```text
"B&A"
```

**Explanation**

Only the letters are reversed, while `'&'` remains at the same position.

---

### Example 2

**Input**

```text
S = "A&x#"
```

**Output**

```text
"x&A#"
```

**Explanation**

Only `'A'` and `'x'` are swapped. The special characters `'&'` and `'#'` remain in their original positions.

---

## Your Task:  
You don't need to read input or print anything. Your task is to complete the function reverse() which takes the string as inputs and returns required reverse string.

## Expected Time Complexity: O(|S|)
## Expected Auxiliary Space: O(|S|)

## Constraints:

- 1 ≤ |S| ≤ 10^5

---
