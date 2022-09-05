# Problem

Implement Stack using Linked list.</b>
To implement a stack using the singly linked list concept, all the singly linked list operations are performed based on Stack operations LIFO(last in first out).</br>
Assume all nodes in the linked list are 0-indexed.

![ds-linked-list-implementation-stack2](https://user-images.githubusercontent.com/77091625/188261505-573a218e-f731-4274-b907-3c59d5638570.png)

Implement the Stack class:
> **push(data)** : Add data to the stack and adjust the head pointing to top.</br>
**pop()** : Remove data from the stack and adjust the head pointing to top.</br>
**status()** : Display the elements of stack.</br>

# Constraints
Data should be integer value.

## Sample Input - 1
```
push, push, push, push
1, 2, 3, 4
```
## Sample Output - 1
```
4=>3=>2=>1=>None
```
## Sample Input - 2
```
push, pop, push, pop
10, -, 20, -
```
## Sample Output - 2
```
None
```
## Sample Input - 3
```
push, push, push, pop, pop, pop, pop, pop, push
1, 2, 3, -, -, -, -, -, 10
```
## Sample Output - 3
```
10=>None
```
