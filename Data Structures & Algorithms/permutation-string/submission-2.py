class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        target=[0]*26
        windows=[0]*26

        if m>n:
            return False
        
        for i in s1:
            target[ord(i)-ord('a')]+=1
        
        for i,c in enumerate(s2):
            windows[ord(c)-ord('a')]+=1

            if i>=m:
                windows[ord(s2[i-m])-ord('a')]-=1
            
            if i>=m-1 and windows==target:
                return True
        
        return m==0
