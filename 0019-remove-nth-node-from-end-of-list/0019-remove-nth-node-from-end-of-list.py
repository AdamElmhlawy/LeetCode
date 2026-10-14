# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        prev = None
        cur = head
        curn = cur
        for i in range(n-1):
            curn = curn.next
        
        while cur and curn.next:
            curn = curn.next
            prev = cur
            cur = cur.next
        if cur and prev:
            prev.next = cur.next
        elif cur:
            head = cur.next
        else:
            return None

        return head