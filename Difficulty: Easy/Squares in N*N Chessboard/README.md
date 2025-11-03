# Total Number of Squares in an N×N Chessboard

## Problem Statement
Given an integer `N`, find the total number of **squares** present in an `N × N` chessboard.

---

## Example 1
**Input:**  

N = 1

**Output:**  

1

**Explanation:**  
A 1×1 chessboard has only one square.

---

## Example 2
**Input:**  

N = 2

**Output:**  

5

**Explanation:**  
A 2×2 chessboard has:  
- 4 squares of size 1×1  
- 1 square of size 2×2  
Total = 4 + 1 = 5 squares.

---

## Your Task
You don't need to read input or print anything.  
Your task is to complete the function **`squaresInChessBoard(N)`** which takes an integer `N` as input and returns the total number of squares in an `N × N` chessboard.

---

## Expected Time Complexity

O(1)


## Expected Auxiliary Space

O(1)


---

## Constraints

1 ≤ N ≤ 10⁵


---

## Formula
The total number of squares in an `N × N` chessboard is given by:  

1² + 2² + 3² + ... + N² = (N × (N + 1) × (2N + 1)) / 6
