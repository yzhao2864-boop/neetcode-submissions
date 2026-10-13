class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        stored={}
        for num in nums:
            if num not in stored:
                stored[num]=1
            else:
                return num
        