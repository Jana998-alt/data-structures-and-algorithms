class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.tail = -1


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self,value):
    # Arguments: value
    # Returns: nothing
    # Adds a new node with that value to the head of the list with an O(1) Time performance.
        if self.head == None:
            self.head = Node(value)

        else:
            current_node = self.head
            while current_node:
                if current_node.tail == -1:
                    current_node.next = Node(value)
                    current_node.next.next = None
                    current_node.tail = 0
                    break
                current_node = current_node.next



    def includes(self,value):
    # Arguments: value
    # Returns: Boolean
    # Indicates whether that value exists as a Node’s value somewhere within the list.
        current_node = self.head
        while current_node.next != None:
            if value == current_node.value:
                return True
            else:
                current_node = current_node.next

        return False

    def to_string(self):
    # Arguments: none
    # Returns: a string representing all the values in the Linked List, formatted as:
    # "{ a } -> { b } -> { c } -> NULL"
        current_node = self.head
        text = ' '
        while current_node:
            text = text + f'{current_node.value} -> '
            current_node = current_node.next

        text = text + "NULL"
        return text

