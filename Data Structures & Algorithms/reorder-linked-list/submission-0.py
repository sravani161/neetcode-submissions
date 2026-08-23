# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        #middle of the LL
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        #reverse of second LL
        prev = None
        while head2:
            next_node = head2.next
            head2.next = prev
            prev = head2
            head2 = next_node
        #merge
        head1 = head
        head_2 = prev
        while head_2:
            tmp1, tmp2 = head1.next, head_2.next
            head1.next = head_2
            head_2.next = tmp1
            head1, head_2 = tmp1, tmp2