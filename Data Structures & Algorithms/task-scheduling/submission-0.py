from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt=Counter(tasks)
        mfreq=max(cnt.values())
        cou_max=sum(1 for c in cnt.values() if c==mfreq)
        return max(len(tasks),(mfreq-1)*(n+1)+cou_max)
