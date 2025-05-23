# Conditional Check with Boolean Flag

## Problem Statement

Given two integer variables `a` and `b`, and a boolean variable `flag`, return `True` if:

- Either `a` or `b` (but not both) is non-negative and `flag` is `False`.
- Both `a` and `b` are negative and `flag` is `True`.

Otherwise, return `False`.

## Examples

### Example 1:
Input:  
`a = 1, b = -1, flag = False`  
Output:  
`True`  
Explanation: `a` is positive, `b` is negative, and `flag` is `False`, so condition 1 is satisfied.

### Example 2:
Input:  
`a = -182, b = -9121, flag = True`  
Output:  
`True`  
Explanation: Both are negative and `flag` is `True`, so condition 2 is satisfied.

### Example 3:
Input:  
`a = 5, b = 3, flag = True`  
Output:  
`False`  
Explanation: Neither condition 1 nor 2 is satisfied.

## Constraints

- `-10 <= a, b <= 10`
- `flag ∈ {True, False}`
