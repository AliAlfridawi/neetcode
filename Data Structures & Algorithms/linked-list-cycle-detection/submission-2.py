# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head

        while p2:
            p2 = p2.next
            if p2 == p1:
                return True
            if p2 is None:
                return False
            p2 = p2.next
            p1 = p1.next
        return False