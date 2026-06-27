# Army Battle Winner

## Problem

Two armies, **A** and **B**, have the same number of soldiers.

The power of the soldiers is given by two arrays:

- `arr1[]` → Army A
- `arr2[]` → Army B

The `i`-th soldier of Army A fights only the `i`-th soldier of Army B.

Battle rules:

- If `arr1[i] > arr2[i]`, Army **A** wins that battle.
- If `arr1[i] < arr2[i]`, Army **B** wins that battle.
- If `arr1[i] == arr2[i]`, neither army gets a point.

Return:

- `"A"` if Army A wins more battles.
- `"B"` if Army B wins more battles.
- `"DRAW"` if both armies win the same number of battles.

---

## Example 1

### Input

```text
arr1 = [2, 2]
arr2 = [5, 5]
```

### Output

```text
"B"
```

### Explanation

Battle 1:

```text
2 < 5 → Army B wins
```

Battle 2:

```text
2 < 5 → Army B wins
```

Wins:

```text
Army A = 0
Army B = 2
```

Hence, the winner is:

```text
"B"
```

---

## Example 2

### Input

```text
arr1 = [9]
arr2 = [8]
```

### Output

```text
"A"
```

### Explanation

```text
9 > 8
```

Army A wins the only battle.

---

## Constraints:

- 1 ≤ arr1.size() ≤ 10^6
- 0 ≤ arr1[i],arr2[i] ≤ 10^5

---
