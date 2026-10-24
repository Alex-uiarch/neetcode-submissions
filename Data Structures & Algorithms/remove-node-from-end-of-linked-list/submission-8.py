# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        curNode = head.next
        prNode = head

        k = self.length(head)
        if n == k:
            return head.next

        for _ in range(k - n - 1):
            curNode = curNode.next
            prNode = prNode.next
        
        if curNode.next == None:
            prNode.next = None

        ftNode = curNode.next

        prNode.next = ftNode

        return head

    def length(self, head: Optional[ListNode]) -> int:
        x = 1
        while head.next:
            x += 1
            head = head.next
        return x

        