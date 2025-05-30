def pos(n):
    ## Write the code
    if n == 0:
        zero()
    else:
        for i in range(n-1,-1,-1):
            print(i,end = " ")

def neg(n):
    ##Write the code
    if n == 0:
        zero()
    else:
        for i in range(n,+1,1):
            print(i,end = " ")

def zero():
    print("already Zero")
