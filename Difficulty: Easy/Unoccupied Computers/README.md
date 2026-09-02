# Cafe Computer Assignment

## Problem

A cafe has `n` computers. Customer events are represented by a string `s` of uppercase English letters.

Each distinct letter appears exactly twice:

- The **first occurrence** represents the customer's arrival.
- The **second occurrence** represents the customer's departure.

A customer gets a computer only if one is available when they arrive. Otherwise, the customer is rejected and does not use a computer.

Return the number of customers who could not be assigned a computer upon arrival.

## Examples

### Example 1

```text
Input: n = 3, s = "GACCBDDBAGEE"
Output: 1
```

**Explanation:**

Only customer `D` cannot get a computer.

### Example 2

```text
Input: n = 1, s = "ABCBAC"
Output: 2
```

**Explanation:**

Customers `B` and `C` cannot get computers.

## Constraints

```text
1 <= n <= 26
1 <= |s| <= 52
```

- `s` consists of uppercase English letters.
- Each letter occurs exactly twice.
