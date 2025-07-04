#User function Template for python3
def find_minimum(a, b):
    # Your code here 
    # Return the minimum of all the valid operations
    p = a+b
    q = a-b
    r = a*b
    if b == 0:
        return min(p,min(q,r))
    else:
        s = a//b
        return min(p,min(q,min(r,s)))
