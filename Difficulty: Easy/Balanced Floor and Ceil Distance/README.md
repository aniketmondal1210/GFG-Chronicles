# Equal Distance to Floor and Ceil

## Problem Description

Given a sorted array `arr[]` and an integer `x`, determine if the absolute difference between `x` and its **floor** is equal to the absolute difference between `x` and its **ceil**.

- **Floor of `x`:** The largest element in the array that is less than or equal to `x`.
- **Ceil of `x`:** The smallest element in the array that is greater than or equal to `x`.

> **Note:** If `x` itself is present in the array, its floor and ceil will both equal `x`, making the absolute differences equal ($0 = 0$), so the result is `true`. If `x` lies strictly outside the range of elements in `arr[]` (i.e., `x` is smaller than `arr[0]` or larger than `arr[n-1]`), either the floor or ceil will not exist, making the answer `false`.

---

## Examples

### Example 1
- **Input:** `arr[] = [1, 2, 8, 10, 10, 12, 19]`, `x = 5`
- **Output:** `true`
- **Explanation:** 
  - Floor of `5` = `2`
  - Ceil of `5` = `8`
  - Distance to floor: $|5 - 2| = 3$
  - Distance to ceil: $|8 - 5| = 3$
  - Since distances are equal ($3 = 3$), output is `true`.

### Example 2
- **Input:** `arr[] = [1, 2, 5, 7, 8, 11, 12, 15]`, `x = 9`
- **Output:** `false`
- **Explanation:** 
  - Floor of `9` = `8`
  - Ceil of `9` = `11`
  - Distance to floor: $|9 - 8| = 1$
  - Distance to ceil: $|11 - 9| = 2$
  - Since distances are not equal ($1 
eq 2$), output is `false`.

### Example 3
- **Input:** `arr[] = [1, 2, 10]`, `x = 2`
- **Output:** `true`
- **Explanation:** `x = 2` is present in the array. Floor = `2`, Ceil = `2`. Both distances are $0$.

---

## Constraints

- $1 \le 	ext{arr.size()} \le 10^5$
- $0 \le 	ext{arr}[i] \le 10^6$
- $1 \le x \le 10^6$
- The array `arr[]` is sorted in non-decreasing order.

---

## Approach & Algorithm: Binary Search

Since the array is sorted, we can find both the **floor** and **ceil** efficiently in $\mathcal{O}(\log N)$ time using binary search.

1. **Find Floor:** Use binary search to find the maximum element $\le x$.
2. **Find Ceil:** Use binary search to find the minimum element $\ge x$.
3. **Edge Cases:**
   - If `x` is smaller than `arr[0]` (no floor exists), return `false`.
   - If `x` is larger than `arr[n-1]` (no ceil exists), return `false`.
4. **Comparison:** Check if $|x - 	ext{floor}| == |	ext{ceil} - x|$.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log N)$ — binary search to locate floor and ceil in a sorted array of size $N$.
- **Space Complexity:** $\mathcal{O}(1)$ — constant extra space.

---

## Code Implementations

### Python 3

```python
import bisect

def isFloorAndCeilEqualDist(arr: list[int], x: int) -> bool:
    n = len(arr)
    
    # Boundary checks: if x is out of bounds, either floor or ceil won't exist
    if x < arr[0] or x > arr[-1]:
        return False
        
    # Find floor (largest element <= x)
    idx_floor = bisect.bisect_right(arr, x) - 1
    floor_val = arr[idx_floor]
    
    # Find ceil (smallest element >= x)
    idx_ceil = bisect.bisect_left(arr, x)
    ceil_val = arr[idx_ceil]
    
    return (x - floor_val) == (ceil_val - x)

# Driver Code
if __name__ == "__main__":
    print(isFloorAndCeilEqualDist([1, 2, 8, 10, 10, 12, 19], 5))   # True
    print(isFloorAndCeilEqualDist([1, 2, 5, 7, 8, 11, 12, 15], 9))  # False
    print(isFloorAndCeilEqualDist([1, 2, 10], 2))                  # True
```

---

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

bool isFloorAndCeilEqualDist(const std::vector<int>& arr, int x) {
    if (x < arr.front() || x > arr.back()) {
        return false;
    }

    // Ceil: first element >= x
    auto ceilIt = std::lower_bound(arr.begin(), arr.end(), x);
    int ceilVal = *ceilIt;

    // Floor: largest element <= x
    auto floorIt = std::upper_bound(arr.begin(), arr.end(), x);
    --floorIt;
    int floorVal = *floorIt;

    return (x - floorVal) == (ceilVal - x);
}

int main() {
    std::cout << std::boolalpha;
    std::cout << isFloorAndCeilEqualDist({1, 2, 8, 10, 10, 12, 19}, 5) << std::endl;  // true
    std::cout << isFloorAndCeilEqualDist({1, 2, 5, 7, 8, 11, 12, 15}, 9) << std::endl; // false
    std::cout << isFloorAndCeilEqualDist({1, 2, 10}, 2) << std::endl;                 // true
    return 0;
}
```

---

### Java

```java
import java.util.Arrays;

public class FloorCeilEqualDistance {

    public static boolean isFloorAndCeilEqualDist(int[] arr, int x) {
        int n = arr.length;
        if (x < arr[0] || x > arr[n - 1]) {
            return false;
        }

        // Binary search to find floor and ceil
        int low = 0, high = n - 1;
        int floorVal = -1, ceilVal = -1;

        // Finding Floor
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] <= x) {
                floorVal = arr[mid];
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        // Finding Ceil
        low = 0;
        high = n - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] >= x) {
                ceilVal = arr[mid];
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return (x - floorVal) == (ceilVal - x);
    }

    public static void main(String[] args) {
        System.out.println(isFloorAndCeilEqualDist(new int[]{1, 2, 8, 10, 10, 12, 19}, 5));   // true
        System.out.println(isFloorAndCeilEqualDist(new int[]{1, 2, 5, 7, 8, 11, 12, 15}, 9));  // false
        System.out.println(isFloorAndCeilEqualDist(new int[]{1, 2, 10}, 2));                  // true
    }
}
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
