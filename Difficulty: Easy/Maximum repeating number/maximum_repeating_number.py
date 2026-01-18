from collections import Counter
#User function Template for python3
class Solution:
	def maxRepeating(self,k, arr):
		# code here
		count = Counter(arr)
        max_frequency = max(count.values())
        max_elements = []
        for i in range(k):
            if count[i] == max_frequency:
                max_elements.append(i)
        return min(max_elements)
