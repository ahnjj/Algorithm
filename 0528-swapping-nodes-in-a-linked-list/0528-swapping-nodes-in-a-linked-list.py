# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = r = head

        # left node
        for i in range(k-1):
            l = l.next

        tail = l
        # right node
        while tail.next:
            r, tail = r.next, tail.next
        
        l.val, r.val = r.val, l.val
        return head



        