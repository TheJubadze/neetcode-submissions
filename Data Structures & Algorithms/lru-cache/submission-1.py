class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.use = deque()
        self.storage = defaultdict(int)

    def get(self, key: int) -> int:
        if key in self.storage:
            tmp = []
            k, v = self.use.pop()
            while len(self.use) and k != key:
                tmp.append((k, v))
                k, v = self.use.pop()
            while tmp:
                self.use.append(tmp.pop())
            self.use.append((k, v))
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            tmp = []
            k, v = self.use.pop()
            while k != key:
                tmp.append((k, v))
                k, v = self.use.pop()
            while tmp:
                self.use.append(tmp.pop())
            self.use.append((key, value))
            self.storage[key] = value
            return

        if self.cap:
            self.use.append((key, value))
            self.storage[key] = value
            self.cap -= 1
            return
        
        k, _ = self.use.popleft()
        self.use.append((key, value))
        self.storage.pop(k)
        self.storage[key] = value
