# Convert Decimal Number to Base K

## Problem Statement

Given two integers `N` and `K`, convert the decimal number `N` to its representation in base `K`.

---

## Input

- `N` — an integer in decimal (1 ≤ N ≤ 10⁵)  
- `K` — the base to convert to (2 ≤ K ≤ 10)

---

## Output

Return the number represented in base `K` as an integer.

---

## Examples

**Example 1:**

Input: N = 10, K = 2
Output: 1010
Explanation: (10)₁₀ = (1010)₂

markdown
Copy code

**Example 2:**

Input: N = 4, K = 8
Output: 4
Explanation: (4)₁₀ = (4)₈

## Expected Complexity

- **Time Complexity:** O(logₖN)  
- **Auxiliary Space:** O(logₖN)
