# Check if One String Can Be Formed from Another

## Problem

Given two strings `a` and `b`, determine whether `a` can be formed from `b` by deleting some characters from `b` and rearranging the remaining characters.

Return `true` if possible; otherwise, return `false`.

A string `a` can be formed from `b` if `b` contains every character required by `a` with at least the same frequency.

## Examples

### Example 1

```text
Input:
a = "GeeksforGeeks"
b = "rteksfoGrdsskGeggehes"

Output:
true
```

**Explanation:**  
Delete the extra characters from `b` and rearrange the remaining characters. Since `b` contains every character required to form `"GeeksforGeeks"` with the required frequencies, `a` can be formed.

### Example 2

```text
Input:
a = "Hello"
b = "Geek"

Output:
false
```

**Explanation:**  
Even after deleting characters and rearranging the remaining ones, `b` does not contain enough required characters, such as two `'l'`s and one `'o'`, to form `"Hello"`.

## Approach

Since the order of characters does not matter, count the frequency of each character.

1. Count the frequency of every character in `b`.
2. Traverse `a`.
3. For each character in `a`, check whether `b` contains an unused occurrence.
4. If a required character is unavailable, return `false`.
5. If all characters in `a` can be matched, return `true`.

## Algorithm

```text
Create a frequency map for characters in b.

For every character c in a:
    If frequency[c] == 0:
        return false
    Decrease frequency[c] by 1

Return true
```

## Complexity

- **Time Complexity:** `O(|a| + |b|)`
- **Space Complexity:** `O(k)`, where `k` is the number of distinct characters.

## Constraints

- `1 ≤ |a|, |b| ≤ 10^5`
