#User function Template for python3

def nonNegativeAverage(arr):
    sum = 0
    count = 0
    for i in arr:
    #Write your code to find average of positive numbers in number list
    #Return the answer
        if i >= 0:
            sum += i
            count += 1
    return sum/count
    
