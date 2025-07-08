import math
#User function Template for python3
n = int(input())
# Your code here
if n < 2:
    print("False")
else:
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            print("False")
            break
    else:
        print("True")
