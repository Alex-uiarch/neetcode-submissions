
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return None

        
        flag = 1
        nflag = 1
        curnode =  head
        lengh = self.getLength(head)

        if lengh == 1:
            return None

        while  nflag <= lengh // 2:
            print("flag:", flag, "nflag:", nflag, "node:", curnode.val)
            
            if flag % 2 != 0:
                nextNode = curnode.next
                neededNode = self.getLast(curnode)
                curnode.next = neededNode

                if neededNode != nextNode:
                    neededNode.next = nextNode
                nflag += 1

            curnode = curnode.next
            flag += 1





        return None


    
    def getLast(self, node:Optional[ListNode]) -> Optional[ListNode]:
        node1 = node
        node = node.next
        while node.next:
            node1, node = node, node.next

        needed = node
        node1.next = None
        
        return needed

    def getLength(self, node: Optional[ListNode]) -> int:
        x = 1
        while node.next:
            x += 1
            node = node.next
        return x




