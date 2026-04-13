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

        node_map = {None: None}
        cur = head

        # create copies of all nodes to map in first pass
        while cur:
            copy = Node(cur.val)
            node_map[cur] = copy
            cur = cur.next

        # reset to beginning of list
        cur = head

        # second pass, retrieve copy of node and assign the random pointer
        while cur:
            copy = node_map[cur]
            copy.next = node_map[cur.next]
            copy.random = node_map[cur.random]

            cur = cur.next
        
        return node_map[head]

