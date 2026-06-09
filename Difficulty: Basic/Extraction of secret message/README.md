# Extract Secret Message

## Problem

Given an encoded string `S`, remove every occurrence of the substring:

```text
"LIE"
```

and return the remaining secret message.

---

## Examples

### Example 1

**Input**

```text
S = "LIEILIEAMLIELIECOOL"
```

**Output**

```text
"I AM COOL"
```

**Explanation**

Removing all occurrences of `"LIE"`:

```text
LIE I LIE AM LIE LIE COOL
```

Remaining string:

```text
I AM COOL
```

---

### Example 2

**Input**

```text
S = "LIELIEALIEBCLIE"
```

**Output**

```text
"A BC"
```

---

## Your Task:  
You don't need to read input or print anything. Your task is to complete the function ExtractMessage() which accepts a string as input parameter and returns a string containing secret message.

## Expected Time Complexity: O(N)
## Expected Auxiliary Space: O(N)

## Constraints:

- 1 ≤ N ≤ 10^6
- String contains only Upper Case Letters.

---
