# Angle Between Hour and Minute Hands

## Problem Statement
You are given a string `s` representing time in **24-hour format** `"HH:MM"`.  
Your task is to compute the **smallest angle** (in degrees) between the **hour** and **minute** hands of an analog clock.

---

## Input
A string `s` in the format `"HH:MM"`.

**Constraints:**

s.length = 5
00 ≤ HH ≤ 23
00 ≤ MM ≤ 59


---

## Output
Return the smallest angle between the hour and minute hands, **rounded to 3 decimal places**.

---

## Explanation
### Formula:
1. Convert the hour to 12-hour format:

hour = hour % 12

2. Calculate angles:

Hour hand angle = 30 × hour + 0.5 × minutes
Minute hand angle = 6 × minutes

3. Find the difference:

angle = abs(hour_angle - minute_angle)

4. The smaller angle between the two hands is:

min(angle, 360 - angle)


---

## Examples

### Example 1
**Input:**

s = "06:00"

**Output:**

180.000

**Explanation:**
- Hour hand = 6 × 30 = 180°
- Minute hand = 0 × 6 = 0°
- Difference = 180°, smallest angle = 180.000°

---

### Example 2
**Input:**

s = "03:15"

**Output:**

7.500

**Explanation:**
- Hour hand = 3 × 30 + 15 × 0.5 = 97.5°
- Minute hand = 15 × 6 = 90°
- Difference = 7.5°, smallest angle = 7.500°

---
