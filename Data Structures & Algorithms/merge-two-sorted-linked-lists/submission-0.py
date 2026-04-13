# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize head node that is a reference of the beggining of the new list
        head = node = ListNode()


        # while list1 and list2 are not none iterate through

        while list1 and list2:

            #if list1 value is lower than we want to set node to the lower value (list1) and then iterate to the next node in list1
            if list1.val < list2.val:
                
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
        
            node = node.next
            
        # once one of the lists run out we can just append the rest of list1 or list2 if they have remaining nodes
        # since they are sorted already.    
        node.next = list1 or list2

        return head.next
