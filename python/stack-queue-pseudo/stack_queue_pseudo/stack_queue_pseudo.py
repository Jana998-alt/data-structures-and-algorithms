class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, node=None):
        self.top = node

    def push(self, value):
        temp_node = self.top
        self.top = Node(value)
        self.top.next = temp_node

    def pop(self):

        if self.top == None:
            raise ValueError('Empty Stack')

        temp_node = self.top.next
        temp_value = self.top.value
        self.top = None
        self.top = temp_node
        return temp_value

    def peek(self):

        if self.top == None:
            raise ValueError('Empty Stack')
        else:
            return self.top.value

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



# Methods:
# enqueue
# Arguments: value
# Inserts value into the PseudoQueue, using a first-in, first-out approach.
# dequeue
# Arguments: none
# Extracts a value from the PseudoQueue, using a first-in, first-out approach.h
# NOTE: The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.


class PseudoQueue:
    def __init__(self):
        self.stack_front = Stack()
        self.stack_rear = Stack()

    def enqueue(self, value):
        self.stack_front.push(value)

    def dequeue(self):
        empty_stack = self.stack_rear
        current = self.stack_front.top
        return_val = None

        while current.next != None:
            value = self.stack_front.peek()
            self.stack_rear.push(value)
            self.stack_front.pop()
            current = current.next
        return_val = current.value
        self.stack_front.pop()

        current2 = self.stack_rear.top
        while current2 != None:
            value = self.stack_rear.peek()
            self.stack_front.push(value)
            current2 = current2.next

        # self.stack_front = self.stack_rear
        self.stack_rear = empty_stack

        return return_val

    def __str__(self):
        str = 'front ->'
        current_node = self.stack_front.top

        while current_node:
            print(current_node.value)
            str = str + f" {current_node.value} ->"
            if current_node == None:
                str = str + ' rear'
                break
            current_node = current_node.next

        if current_node == None:
            str = str + ' rear'

        return str



if __name__ == "__main__":
    pass
