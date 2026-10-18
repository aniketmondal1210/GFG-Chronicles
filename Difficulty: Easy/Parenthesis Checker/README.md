# Parenthesis Checker

## Problem Description

Given a string `s`, composed of different combinations of `'('`, `')'`, `'{'`, `'}'`, `'['`, `'u'`. Determine whether the expression is balanced or not.

An expression is balanced if:
1. Each opening bracket has a corresponding closing bracket of the same type.
2. Opening brackets must be closed in the correct order.

---

## Examples

### Example 1
- **Input:** `s = "[{()}]"`
- **Output:** `true`
- **Explanation:** All the brackets are well-formed.

### Example 2
- **Input:** `s = "[()()]{}"`
- **Output:** `true`
- **Explanation:** All the brackets are well-formed.

### Example 3
- **Input:** `s = "([]"`
- **Output:** `false`
- **Explanation:** The expression is not balanced as there is a missing `')'` at the end.

### Example 4
- **Input:** `s = "([{]})"`
- **Output:** `false`
- **Explanation:** The expression is not balanced as there is a closing `']'` before the closing `'}'`.

---

## Constraints

- 1 ≤ s.size() ≤ 10^6
- s[i] = [, ], {, }, (, )

---
