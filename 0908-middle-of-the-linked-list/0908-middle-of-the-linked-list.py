# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        visited = []
        cur = head

        while cur and cur.next:
            visited.append(cur)
            cur = cur.next
        visited.append(cur)

        return visited[len(visited) // 2]