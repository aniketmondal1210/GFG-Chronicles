# Count Numbers Containing the Digit '0' — `CountNo()`

## Problem Statement
Given a number **N**, find how many integers from **1 to N** contain **'0'** as one of their digits.

---

## Examples

### **Example 1**
**Input:**
N = 20

Output:

2

Explanation:
Numbers that contain 0 are 10 and 20.
Example 2

Input:

N = 100

Output:

10

Explanation:
Numbers that contain 0 are:
10, 20, 30, 40, 50, 60, 70, 80, 90, and 100.

## Time & Space Complexity

Time Complexity: O(N * log10(N))
(Each number is converted to a string, which takes log₁₀(N) time per number.)

Space Complexity: O(1)
(Only a few variables used regardless of input size.)
