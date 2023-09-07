# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = lnode = rnode = head
        l = r = 1
        n = 0

        # length of the ListNode
        while curr is not None:
            curr = curr.next
            n += 1
        
        # left node
        while l < k:
            lnode = lnode.next
            l += 1
        
        lval = lnode.val

        # right node
        while r < n - k + 1:
            rnode = rnode.next
            r += 1
        
        rval = rnode.val

        lnode.val = rval
        rnode.val = lval

        return head



        