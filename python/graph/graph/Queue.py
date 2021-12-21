import re


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    # enqueue
    # Arguments: value
    # adds a new node with that value to the back of the queue with an O(1) Time performance.

# "front -> 1 -> 2 -> 3 -> 4 -> 5 -> 99 -> rear"

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
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

    def dequeue(self):
        if self.is_empty():
            raise ValueError('empty queue')
        elif self.front:
          temp_val = self.front.value
          self.front = self.front.next

          return temp_val

        elif self.rear:
          temp_val = self.rear.value
          self.rear = None

          return temp_val

    # peek
    # Arguments: none
    # Returns: Value of the node located at the top of the queue
    # Should raise exception when called on empty stack

    def peek(self):
        if self.front == None:
            raise ValueError('empty queue')
        else:
            return self.front.value

    # is empty
    # Arguments: none
    # Returns: Boolean indicating whether or not the queue is empty

    def is_empty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            return False


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

