
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, prev: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node  = self.cache[key]
        self.removeNode(node)
        self.addToTail(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addToTail(node)
        else:
            node = Node(value)
            self.cache[key] = node
            self.addToTail(node)

            if len(self.cache) > self.capacity:
                lru_node = self.head.next

                for k, v in self.cache.items():
                    if v is lru_node:
                        del self.cache[k]
                        break

                self.removeNode(lru_node)





    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def addToTail(self, node):
        tail = self.tail
        prev = tail.prev
        prev.next = node
        node.prev = prev
        node.next = tail
        tail.prev = node

        
        
