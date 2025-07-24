# Calculate Areas of Basic Geometric Shapes

## Problem Statement

Given:
- `L` and `W` as the **length** and **width** of a rectangle,
- `B` and `H` as the **base** and **height** (perpendicular) of a right-angled triangle,
- `R` as the **radius** of a circle,

Calculate and return the **areas** of:
1. Rectangle
2. Right-angled Triangle
3. Circle

---

## Formulas

- **Rectangle Area** = `L * W`
- **Triangle Area** = `0.5 * B * H`
- **Circle Area** = `3.14 * R * R`

---

## Examples

### Example 1:

**Input:**  
`L = 32, W = 32, B = 54, H = 12, R = 52`  
**Output:**  
`[1024, 324, 8490]`  
**Explanation:**
- Rectangle = 32 * 32 = 1024
- Triangle = 0.5 * 54 * 12 = 324
- Circle = 3.14 * 52 * 52 = 8490

---

### Example 2:

**Input:**  
`L = 2, W = 2, B = 4, H = 8, R = 4`  
**Output:**  
`[4, 16, 50]`  
**Explanation:**
- Rectangle = 2 * 2 = 4
- Triangle = 0.5 * 4 * 8 = 16
- Circle = 3.14 * 4 * 4 = 50.24 → Rounded to 50

---

## Constraints

- `1 ≤ L, W, B, H, R ≤ 10^4`

---

## Expected Time Complexity

- `O(1)`

## Expected Auxiliary Space

- `O(1)`

---
