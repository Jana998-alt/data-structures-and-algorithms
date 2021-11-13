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


if __name__ == "__main__":
    new_stack = Stack()
    print(type(new_stack.pop()))
