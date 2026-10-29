
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None
        
        curNode = head
        lst = {}

        while curNode:
            lst[curNode] = Node(curNode.val)
            curNode = curNode.next

        node = head

        while node:
            lst[node].random = lst.get(node.random)
            lst[node].next = lst.get(node.next)
            node = node.next

        return lst[head]


