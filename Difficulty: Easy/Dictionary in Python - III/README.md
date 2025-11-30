# Dictionary Operations in Python

## Introduction
Python dictionaries allow efficient insertion, deletion, and retrieval of key–value pairs.  
This problem focuses on performing specific dictionary operations based on user commands.

We also explore examples of:

- **Dictionary formatting**
- **Deleting key–value pairs**
- **Performing operations using commands**

---

## Dictionary Formatting Example

hash = {}
hash['Geeks'] = 5
hash['geeksforgeeks'] = 13
key = 'Geeks'

s = "Count of characters is " + str(hash[key]) + " in " + key
# Output: Count of characters is 5 in Geeks

Note: Use str() when concatenating numbers with strings.
Dictionary Deletion Example

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

del dict['c']
# Removes the key 'c' and its value

Problem Description

You are given a list of student names and their corresponding marks.
You must process queries to insert, delete, or print dictionary entries.
Operations
1. i key value

Insert the key and value into the dictionary.
Print:

Inserted

2. d key

Delete the key from the dictionary.

    If the key exists:

Deleted

Otherwise:

    -1

3. p key

Print marks of the given key in this format:

Marks of key is value

If the key does not exist:

-1

Example
Input

N = 5
i geeks 100
i for 200
d geeks
i geeks 300
p geeks

Output

Inserted
Inserted
Deleted
Inserted
Marks of geeks is 300

Explanation

    First two commands insert → "Inserted"

    Third command deletes → "Deleted"

    Fourth command inserts again → "Inserted"

    Last command prints marks → "Marks of geeks is 300"

Functions to Implement

You must complete the following functions:

    insert_dict(dictionary, key, value)

    del_dict(dictionary, key)

    print_dict(dictionary, key)

## Constraints

- 1 ≤ N ≤ 10⁴
- 1 ≤ marks ≤ 10⁴

---
