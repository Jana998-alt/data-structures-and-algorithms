class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, node=None):
        self.top = node

        # push
        # Arguments: value
        # adds a new node with that value to the top of the stack with an O(1) Time performance.

    def push(self, value):
        temp_node = self.top
        self.top = Node(value)
        self.top.next = temp_node

        # pop
        # Arguments: none
        # Returns: the value from node from the top of the stack
        # Removes the node from the top of the stack
        # Should raise exception when called on empty stack

    def pop(self):

        if self.top == None:
            raise ValueError('Empty Stack')

        temp_node = self.top.next
        temp_value = self.top.value
        self.top = None
        self.top = temp_node
        return temp_value

        # peek
        # Arguments: none
        # Returns: Value of the node located at the top of the stack
        # Should raise exception when called on empty stack

    def peek(self):

        if self.top == None:
            raise ValueError('Empty Stack')
        else:
            return self.top.value

        # is empty
        # Arguments: none
        # Returns: Boolean indicating whether or not the stack is empty.


    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


    def __str__(self):
        str = 'top ->'
        current_node = self.top

        while current_node:
            print(current_node.value)
            str = str + f" {current_node.value} ->"
            if current_node == None:
                str = str + ' NULL'
                break
            current_node = current_node.next

        if current_node == None:
            str = str + ' NULL'

        return str



class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    # enqueue
    # Arguments: value
    # adds a new node with that value to the back of the queue with an O(1) Time performance.

# "top -> 1 -> 2 -> 3 -> 4 -> 5 -> 99 -> rear"

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear == None and self.front == None:
            self.front = new_node
            self.rear = None

        elif self.rear == None:
            self.front.next = new_node
            self.rear = new_node
        else:
            temp_node = self.rear
            temp_node.next = new_node
            self.rear = new_node


    # dequeue
    # Arguments: none
    # Returns: the value from node from the top of the queue
    # Removes the node from the top of the queue
    # Should raise exception when called on empty queuey


    # peek
    # Arguments: none
    # Returns: Value of the node located at the top of the queue
    # Should raise exception when called on empty stack


    # is empty
    # Arguments: none
    # Returns: Boolean indicating whether or not the queue is empty

    def __str__(self):
        str = 'front ->'
        current_node = self.front

        while current_node:
            print(current_node.value)
            str = str + f" {current_node.value} ->"
            if current_node == None:
                str = str + ' NULL'
                break
            current_node = current_node.next

        if current_node == None:
            str = str + ' rear'

        return str



if __name__ == "__main__":
    new_stack = Stack()
    print(type(new_stack.pop()))
