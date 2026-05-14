class Node:
    def __init__(self, k, v):
        self.key, self.value = k, v
        self.next: 'Node | None' = None

class HashTable:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = [None] * capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        idx = key % self.cap
        head = self.arr[idx]
        while head:
            if head.key == key:
                head.value = value
                return
            head = head.next
        
        new_node = Node(key, value)
        new_node.next = self.arr[idx]
        self.arr[idx] = new_node
        self.size += 1
        
        if self.size >= self.cap / 2:
            self.resize()

    def get(self, key: int) -> int:
        idx = key % self.cap
        head = self.arr[idx]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def remove(self, key: int) -> bool:
        idx = key % self.cap
        prev = None
        head = self.arr[idx]
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.arr[idx] = head.next
                self.size -= 1
                return True
            prev, head = head, head.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        oldArr = self.arr
        self.size = 0
        self.cap *= 2
        self.arr = [None] * self.cap
        for node in oldArr:
            while node:
                self.insert(node.key, node.value)
                node = node.next