class OurQueue:
    def __init__(self):
        self.in_stack = []  # 队列的尾部
        self.out_stack = []  # 队列的头部

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:  # 队列的头为空
            self.out_stack = self.in_stack[::-1]  # in_stack逆序给out_stack
            self.in_stack = []
        return self.out_stack.pop()


queue = OurQueue()
for i in range(5):
    queue.push(i)
    print(queue.pop(), end=" ")
