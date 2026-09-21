class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n,m=len(s),len(t)
        res=""
        ans=float("inf")
        start=0
        target={}
        windows={}
        if m>n or t=="":
            return res
        for i in t:
            target[i]=1+target.get(i,0)
        need=len(target)
        have=0
        left=0
        for i,c in enumerate(s):
            windows[c]=1+windows.get(c,0)
            if c in target and windows[c]==target[c]:
                have+=1
            while have==need:
                if i-left+1<ans:
                    ans=i-left+1
                    start=left
                pop=s[left]
                windows[pop]-=1
                if pop in target and windows[pop]<target[pop]:
                    have-=1
                left+=1
        return res if ans ==float("inf") else s[start:start+ans]

