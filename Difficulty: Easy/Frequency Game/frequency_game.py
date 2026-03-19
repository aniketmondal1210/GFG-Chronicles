from collections import Counter
def LargButMinFreq(arr,n):
    #code here
    a = Counter(arr)
    result = []
    min_freq = min(a.values())
    for key,value in a.items():
        if value == min_freq:
            result.append(key)
    return max(result)
