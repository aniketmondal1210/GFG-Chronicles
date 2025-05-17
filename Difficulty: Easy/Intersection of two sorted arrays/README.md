# Problem: Intersection of Two Sorted Arrays

## Description
Given two sorted arrays `arr1[]` and `arr2[]`. Your task is to return the intersection of both arrays.

Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.

**Note:** If there is no intersection then return an empty array.

## Examples

```text
Input: arr1[] = [1, 2, 3, 4], arr2[] = [2, 4, 6, 7, 8]
Output: [2, 4]
Explanation: 2 and 4 are only common elements in both the arrays.

Input: arr1[] = [1, 2, 2, 3, 4], arr2[] = [2, 2, 4, 6, 7, 8]
Output: [2, 4]
Explanation: 2 and 4 are the only common elements.

Input: arr1[] = [1, 2], arr2[] = [3, 4]
Output: []
Explanation: No common elements.
```

## Constraints
```text
Expected Time Complexity: O(n + m)
Expected Auxiliary Space: O(min(n,m))

1 <= arr1.size(), arr2.size() <= 10^5
1 <= arr1[i], arr2[i] <= 10^6
```
