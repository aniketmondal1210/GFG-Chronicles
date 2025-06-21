# Binary to Decimal Conversion

Given a string `b` representing a binary number, return its **decimal equivalent**.

## Input
- `b`: A string of '0' and '1' characters representing a binary number.

## Output
- An integer representing the decimal equivalent of the binary string.

## Example 1
```
Input: b = "111"
Output: 7

Explanation:
2^2 + 2^1 + 2^0 = 4 + 2 + 1 = 7
```

## Example 2
```
Input: b = "1010"
Output: 10

Explanation:
2^3 + 2^1 = 8 + 2 = 10
```

## Example 3
```
Input: b = "100001"
Output: 33

Explanation:
2^5 + 2^0 = 32 + 1 = 33
```

## Constraints
- `1 <= number of bits in binary number <= 16`
- The input string contains only '0' or '1' characters.
