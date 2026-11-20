import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users=set(self.following[userId])
        users.add(userId)

        heap=[]
        for u in users:
            if self.tweets[u]:
                idx=len(self.tweets[u])-1
                t,tid=self.tweets[u][idx]
                heap.append((-t,tid,u,idx))
        heapq.heapify(heap)

        feed=[]
        while heap and len(feed)<10:
            _,tid,u,idx=heapq.heappop(heap)
            feed.append(tid)
            if idx>0:
                t,nxt=self.tweets[u][idx-1]
                heapq.heappush(heap,(-t,nxt,u,idx-1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.following[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
