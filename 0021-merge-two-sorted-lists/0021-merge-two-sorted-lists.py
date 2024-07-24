# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base case 1: list1 is empty
        if not list1:
            return list2
        # base case 2: list2 is empty
        if not list2:
            return list1
        # determine smaller and bigger lists
        if list1.val < list2.val:
            lil, big = (list1, list2)
        else:
            lil, big = (list2, list1)
            
        # recursive case, set lil.next and rec call on lil.next (took head) and big
        lil.next = self.mergeTwoLists(lil.next, big)
        
        return lil