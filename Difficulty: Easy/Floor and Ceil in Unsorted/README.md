# Floor and Ceil in an Unsorted Array

## Problem Description

Given an unsorted array `arr[]` of integers and an integer `x`, find the **floor** and **ceil** of `x` in `arr[]`.

- **Floor of x:** The largest element in `arr[]` that is smaller than or equal to `x`. If no such element exists, the floor is `-1`.
- **Ceil of x:** The smallest element in `arr[]` that is greater than or equal to `x`. If no such element exists, the ceil is `-1`.

Return an array/list of two integers representing `[floor, ceil]`.

---

## Examples

### Example 1
- **Input:** `x = 7`, `arr[] = [5, 6, 8, 9, 6, 5, 5, 6]`
- **Output:** `[6, 8]`
- **Explanation:** Floor of $7$ is $6$ (largest value $\le 7$), and ceil of $7$ is $8$ (smallest value $\ge 7$).

### Example 2
- **Input:** `x = 10`, `arr[] = [5, 6, 8, 8, 6, 5, 5, 6]`
- **Output:** `[8, -1]`
- **Explanation:** Floor of $10$ is $8$, but there is no element $\ge 10$, so ceil is `-1`.

---

## Constraints

- $1 \le \text{arr.size} \le 10^5$
- $1 \le \text{arr}[i], x \le 10^6$

---

## Approach: Single Pass Linear Scan

Since the array is **unsorted**, we can find both floor and ceil in a single traversal:

1. Initialize `floor = -1` and `ceil = -1`.
2. Iterate through each element `num` in `arr`:
   - If `num <= x` and (`floor == -1` or `num > floor`), update `floor = num`.
   - If `num >= x` and (`ceil == -1` or `num < ceil`), update `ceil = num`.
3. Return `[floor, ceil]`.

This avoids sorting the array, keeping time complexity at $\mathcal{O}(n)$.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$ — Requires traversing the array once.
- **Space Complexity:** $\mathcal{O}(1)$ — Constant extra space.

---

## Code Implementations

### Python 3

```python
def getFloorAndCeil(x: int, arr: list[int]) -> list[int]:
    floor = -1
    ceil = -1
    
    for num in arr:
        if num <= x:
            if floor == -1 or num > floor:
                floor = num
        if num >= x:
            if ceil == -1 or num < ceil:
                ceil = num
                
    return [floor, ceil]

# Driver Code
if __name__ == "__main__":
    print(getFloorAndCeil(7, [5, 6, 8, 9, 6, 5, 5, 6]))   # Output: [6, 8]
    print(getFloorAndCeil(10, [5, 6, 8, 8, 6, 5, 5, 6]))  # Output: [8, -1]
```

---

### C++

```cpp
#include <iostream>
#include <vector>

std::vector<int> getFloorAndCeil(int x, const std::vector<int>& arr) {
    int floorVal = -1;
    int ceilVal = -1;
    
    for (int num : arr) {
        if (num <= x) {
            if (floorVal == -1 || num > floorVal) {
                floorVal = num;
            }
        }
        if (num >= x) {
            if (ceilVal == -1 || num < ceilVal) {
                ceilVal = num;
            }
        }
    }
    
    return {floorVal, ceilVal};
}

int main() {
    std::vector<int> arr1 = {5, 6, 8, 9, 6, 5, 5, 6};
    std::vector<int> res1 = getFloorAndCeil(7, arr1);
    std::cout << "[" << res1[0] << ", " << res1[1] << "]" << std::endl; // [6, 8]

    std::vector<int> arr2 = {5, 6, 8, 8, 6, 5, 5, 6};
    std::vector<int> res2 = getFloorAndCeil(10, arr2);
    std::cout << "[" << res2[0] << ", " << res2[1] << "]" << std::endl; // [8, -1]

    return 0;
}
```

---

### Java

```java
import java.util.Arrays;

public class FloorAndCeil {

    public static int[] getFloorAndCeil(int x, int[] arr) {
        int floorVal = -1;
        int ceilVal = -1;

        for (int num : arr) {
            if (num <= x) {
                if (floorVal == -1 || num > floorVal) {
                    floorVal = num;
                }
            }
            if (num >= x) {
                if (ceilVal == -1 || num < ceilVal) {
                    ceilVal = num;
                }
            }
        }

        return new int[]{floorVal, ceilVal};
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(getFloorAndCeil(7, new int[]{5, 6, 8, 9, 6, 5, 5, 6})));  // [6, 8]
        System.out.println(Arrays.toString(getFloorAndCeil(10, new int[]{5, 6, 8, 8, 6, 5, 5, 6}))); // [8, -1]
    }
}
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
