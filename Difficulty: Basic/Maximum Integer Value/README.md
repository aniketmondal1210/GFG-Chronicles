# Maximum Value by Inserting '+' or '*' Between Digits

## Problem

Given a string `S` consisting of digits (`0-9`), traverse the string from **left to right**.

- Start with the first digit as the initial value.
- For every next digit, insert either:
  - `'+'`, or
  - `'*'`
- Choose the operation that gives the **maximum possible value** at each step.

Return the maximum value obtained after processing the entire string.

---

## Examples

### Example 1

**Input**

```text
S = "01230"
```

**Output**

```text
9
```

**Explanation**

```text
Start = 0

0 + 1 = 1      (better than 0 × 1)

1 + 2 = 3      (better than 1 × 2 = 2)

3 × 3 = 9      (better than 3 + 3 = 6)

9 + 0 = 9      (better than 9 × 0 = 0)
```

Final answer:

```text
9
```

---

### Example 2

**Input**

```text
S = "891"
```

**Output**

```text
73
```

**Explanation**

```text
Start = 8

8 × 9 = 72

72 + 1 = 73
```

Final answer:

```text
73
```

---

## Your Task:
You don't need to read input or print anything. Your task is to complete the function MaximumIntegerValue() which takes the string S as input parameter and returns the maximum integer value that can be created using given procedures

## Expected Time Complexity: O(|S|)
## Expected Auxiliary Space: O(1)

## Constraints:

- 1 <= |S| < 20
- S contains only digits from 0 to 9
- Leading 0's maybe present.

---
