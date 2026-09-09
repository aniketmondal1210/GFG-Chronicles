# Good String Verification (Cyclic Alphabet Distance)

## Problem Description

Given a string `s`, determine if it is **good**. 

A string is considered **good** if the **cyclic distance** between every pair of adjacent characters is **exactly 1**.

- The **cyclic distance** between two lowercase English letters is the shortest distance between them in a circular alphabet arrangement ('a' through 'z').
  - For example, distance between `'a'` and `'c'` is 2, and distance between `'a'` and `'y'` is 2.
  - Wrap-around distance between `'z'` and `'a'` is 1.
- A string of length 1 is **always** considered good.

---

## Examples

### Example 1
- **Input:** `s = "aaa"`
- **Output:** `false`
- **Explanation:** The distance between adjacent `'a'` and `'a'` is $0$, which is not $1$.

### Example 2
- **Input:** `s = "cbc"`
- **Output:** `true`
- **Explanation:** 
  - Distance between `'c'` and `'b'` is $1$.
  - Distance between `'b'` and `'c'` is $1$.
  - All adjacent pairs have a cyclic distance of $1$.

---

## Constraints

- $1 \le 	ext{s.size()} \le 10^5$
- `s` consists of only lowercase English letters.

---

## Formula & Strategy

For any two adjacent characters $c_1$ and $c_2$:

$$	ext{diff} = | 	ext{ord}(c_1) - 	ext{ord}(c_2) |$$
$$	ext{cyclic\_distance} = \min(	ext{diff}, 26 - 	ext{diff})$$

A string is valid if and only if $	ext{cyclic\_distance} == 1$ for all adjacent pairs $(s[i], s[i+1])$.

### Valid Adjacent Pairs Matrix
Adjacent characters must satisfy one of the following:
1. $c_2 = c_1 + 1$ (e.g., `'a' ightarrow 'b'`)
2. $c_2 = c_1 - 1$ (e.g., `'b' ightarrow 'a'`)
3. **Wrap-around:** `'a' \leftrightarrow 'z'`

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$ — single pass over the string of length $n$.
- **Space Complexity:** $\mathcal{O}(1)$ — constant auxiliary memory.

---

## Code Implementations

### Python 3

```python
def isGoodString(s: str) -> bool:
    if len(s) <= 1:
        return True
        
    for i in range(len(s) - 1):
        diff = abs(ord(s[i]) - ord(s[i + 1]))
        cyclic_dist = min(diff, 26 - diff)
        
        if cyclic_dist != 1:
            return False
            
    return True

# Driver Code
if __name__ == "__main__":
    print(isGoodString("aaa"))  # False
    print(isGoodString("cbc"))  # True
    print(isGoodString("za"))   # True
```

---

### C++

```cpp
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

bool isGoodString(const std::string& s) {
    if (s.length() <= 1) return true;

    for (size_t i = 0; i < s.length() - 1; ++i) {
        int diff = std::abs(s[i] - s[i + 1]);
        int cyclic_dist = std::min(diff, 26 - diff);

        if (cyclic_dist != 1) {
            return false;
        }
    }
    return true;
}

int main() {
    std::cout << std::boolalpha;
    std::cout << isGoodString("aaa") << std::endl; // false
    std::cout << isGoodString("cbc") << std::endl; // true
    std::cout << isGoodString("za") << std::endl;  // true
    return 0;
}
```

---

### Java

```java
public class GoodString {

    public static boolean isGoodString(String s) {
        if (s.length() <= 1) return true;

        for (int i = 0; i < s.length() - 1; i++) {
            int diff = Math.abs(s.charAt(i) - s.charAt(i + 1));
            int cyclicDist = Math.min(diff, 26 - diff);

            if (cyclicDist != 1) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isGoodString("aaa")); // false
        System.out.println(isGoodString("cbc")); // true
        System.out.println(isGoodString("za"));  // true
    }
}
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
