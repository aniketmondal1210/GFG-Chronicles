# Print Variables in Different Formats

## Problem Statement

You are given two variables `a` and `b`. Your task is to print these variables in the following formats:

1. **With space**: Print `a` and `b` in a single line, separated by a space, followed by a newline.  
2. **Without newline**: Print `a` and `b` separated by a space, but do not end the output with a newline.  
3. **With separator**: Print `a` and `b` separated by a specified separator, followed by a newline.  
4. **Without space**: Print `a` and `b` in a single line, with no spaces between them, followed by a newline.  

---

## Examples

### Example 1

**Input:**  
`a = "Hello"`  
`b = "World"`  
`separator = '&'`  

**Output:**  
Hello World
Hello WorldHello&World
HelloWorld


**Explanation:**  
- `Hello World` → printed with space and newline.  
- `Hello World` (again) → printed without newline, followed by `Hello&World` with separator and newline.  
- `HelloWorld` → printed without space between variables.

---

## Constraints

- 1 ≤ length of `a`, `b` ≤ 100  
- `a` and `b` contain only printable ASCII characters  
- `separator` is a single printable ASCII character
