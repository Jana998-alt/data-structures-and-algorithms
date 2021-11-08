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
        text = 'head'
        if self.head != None:
            while current_node:
                text = text + f' -> {current_node.value}'
                current_node = current_node.next

        text = text + " -> NULL"
        return text


    def append(self,new_value):
        # arguments: new value
        # adds a new node with the given value to the end of the list
        current_node = self.head
        if self.head == None:
            self.head = Node(new_value)

        else:
            while current_node:
                if current_node.next == None:
                    current_node.next = Node(new_value)
                    current_node.next.next = None
                    break
                else:
                    current_node = current_node.next




    def insert_before(self,value, new_value):
        # arguments: value, new value
        # adds a new node with the given new value immediately before the first node that has the value specified

        previous_node = self.head
        if self.head.value == value:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node

        else:
            current_node = self.head.next
            while current_node:
                if current_node.value == value:
                    previous_node.next = Node(new_value)
                    previous_node.next.next= current_node
                    break
                elif current_node == None:
                    raise('node does not exist in linked list')

                else:
                    previous_node = current_node
                    current_node = current_node.next



    def insert_after(self, value, new_value):
        # arguments: value, new value
        # adds a new node with the given new value immediately after the first node that has the value specified
        current_node = self.head
        holder_node = ''
        while current_node:
            if value == current_node.value:
                holder_node = current_node.next
                current_node.next = Node(new_value)
                current_node.next.next = holder_node
                break

            elif current_node == None:
                raise('node does not exist in linked list')

            else:
                current_node = current_node.next

