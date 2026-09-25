
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        

        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next

        previous = head

        while list1 and list2:
    
            if list1.val > list2.val:
                tail = list2
                previous.next = tail
                list2 = list2.next
            else:
                tail = list1
                previous.next = tail
                list1 = list1.next

            previous = tail

        if list1 is not None:
            previous.next = list1
        else:
            previous.next = list2


        return head
