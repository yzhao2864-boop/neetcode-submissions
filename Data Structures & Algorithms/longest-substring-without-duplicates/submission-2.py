class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        seta=set()
        count=0
        for i in s:
            while i in seta:
                seta.remove(s[l])
                count-=1
                l+=1
            seta.add(i)
            count+=1
            res=max(res,count)
        return res