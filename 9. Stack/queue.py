import collections

# 23. 큐를 이용한 스택 구현
class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
    
# 통과

# 24. 스택을 이용한 큐 구현
class MyQueue:
    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        return self.s.pop(0)

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return len(self.s) == 0
    
# 통과

# 25. 원형 큐 디자인
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.max = k

    def enQueue(self, value: int) -> bool:
        if self.max > len(self.q):
            self.q.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.q) == 0:
            return False
        self.q.pop(0)
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[0]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[len(self.q)-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.max
    
# 통과