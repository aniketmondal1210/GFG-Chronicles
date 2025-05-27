# Reverse Words in a String

## Problem Statement

Given a string `s`, reverse the order of words in the string without reversing the characters of individual words.

- Words are separated by **one or more spaces**.
- The output string should contain **no leading or trailing spaces**, and **only one space** should separate each word.

## Examples

### Example 1:
**Input:**  
`s = " i like this program very much "`  
**Output:**  
`"much very program this like i"`  
**Explanation:**  
After trimming extra spaces and reversing the word order, the result is `"much very program this like i"`.

---

### Example 2:
**Input:**  
`s = " pqr mno "`  
**Output:**  
`"mno pqr"`  
**Explanation:**  
Trim spaces and reverse the words to get `"mno pqr"`.

---

### Example 3:
**Input:**  
`s = " a "`  
**Output:**  
`"a"`  
**Explanation:**  
Only one word present, so output is just `"a"`.

## Constraints

- `1 <= s.length <= 10^6`
- The string `s` contains **only lowercase English alphabets and spaces**.
