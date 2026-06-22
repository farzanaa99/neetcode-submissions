# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current = head

        length = 0
        while current:
            length += 1
            current = current.next

        if n == length:
            return head.next

        dummy = head        
        for _ in range(length - n - 1):
            dummy = dummy.next

        dummy.next = dummy.next.next

        return head

        
