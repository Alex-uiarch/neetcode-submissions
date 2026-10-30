

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = '', ''

        while l1:
            num1 = str(l1.val) + num1  
            l1 = l1.next

        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        num = int(num1) + int(num2)

        num = str(num)[::-1]
        lst = [ListNode(val=int(x)) for x in num]

        for i in range(len(lst) - 1):
            lst[i].next = lst[i + 1]

        return lst[0]
        


        
    




