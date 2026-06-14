# String Exists with Exactly One Character Different

## Problem

Given a string `S` and an array of strings `arr[]`, determine whether there exists a string in the array that differs from `S` by **exactly one character**.

### Conditions

- The two strings must have the **same length**.
- Exactly **one position** should contain different characters.
- Return `"True"` if such a string exists; otherwise return `"False"`.

---

## Examples

### Example 1

**Input**

```text
N = 4
arr[] = {"bana", "apple", "banaba", "bonanzo"}
S = "banana"
```

**Output**

```text
True
```

**Explanation**

```text
"banaba" and "banana" have the same length.

banana
banaba
     ^
Only one character differs ('n' and 'b').
```

Therefore, the answer is `"True"`.

---

### Example 2

**Input**

```text
N = 4
arr[] = {"bana", "apple", "banaba", "bonanzo"}
S = "apple"
```

**Output**

```text
False
```

**Explanation**

```text
No string in the array differs from "apple"
by exactly one character.
```

---

##  Your Task: 
You don't need to read input or print anything. Your task is to complete the function isStringExist() which takes the string array arr[], its size N and a string S as input parameters and returns "True" if a string exists in arr which has only one character different from S else return "False".

 

## Expected Time Complexity: O(N*Length of the string S)

## Expected Space Complexity: O(1)

 

## Constraints :

- 1 ≤ N ≤ 100
- 1 ≤| arr[i] | ≤ 1000
- 1 ≤| S | ≤ 1000

---
