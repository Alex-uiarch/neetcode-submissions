
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        previous = None

        while curr is not None:

            curr_next = curr.next
            curr.next = previous
            previous = curr
            curr = curr_next

        return previous
        