# Problem: Highest Frequency Word

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

---

## Approach

Use a frequency map to count the occurrences of every word.

1. Split the sentence into individual words.
2. Count the frequency of each word using a hash map.
3. Traverse the words in their original order.
4. Keep track of the word with the highest frequency.
5. If two words have the same frequency, keep the one that appeared earlier.
6. Return the word and its frequency.

---

## Complexity

### Time Complexity

```text
O(n)
```

where `n` is the length of the string.

### Auxiliary Space

```text
O(n)
```

for storing the frequency of the words.

---

## Constraints

```text
1 <= s.size() <= 10^6
```
