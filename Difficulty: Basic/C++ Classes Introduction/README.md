# CollegeCourse Class Implementation

## Problem Statement
Create a class named `CollegeCourse` with the following:
- **Fields**:  
  - `courseID` (string)  
  - `grade` (char)  
  - `credits` (int)  
  - `gradePoints` (int)  
  - `honorPoints` (float)  

- **Calculations**:  
  - `gradePoints` are assigned as:  
    - A → 10  
    - B → 9  
    - C → 8  
    - D → 7  
    - E → 6  
    - F → 5  
  - `honorPoints = gradePoints × credits`

---

## Functions
1. `set_CourseId(string CID)` → sets courseId  
2. `set_Grade(char g)` → sets grade (case-insensitive)  
3. `set_Credit(int cr)` → sets credits  
4. `calculateGradePoints(char g)` → returns gradePoint (int)  
5. `calculateHonorPoints(int gp, int cr)` → returns honorPoint (float)  
6. `display()` → prints gradePoint and honorPoint  

---

## Examples

### Example 1
**Input:**  

CSN-206 A 4

**Output:**  

10 40


### Example 2
**Input:**  

ECE-500 d 3

**Output:**  

7 21


---

## Constraints
- 1 ≤ CID.length() ≤ 100  
- 'A' ≤ g ≤ 'F' (case insensitive)  
- 1 ≤ credits ≤ 4  

---
