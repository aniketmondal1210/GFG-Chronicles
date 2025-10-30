# Find Focal Length of a Spherical Mirror

## Problem Statement
Given the **radius of curvature (R)** of a spherical mirror and the **type** of mirror, find its **focal length**.

- For a **concave mirror**:

  f = {floor}(R / 2)

- For a **convex mirror**:  

  f = \text{floor}(-R / 2)

where `floor(x)` represents the greatest integer less than or equal to `x`.

---

## Example

### **Example 1**
**Input:**
type = "concave"
R = 5.4

Output:

2

Explanation:
Focal length = floor(R / 2) = floor(5.4 / 2) = floor(2.7) = 2.
Example 2

Input:

type = "convex"
R = 10

Output:

-5

Explanation:
Focal length = floor(-R / 2) = floor(-10 / 2) = floor(-5) = -5.
