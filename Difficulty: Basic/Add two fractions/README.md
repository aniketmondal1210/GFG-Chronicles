# Program to Add Two Fractions and Express in Simplified Form

## Problem Description

Given four integers `num1`, `den1`, `num2`, and `den2`, representing two fractions $\frac{\text{num1}}{\text{den1}}$ and $\frac{\text{num2}}{\text{den2}}$, write a program to find their sum and return the resulting fraction in its **simplest (reduced) form**.

### Output Format
Return the answer as an array/list of two integers:
1. **Numerator** of the resulting fraction.
2. **Denominator** of the resulting fraction.

---

## Examples

### Example 1
- **Input:** `num1 = 1`, `den1 = 500`, `num2 = 2`, `den2 = 500`
- **Output:** `[3, 500]`
- **Explanation:** 
  $$\frac{1}{500} + \frac{2}{500} = \frac{1 + 2}{500} = \frac{3}{500}$$

### Example 2
- **Input:** `num1 = 1`, `den1 = 6`, `num2 = 1`, `den2 = 3`
- **Output:** `[1, 2]`
- **Explanation:** 
  $$\frac{1}{6} + \frac{1}{3} = \frac{1}{6} + \frac{2}{6} = \frac{3}{6} = \frac{1}{2}$$

---

## Constraints

- $1 \le \text{num1}, \text{den1}, \text{num2}, \text{den2} \le 10^4$

---

## Approach & Algorithm

1. **Find a Common Denominator:**
   Compute the cross-multiplied numerator and common denominator:
   $$\text{res\_num} = (\text{num1} \times \text{den2}) + (\text{num2} \times \text{den1})$$
   $$\text{res\_den} = \text{den1} \times \text{den2}$$

2. **Simplify the Fraction:**
   Find the **Greatest Common Divisor (GCD)** of `res_num` and `res_den` using Euclid's Algorithm.
   $$\text{common\_gcd} = \text{gcd}(\text{res\_num}, \text{res\_den})$$

3. **Divide by GCD:**
   Divide both the numerator and denominator by `common_gcd`:
   $$\text{simplified\_num} = \frac{\text{res\_num}}{\text{common\_gcd}}$$
   $$\text{simplified\_den} = \frac{\text{res\_den}}{\text{common\_gcd}}$$

4. **Return:**
   Return `[simplified_num, simplified_den]`.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log(\min(\text{res\_num}, \text{res\_den})))$ — due to the GCD computation via the Euclidean algorithm.
- **Space Complexity:** $\mathcal{O}(1)$ — constant space as only integer variables are used.

---

## Code Implementations

### Python 3

```python
import math

def addFraction(num1: int, den1: int, num2: int, den2: int) -> list[int]:
    # Calculate combined numerator and denominator
    res_num = num1 * den2 + num2 * den1
    res_den = den1 * den2
    
    # Find Greatest Common Divisor (GCD)
    common_gcd = math.gcd(res_num, res_den)
    
    # Simplify fraction
    return [res_num // common_gcd, res_den // common_gcd]

# Driver Code Example
if __name__ == "__main__":
    print(addFraction(1, 500, 2, 500))  # Output: [3, 500]
    print(addFraction(1, 6, 1, 3))      # Output: [1, 2]
```

---

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric> // for std::gcd

std::vector<int> addFraction(int num1, int den1, int num2, int den2) {
    int res_num = num1 * den2 + num2 * den1;
    int res_den = den1 * den2;
    
    int common_gcd = std::gcd(res_num, res_den);
    
    return {res_num / common_gcd, res_den / common_gcd};
}

int main() {
    std::vector<int> ans1 = addFraction(1, 500, 2, 500);
    std::cout << "[" << ans1[0] << ", " << ans1[1] << "]" << std::endl; // [3, 500]

    std::vector<int> ans2 = addFraction(1, 6, 1, 3);
    std::cout << "[" << ans2[0] << ", " << ans2[1] << "]" << std::endl; // [1, 2]

    return 0;
}
```

---

### Java

```java
import java.util.Arrays;

public class FractionAddition {

    // Helper method to compute GCD
    private static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    public static int[] addFraction(int num1, int den1, int num2, int den2) {
        int resNum = num1 * den2 + num2 * den1;
        int resDen = den1 * den2;

        int commonGcd = gcd(resNum, resDen);

        return new int[]{resNum / commonGcd, resDen / commonGcd};
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(addFraction(1, 500, 2, 500))); // [3, 500]
        System.out.println(Arrays.toString(addFraction(1, 6, 1, 3)));     // [1, 2]
    }
}
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
