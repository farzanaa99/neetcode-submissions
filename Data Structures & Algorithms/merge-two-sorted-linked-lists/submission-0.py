# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = list1
        current2 = list2

        newHead = None
        tail = newHead

        while current1 and current2:
            if current1.val < current2.val:
                if newHead:
                    tail.next = current1
                    tail = current1
                else:
                    newHead = current1
                    tail = newHead
                
                current1 = current1.next

            else:
                if newHead:
                    tail.next = current2
                    tail = current2
                else:
                    newHead = current2
                    tail = newHead
                current2 = current2.next


        while current1:
            if newHead:
                tail.next = current1
                tail = current1
            else:
                newHead = current1
                tail = newHead
            current1 = current1.next

        while current2:
            if newHead:
                tail.next = current2
                tail = current2
            else:
                newHead = current2
                tail = newHead
            current2 = current2.next

        return newHead

