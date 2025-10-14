#User function Template for python3
def game_with_number (arr,  n) : 
    #Complete the function
    result = []
    for i in range(n - 1):
        result.append(arr[i] ^ arr[i + 1])
    result.append(arr[-1])
    return result
