# Tidy Number

## Problem

Given an integer **n**, check whether it is a tidy number.

A number is called **tidy** if its digits are in non-decreasing order from left to right.

### Examples

#### Example 1
```text
Input: n = 1234
Output: true
Explanation: The digits 1, 2, 3 and 4 are in non-decreasing order.
```

#### Example 2
```text
Input: n = 1243
Output: false
Explanation: Since 4 > 3, the digits are not in non-decreasing order.
```

## Constraints

- `1 ≤ n ≤ 10^9`

## Solution

```python
def is_tidy(n):
    digits = str(n)

    for i in range(1, len(digits)):
        if digits[i] < digits[i - 1]:
            return False

    return True
```

## Sample Usage

```python
print(is_tidy(1234))  # True
print(is_tidy(1243))  # False
```
