"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        listt = {}
        cur = head

        while cur:
            node = Node(cur.val)
            listt[cur] = node
            cur = cur.next
        cur = head
        while cur:
            node = listt[cur]
            node.next = listt[cur.next] if cur.next else None
            node.random = listt[cur.random] if cur.random else None
            cur = cur.next
        
        return listt[head]
