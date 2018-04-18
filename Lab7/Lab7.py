#Autumn Franke
#Lab 7

class MyQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, value):
        li = ListItem(value, self.length)

        if self.length ==0:
            self.head = li
        else:
            li.prev = self.tail
            self.tail.next = li
        self.tail = li
        self.length += 1

    def __str__(self):
        output = str(self.head.value)

        ci = self.head
        for i in range(self.length-1):
            ci = ci.next
            output += str(ci.value) + ', '

        return output

class MyStack:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, value):
        li = ListItem(value, self.length)

        if self.length ==0:
            self.head = li
        else:
            li.prev = self.tail
            self.tail.next = li
        self.tail = li
        self.length += 1

    def __str__(self):
        output = str(self.tail.value)

        ci = self.tail
        for i in range(self.length-1):
            ci = ci.next
            output += str(ci.value) + ', '

        return output

class ListItem:
    def __init__(self,value,index):
        self.value = value
        self.index = index
        self.next = None
        self.prev = None


newQueue = MyQueue()
newQueue.add(7)
newQueue.add(3)
newQueue.add(14)
newQueue.add(1)
newQueue.add(21)
newQueue.add(0)
newQueue.add(0)
newQueue.add(56)
print(newQueue)


newStack = MyStack()
newStack.add(7)
newStack.add(3)
newStack.add(14)
newStack.add(1)
newStack.add(21)
newStack.add(0)
newStack.add(0)
newStack.add(56)
print(newStack)
