# Find the Missing Element After Shuffling and Removing One

## Problem Statement

You are given two integer arrays `arr1` and `arr2`.

- `arr2` is formed by shuffling all elements of `arr1` and removing **one** element.
- You need to find and return the **missing element**.

You must solve this in **O(n)** time and **O(1)** extra space.

---

## Example 1

**Input:**
arr1 = [4, 8, 1, 3, 7]
arr2 = [7, 4, 3, 1]

**Output:**

8

Explanation:
The number 8 is missing from arr2.

## Example 2

**Input:**

arr1 = [12, 10, 15, 23, 11, 30]
arr2 = [15, 12, 23, 11, 30]

**Output:**

10

Explanation:
10 is not present in arr2.

## Constraints

- 2 <= arr1.length <= 10^6
- arr2.length = arr1.length - 1
- 1 <= arr[i] <= 10^6
