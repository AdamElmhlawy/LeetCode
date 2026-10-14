# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        cur = curn = dummy

        for n in range(n+1):
            curn = curn.next
        
        while curn:
            cur = cur.next
            curn = curn.next
        cur.next = cur.next.next
        
        return dummy.next