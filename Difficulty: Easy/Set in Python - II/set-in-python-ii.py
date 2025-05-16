#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

# Function to find common elements in sets
# should return the intersection of sets
def common_in_set(a, b):
    # Your code here
    set_a = set(a)
    set_b = set(b)
    int_set = set_a.intersection(set_b)
    return int_set

# Function to find difference in sets
# Should return the difference in sets
def diff(a, b):
    # Your code here
    set_a = set(a)
    set_b = set(b)
    set_diff = set_a - set_b
    return set_diff

# Function to find union of sets
# Should return the union of sets
def all_in_set(a, b):
    # Your code here
    set_a = set(a)
    set_b = set(b)
    union_set = set_a.union(set_b)
    return union_set
    

#{ 
 # Driver Code Starts.

# Driver code
def main():
    testcase = int(input())
    
    # looping through all testcases
    while testcase > 0:
        
        # taking input of set
        a = {int(x) for x in input().split()}
        b = {int(x) for x in input().split()}
        
        for x in all_in_set(a, b):
            print (x, end = ' ')
            
        print ()
        
        for x in common_in_set(a, b):
            print (x, end = ' ')
            
        print ()
        
        for x in diff(a, b):
            print (x, end = ' ')
        
        print ()
        
        testcase -= 1

        print("~")
if __name__ == '__main__':
    main()
# } Driver Code Ends