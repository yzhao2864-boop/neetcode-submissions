# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                a=lists[i]
                b=lists[i+1] if i+1<len(lists) else None
                merged.append(self.mergeTwo(a,b))
            lists=merged
        return lists[0]
    
    def mergeTwo(self,a,b):
        dummy=ListNode(0)
        tail=dummy
        while a and b:
            if a.val<=b.val:
                tail.next=a
                a=a.next
            else:
                tail.next=b
                b=b.next
            
            tail=tail.next
        
        tail.next=a if a else b

        return dummy.next