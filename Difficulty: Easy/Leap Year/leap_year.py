#User function Template for python3
# Take year input and print if year is a leap year
t = int(input())
if (t % 4 == 0):
    if (t % 100 != 0) or (t % 400 == 0):
        print("True")
    else:
        print("False")
else:
    print("False")
