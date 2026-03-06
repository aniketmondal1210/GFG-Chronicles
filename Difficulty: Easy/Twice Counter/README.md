# Count Words That Appear Exactly Twice

## Problem Statement

Given a list of **N words**, count how many words **appear exactly twice** in the list.

Return the **number of such words**.

---

## Examples

### Example 1

**Input**
```
N = 3
list = {Geeks, For, Geeks}
```

**Output**
```
1
```

**Explanation**

- `Geeks` appears **2 times**
- `For` appears **1 time**

So, only **1 word** appears exactly twice.

---

### Example 2

**Input**
```
N = 8
list = {Tom, Jerry, Thomas, Tom, Jerry, Courage, Tom, Courage}
```

**Output**
```
2
```

**Explanation**

Word frequencies:

```
Tom → 3
Jerry → 2
Thomas → 1
Courage → 2
```

Words appearing **exactly twice**:

```
Jerry
Courage
```

Total = **2**

---

## Time Complexity

```
O(N)
```

- One pass to count frequencies.
- One pass through the map.

---

## Space Complexity

```
O(N)
```

- For storing frequencies in the hash map.

---

## Constraints:

- 1<= N <= 10^4

---
