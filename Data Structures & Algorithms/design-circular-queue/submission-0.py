class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.maxSize = k
        self.arr = [None] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.maxSize
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.arr[self.front] = None
        self.front = (self.front + 1) % self.maxSize
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.arr[(self.rear - 1) % self.maxSize]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize