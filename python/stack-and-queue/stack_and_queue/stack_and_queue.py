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

        # peek
        # Arguments: none
        # Returns: Value of the node located at the top of the stack
        # Should raise exception when called on empty stack

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
    new_stack.top = Node(1)
    new_stack.top.next = Node(2)
    new_stack.top.next.next = Node(3)
    new_stack.top.next.next.next = Node(4)
    new_stack.top.next.next.next.next = Node(5)
    print(new_stack.__str__())
