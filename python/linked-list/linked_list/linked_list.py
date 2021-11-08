class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None


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
            temp_node = self.head
            self.head = Node(value)
            self.head.next = temp_node



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

    def __str__(self):
    # Arguments: none
    # Returns: a string representing all the values in the Linked List, formatted as:
    # "{ a } -> { b } -> { c } -> NULL"
        current_node = self.head
        text = 'head -> '
        while current_node:
            text = text + f'{current_node.value} -> '
            current_node = current_node.next

        text = text + "NULL"
        return text

