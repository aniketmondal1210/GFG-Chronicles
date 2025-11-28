class Solution:
    def _push(self, arr):
        # code here
        stack = []
        for x in arr:
            stack.append(x)
        return stack

    def _pop(self, stack):
        while stack:
            print(stack.pop(), end=" ")
