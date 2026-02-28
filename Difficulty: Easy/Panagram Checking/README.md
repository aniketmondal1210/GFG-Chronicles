# Check if a String is a Pangram

## Problem Statement

Given a string `s`, determine whether it is a **Pangram**.

A **Pangram** is a sentence that contains **every letter of the English alphabet (a–z)** at least once, either in lowercase or uppercase.

Return:

- `true` → if `s` is a Pangram  
- `false` → otherwise  

---

## Examples

### Example 1

**Input**
```
s = "Bawds jog, flick quartz, vex nymph"
```

**Output**
```
true
```

**Explanation**  
All 26 letters of the English alphabet appear at least once.

---

### Example 2

**Input**
```
s = "sdfs"
```

**Output**
```
false
```

**Explanation**  
Not all letters from `a` to `z` are present.

---

## Time Complexity

```
O(n)
```

We traverse the string once.

---

## Space Complexity

```
O(1)
```

We only use a fixed array of size 26.

---
