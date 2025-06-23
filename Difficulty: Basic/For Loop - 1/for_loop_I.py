#User function Template for python3
n = int(input())
for i in range(1,11):
    print(n*i,end = " ")
# Your code here



OR



#User function Template for python3
def utility():
    n = int(input())
    ## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11):  ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i * n, end=" ")  ## Separating by spaces using end =" "
