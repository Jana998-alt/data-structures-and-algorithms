class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"value: {self.value}"


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

    def kth_from_end(self,k):
        # argument: a number, k, as a parameter.
        # Return the node’s value that is k places from the tail of the linked list.
        # You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
        current_node = self.head
        length = 1
        while current_node:
            current_node = current_node.next
            length+=1

        if length == 1:
            return "linked list is empty"

        if k>= length or k<0:
            return None

        else:
            current_node = self.head
            value_at_k = ''

            for i in range(length - k - 2):
                current_node.next

            value_at_k = current_node.value
        return value_at_k


    @staticmethod
    def zip_lists(l1, l2):
        # Arguments: 2 linked lists
        # Return: Linked List, zipped as noted below
        # Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
        # Try and keep additional space down to O(1)
        # You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.


        zipped_list = Linked_List()
        zipped_list_current = zipped_list.head
        node1= l1.head
        node2 = l2.head
        while node1 != None and node2 != None:
            print(node1)
            print(node2)
            print(zipped_list_current)
            zipped_list_current = node1
            zipped_list_current.next = node2
            node1 = node1.next
            node2 = node2.next
            zipped_list_current = zipped_list_current.next.next

        return zipped_list


if __name__ == "__main__":
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)

    new_linked2 = Linked_List()
    new_linked2.insert(22)
    new_linked2.insert(33)
    new_linked2.insert(44)
    expected = "head -> 2 -> 22 -> 3 -> 33 -> 4 -> 44 -> NULL"
    actual = Linked_List.zip_lists(new_linked, new_linked2)
    print(actual)
