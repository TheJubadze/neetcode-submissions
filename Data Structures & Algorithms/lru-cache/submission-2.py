class Node:
    def __init__(self, key, val):
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None
        self.key, self.val = key, val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def addLast(self, node: Node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node):
        prv, nxt = node.prev, node.next
        nxt.prev, prv.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addLast(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.addLast(node)

        if len(self.cache) > self.cap:
            toRemove = self.head.next
            self.removeNode(toRemove)
            del self.cache[toRemove.key]