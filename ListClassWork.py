#Autumn
#class work

class MyList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, value):
        li = ListItem(value, self.length)

        if self.length == 0:
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
            output += ", " + str(ci.value) + ', '

        return output


class ListItem:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.next = None
        self.prev = None

newList = MyList()
newList.add(5)
newList.add(7)
newList.add("hello")
print(newList.head.value)
print(newList.head.next.value)
print(newList.tail.value)
print(newList)
