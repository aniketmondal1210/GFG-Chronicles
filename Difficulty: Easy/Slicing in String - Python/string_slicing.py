#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# Function to join given bound_by and tag_name
def join_middle(bound_by, tag_name):
    # Return the string with tag_name inserted in the middle of bound_by
    return bound_by[0:len(bound_by)//2] + tag_name + bound_by[len(bound_by)//2:]

#{
 # Driver Code Starts
# Driver Code
def main():
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while testcases > 0:
        string = input().split()
        bound_by = string[0]
        tag_name = string[1]
        testcases -= 1
        print(join_middle(bound_by, tag_name))

# Entry point
if __name__ == "__main__":
    main()
