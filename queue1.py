class Queue():
    def __init__(self):
        self.queue = []

    def push(self, element: int):
        self.queue.append(element)

    def sortedPush(self, element: int):
        if self.queue == []:
            self.queue.append(element)
            return
        
        if element >= self.queue[-1]:
            self.queue.append(element)
            return
        
        if element <= self.queue[0]:
            self.queue.insert(0, element)
            return

        for i in range(1, len(self.queue)):
            if self.queue[i-1] <= element < self.queue[i]:
                self.queue.insert(i, element)
                return

    def pop(self, index: int):
        del self.queue[index]

queue1 = Queue()

input1 = input()

while input1 != "":
    queue1.sortedPush(int(input1))
    print(queue1.queue)
    input1 = input()