# Highest Frequency Word

## Problem Statement

You are given a string `s` that is made up of words separated by spaces.

Find the word with the highest frequency, meaning the word that appears the most times in the sentence.

If multiple words have the same maximum frequency, return the word that occurs first in the sentence.

Return the word along with its frequency in the following format:

```text
word frequency
```

---

## Example 1

**Input:**

```text
s = "the devil in the sky the"
```

**Output:**

```text
the 2
```

**Explanation:**

The word `"the"` appears 2 times, which is the highest frequency.

Therefore, the answer is:

```text
the 2
```

---

## Example 2

**Input:**

```text
s = "this is not right"
```

**Output:**

```text
this 1
```

**Explanation:**

Every word appears exactly once.

Since `"this"` occurs first in the sentence, it is returned along with its frequency:

```text
this 1
```

## Constraints

```text
1 <= s.size() <= 10^6
```
