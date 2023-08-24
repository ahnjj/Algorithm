# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        # reversed half (1) get to the middle : slow = starts from the half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # (2)
        prev, nextNode = None, None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        maxVal = 0

        while prev:
            maxVal = max(maxVal, head.val+prev.val)
            prev = prev.next
            head = head.next
        
        return maxVal