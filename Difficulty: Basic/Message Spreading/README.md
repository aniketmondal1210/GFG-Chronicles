# Message Spreading (Minimum Messages to Share All Stories)

## Problem Description

There are `n` students in a class, each initially possessing a distinct funny story. Students share stories by sending electronic messages under the following rules:
- A sender includes **all** funny stories they know at the moment the message is sent.
- Each message has **only one** recipient (one-way communication).

Find the minimum number of messages required to guarantee that every student knows all `n` funny stories.

---

## Examples

### Example 1
- **Input:** `n = 2`
- **Output:** `2`
- **Explanation:** Student 1 sends a message to Student 2, and Student 2 sends a message back to Student 1, requiring `2` messages in total.

### Example 2
- **Input:** `n = 1`
- **Output:** `0`
- **Explanation:** With only one student, everyone already knows all stories, so `0` messages are needed.

---

## Constraints

- $1 \le n \le 10^5$

---
