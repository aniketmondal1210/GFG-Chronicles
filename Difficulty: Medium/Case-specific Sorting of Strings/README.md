# Sort Uppercase & Lowercase Separately

## Problem Statement

Given a string `s` of uppercase and lowercase letters:

- Sort **uppercase letters among themselves**
- Sort **lowercase letters among themselves**
- Keep the **original positions' case unchanged**

That means:
- If index `i` had uppercase → still uppercase after sorting
- If index `i` had lowercase → still lowercase after sorting

---

# Examples

### Example 1

**Input**
```
s = "GEekS"
```

Uppercase → G, E, S → sorted → E, G, S  
Lowercase → e, k → sorted → e, k  

Rebuild:
```
E G e k S
```

**Output**
```
EGekS
```

---

### Example 2

**Input**
```
s = "XWMSPQ"
```

All uppercase → just sort:
```
MPQSWX
```

**Output**
```
MPQSWX
```

---

## Constraints:

- 1 ≤ s.length() ≤ 10^5

---
