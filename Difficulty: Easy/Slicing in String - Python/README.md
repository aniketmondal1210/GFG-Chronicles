# Slicing and String Manipulation

## Problem Statement

Here we'll talk about the novel and perhaps tantalizing concept of slicing.  
Slicing is the process through which you can extract some continuous part of a string.  
For example, if the string is `"python"`, slicing can be done as:

a. `string[0:2] = py` (Slicing till index 1)  
b. `string[0:] = python` (Slicing till last index)  
c. `string[0:4] = pyth` (Slicing till index 3)  
d. `string[0:-2] = pyth` (Slicing till index -3)  

**Note**: -1 indexing starts from the last of any string.

## Problem

Given a string of braces named `bound_by`, and a string named `tag_name`.  
The task is to print a new string such that `tag_name` is in the middle of `bound_by`.

## Examples

### Example 1:
Input:  
bound_by = `[[ ]]`, tag_name = `tag`  
Output:  
`[[tag]]`

### Example 2:
Input:  
bound_by = `<>`, tag_name = `body`  
Output:  
`<body>`

## Your Task

Your task is to complete the function `join_middle()` which should return the modified string.

## Constraints

- 1 <= |tag_name| <= 10³
