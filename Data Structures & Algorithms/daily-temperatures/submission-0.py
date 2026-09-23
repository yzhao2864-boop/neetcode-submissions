class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,c in enumerate(temperatures):
            while stack and c>stack[-1][0]:
                stacki,stackint=stack.pop()
                res[stackint]=i-stackint
            stack.append([c,i])
        return res
        