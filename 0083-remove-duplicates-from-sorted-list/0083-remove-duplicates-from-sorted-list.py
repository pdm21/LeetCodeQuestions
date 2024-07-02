# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        i, j = head, head.next
        while j:
            # if i = j, hold i, move j
            if i.val == j.val:
                j = j.next
                continue
            else:
                i.next = j
                i = j
                j = j.next
        i.next = None
        return head
    
