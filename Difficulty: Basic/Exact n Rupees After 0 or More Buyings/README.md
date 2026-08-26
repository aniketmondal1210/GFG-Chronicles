# Geek and Chocolates

## Problem

Given an integer `n`, determine whether Geek can have **exactly `n` rupees** after buying **0 or more chocolates** from a shop.

- Geek initially has **100 rupees**.
- The shop sells two types of chocolates costing **3** rupees and **7** rupees.
- Geek can buy any number of chocolates, including zero chocolates.

Return `true` if it is possible to have exactly `n` rupees remaining; otherwise, return `false`.

### Example 1

**Input:**
```text
n = 99
```

**Output:**
```text
false
```

**Explanation:**

Geek starts with 100 rupees, so he needs to spend:

```text
100 - 99 = 1
```

No combination of chocolates costing 3 and 7 rupees can total 1 rupee. Therefore, the answer is `false`.

### Example 2

**Input:**
```text
n = 97
```

**Output:**
```text
true
```

**Explanation:**

Geek needs to spend:

```text
100 - 97 = 3
```

He can buy one chocolate costing 3 rupees, leaving exactly 97 rupees.

---

## Approach

First calculate how much money Geek needs to spend:

```text
amount = 100 - n
```

Now we need to check whether `amount` can be represented as:

```text
3 × x + 7 × y
```

where `x` and `y` are non-negative integers.

Because `n` is at most 100, we can simply try every possible number of 3-rupee chocolates and check whether the remaining amount is divisible by 7.

### Example

For:

```text
n = 88
```

Geek needs to spend:

```text
100 - 88 = 12
```

We can buy four 3-rupee chocolates:

```text
3 + 3 + 3 + 3 = 12
```

Therefore, the answer is `true`.

---

## Java Solution

```java
class Solution {
    public boolean canHave(int n) {
        int amount = 100 - n;

        for (int i = 0; i * 3 <= amount; i++) {
            int remaining = amount - (i * 3);

            if (remaining % 7 == 0) {
                return true;
            }
        }

        return false;
    }
}
```

---

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

Since `0 <= n <= 100`, the loop runs only a small number of times.

---

## Key Idea

> Convert the problem into finding whether `100 - n` can be formed using only 3-rupee and 7-rupee chocolates.

If it can, return `true`; otherwise, return `false`.
