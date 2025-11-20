class QueueArray:
    def __init__(self):
        self.Queue = []
        self.front = 0
        self.rear = -1

    def size(self):
        return len(self.Queue) - self.front

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.Queue.append(item)
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            print("\nQueue is empty")
            return None
        item = self.Queue[self.front]
        self.front += 1
        # Optional: clear unused space if front gets large to free memory
        if self.front > len(self.Queue) // 2:
            self.Queue = self.Queue[self.front:]
            self.rear -= self.front
            self.front = 0
        return item


obj = QueueArray()
while True:
    print("1. enqueue")
    print("2. dequeue")
    print("Enter your choice")
    choice = int(input())
    if choice == 1:
        print("Number")
        num = int(input())
        obj.enqueue(num)
    elif choice == 2:
        print("dequeue element", obj.dequeue())
