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

## Constraints

- `1 ≤ |a|, |b| ≤ 10^5`
