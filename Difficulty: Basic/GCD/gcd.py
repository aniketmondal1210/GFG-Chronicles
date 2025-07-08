#User function Template for python3
a = int(input())
b = int(input())
# Your code here
if a == 0:
    print(b)
elif b == 0:
    print(a)
else:
    result = []
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i==0:
            result.append(i)
    print(max(result))
