class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    

class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    new = Node(data)
    if not self.head== None:
      new.next = self.head
      self.head=new
    else:
      self.head=new
      

  def pop(self) -> None:
    if not self.head==None:
      self.head = self.head.next

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
    ele= ""
    temp=self.head
    while temp is not None:
      ele += str(temp.data) + "=>"
      temp=temp.next
    print (ele+"None")


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
