# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    flag = True
    for i in arr:
        if str(i)[::-1] != str(i):
            flag = False
    return flag
