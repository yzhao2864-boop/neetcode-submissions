# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        cur=slow.next
        pre=None
        slow.next=None
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        
        first,second=head,pre
        while second:
            next_first=first.next
            next_second=second.next

            first.next=second
            second.next=next_first

            first=next_first
            second=next_second
