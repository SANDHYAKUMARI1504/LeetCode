# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prefix = 0
        mp = {}

        curr = dummy
        while curr:
            prefix += curr.val
            mp[prefix] = curr
            curr = curr.next

        prefix = 0
        curr = dummy

        while curr:
            prefix += curr.val
            curr.next = mp[prefix].next
            curr = curr.next

        return dummy.next
        