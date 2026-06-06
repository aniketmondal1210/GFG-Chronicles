# Divisibility by 11

## Problem

Given a number `S` in the form of a string, determine whether it is divisible by `11`.

Return:
- `1` if divisible by `11`
- `0` otherwise

---

## Examples

### Example 1

**Input**
```text
S = "76945"
```

**Output**
```text
1
```

**Explanation**

```text
76945 % 11 = 0
```

Therefore, the number is divisible by 11.

### Example 2

**Input**
```text
S = "12"
```

**Output**
```text
0
```

**Explanation**

```text
12 % 11 = 1
```

Therefore, the number is not divisible by 11.

---

## Your Task:
You don't need to read input or print anything. Your task is to complete the function divisibleBy11() which takes the number in the form of string S as input and returns 1 if the number is divisible by 11. Else, it returns 0.


## Expected Time Complexity: O(Log S) where S is the input number.
## Expected Auxiliary Space: O(1). 


# Constraints:

- 1 <= S<= 10^1000 + 5

---
