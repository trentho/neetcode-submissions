# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # store nodes in an array
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        # two pointers to reorder
        left, right = 0 , len(nodes) - 1
              
        while left < right:
            # Connects the current left node to the right node.
            nodes[left].next = nodes[right]
            left += 1

            #connect right pointer to next left node
            nodes[right].next = nodes[left]
            right -= 1
    
        # terminate the new reordered list
        nodes[left].next = None
