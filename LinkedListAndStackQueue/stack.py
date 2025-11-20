class StackArray:
    def __init__(self):
        self.Stack = []
        self.top = -1

    def size(self):
        return len(self.Stack)

    def StEmpty(self):
        if len(self.Stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.Stack.append(item)
        self.top = len(self.Stack)

    def pop(self):
        if self.StEmpty():
            print("\nStack is empty")
            return
        else:
            item = self.Stack.pop()
            if len(self.Stack) == 0:
                self.top = None
            else:
                self.top = self.top - 1
            return item
obj = StackArray()
while True:
    print("1. push")
    print("2. pop")
    print("Enter your choice")
    choice = int(input())
    if choice == 1:
        print("Number")
        num = int(input())
        obj.push(num)
    elif choice == 2:
        print("pop element", obj.pop())
