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


def validate_brackets(b_str):

  bracket_stack = Stack()

  for bracket in b_str:
    if bracket == '(' or bracket =='[' or bracket =='{':
      bracket_stack.push(bracket)

    else:
      if bracket_stack.is_empty():
        return False

    if bracket == ')':
      if bracket_stack.peek() == '(':
        bracket_stack.pop()
      else:
        return False

    elif bracket ==']':
      if bracket_stack.peek() == '[':
        bracket_stack.pop()
      else:
        return False

    elif bracket =='}':
      if bracket_stack.peek() == '{':
        bracket_stack.pop()
      else:
        return False


  return True


if __name__ =="__main__":
  pass
