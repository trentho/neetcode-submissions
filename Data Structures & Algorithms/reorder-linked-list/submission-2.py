# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        # two pointers

        left, right = 0 , len(nodes) - 1

        # [1, 2 ,3 ,4 ,5]
        # [1, 5]
        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left >= right:
                break
            nodes[right].next = nodes[left]
            
            right -= 1

        nodes[left].next = None
