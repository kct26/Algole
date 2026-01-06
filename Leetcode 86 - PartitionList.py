# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        l1 = ListNode() # less than x
        l2 = ListNode() # greater than or equal to x
        head1 = l1
        head2 = l2
        current = head
        while current:
            if current.val < x:
                l1.next = current
                l1 = l1.next
            else:
                l2.next = current
                l2 = l2.next
            current = current.next
        l2.next = None      
        head2 = head2.next
        l1.next = head2
        return head1.next
