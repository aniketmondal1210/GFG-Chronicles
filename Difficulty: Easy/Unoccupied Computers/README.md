# Cafe Computer Assignment

## Problem

A cafe has `n` computers. Customer events are represented by a string `s` of uppercase English letters.

Each distinct letter appears exactly twice:

- The **first occurrence** represents the customer's arrival.
- The **second occurrence** represents the customer's departure.

A customer gets a computer only if one is available when they arrive. Otherwise, the customer is rejected and does not use a computer.

Return the number of customers who could not be assigned a computer upon arrival.

## Examples

### Example 1

```text
Input: n = 3, s = "GACCBDDBAGEE"
Output: 1
```

**Explanation:**

Only customer `D` cannot get a computer.

### Example 2

```text
Input: n = 1, s = "ABCBAC"
Output: 2
```

**Explanation:**

Customers `B` and `C` cannot get computers.

## Constraints

```text
1 <= n <= 26
1 <= |s| <= 52
```

- `s` consists of uppercase English letters.
- Each letter occurs exactly twice.

## Approach

We need to track three things:

1. Which customers are currently using a computer.
2. Which customers were rejected.
3. How many computers are currently occupied.

For every character in the string:

- If it is the **first occurrence** of the customer:
  - If a computer is available, assign one.
  - Otherwise, mark the customer as rejected.
- If it is the **second occurrence**:
  - If the customer was using a computer, free that computer.
  - If the customer was rejected, they never occupied a computer, so nothing needs to be freed.

A simple set can be used to keep track of customers currently using computers.

## Python Solution

```python
def count_rejected_customers(n, s):
    using = set()
    rejected = set()

    for customer in s:
        if customer in using:
            # Customer is leaving and frees a computer.
            using.remove(customer)

        elif customer in rejected:
            # Rejected customer is leaving.
            rejected.remove(customer)

        elif len(using) < n:
            # A computer is available.
            using.add(customer)

        else:
            # No computer is available.
            rejected.add(customer)

    return len(rejected)
```

## Walkthrough

For:

```text
n = 3
s = "GACCBDDBAGEE"
```

The cafe has 3 computers.

- `G` arrives → computer assigned.
- `A` arrives → computer assigned.
- `C` arrives → computer assigned.
- `C` leaves → computer becomes free.
- `B` arrives → computer assigned.
- `D` arrives → all 3 computers are occupied, so `D` is rejected.
- `D` leaves → `D` never had a computer.
- `B` leaves → computer becomes free.
- `A` leaves.
- `G` leaves.
- `E` arrives → computer assigned.
- `E` leaves.

Only `D` was rejected.

```text
Answer = 1
```

## Why the Set Works

The `using` set contains exactly the customers who currently occupy computers.

Therefore:

```python
len(using)
```

is the number of occupied computers.

Before assigning a new customer, we check:

```python
len(using) < n
```

If true, a computer is available.

If false, all computers are occupied and the customer is rejected.

## Complexity

Let `m = len(s)`.

- **Time:** `O(m)` average case
- **Space:** `O(m)`

Since `|s| <= 52`, this is easily efficient enough.

## Key Takeaway

The main idea is to simulate the customer arrivals and departures.

```text
Arrival + computer available  → assign computer
Arrival + no computer        → reject customer
Departure + assigned         → free computer
Departure + rejected         → do nothing
```

Using a set makes checking and updating customer status efficient.
