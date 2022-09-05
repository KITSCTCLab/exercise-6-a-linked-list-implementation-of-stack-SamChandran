class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        temp = self.head
        if temp is None:
            self.head = Node(data)
            self.count += 1
#             return True
        else:
            while temp.next is not self.head:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node
            new_node.previous = temp
            new_node.next = self.head
            self.count += 1
            return True

    def add_at_head(self, data) -> bool:
        if self.head is None:
            self.head = Node(data)
            self.count = 1
            return True
        else:
            new_node = Node(data)
            temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        new_node.previous = temp
        temp.next = new_node
        self.head = new_node
        self.count += 1
        return True        

    def add_at_index(self, index, data) -> bool:
        if (index >= self.count) or (index < 0):
            return False
        if self.head is None:
            self.count = 1
            self.head = Node(data)
            return True
        else:
            temp = self.head
            if index == 0:
                temp = temp.previous
            else:
                for _ in range(index - 1):
                    temp = temp.next
            temp.next.previous = Node(data)
            temp.next.previous.next, temp.next.previous.previous = temp.next, temp
            temp.next = temp.next.previous
            if index == 0:
                self.head = self.head.previous
            self.count += 1
            return True        

    def get(self, index) -> int:
        if (index >= self.count) or (index < 0):
            return -1
        if self.head is None:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.data        

    def delete_at_index(self, index) -> bool:
        if (index >= self.count) | (index < 0):
            return False
        if self.count == 1:
            self.head = None
            self.count -= 1
            return True

        target = self.head
        for _ in range(index):
            target = target.next

        if target is self.head:
            self.head = self.head.next

        target.previous.next, target.next.previous = target.next, target.previous
        self.count -= 1
        return True        

    def get_previous_next(self, index) -> list:
        if (index >= self.count) or (index < 0) or self.head is None:
            return [-1]
        else:
            if self.count == 1:
                return [self.head.previous.data, self.head.next.data]
            else:
                my_counter = 0
                temp = self.head
                while my_counter < index:
                    temp = temp.next
                    my_counter += 1
                return [temp.previous.data, temp.next.data]        


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []



# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
