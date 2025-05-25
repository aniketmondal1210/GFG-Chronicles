# Starts and Ends with 'gfg'

## Problem Statement

Given a string `S`, determine whether it **starts** and **ends** with the substring `"gfg"` (case insensitive).

To solve this, you can use the following string functions:
- `S.lower()`
- `S.upper()`
- `S.startswith('string')`
- `S.endswith('string')`

## Your Task

Write a function `gfg(S)` that:
- Takes a string `S` as input.
- Prints `"Yes"` if `S` starts and ends with `'gfg'` (ignoring case).
- Otherwise, prints `"No"`.

## Examples

### Example 1
**Input:**  
`S = "gFgabcdEGfG"`  
**Output:**  
`Yes`  
**Explanation:**  
After converting to lowercase → `"gfgabcdegfg"`  
Starts and ends with `'gfg'`.

### Example 2
**Input:**  
`S = "GgfhTnagfg"`  
**Output:**  
`No`  
**Explanation:**  
After converting to lowercase → `"ggfhtnagfg"`  
Only ends with `'gfg'`, doesn't start with it.

## Constraints

- `1 ≤ |S| ≤ 10^5`
