import pytest
from linked_list import __version__



def test_version():
    assert __version__ == '0.1.0'


from linked_list.linked_list import (Linked_List, Node)

# Can successfully instantiate an empty linked list

def test_for_Linked_List_instantiation():
    expected = None
    actual = Linked_List().head
    assert expected == actual


# Can properly insert into the linked list

def test_for_Linked_List_insert():
    new_linked = Linked_List()
    new_linked.insert(2)
    expected = "head -> 2 -> NULL"
    actual = new_linked.__str__()
    assert expected == actual


# The head property will properly point to the first node in the linked list

def test_head_point_to_first_node():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    excepted = 4
    actual = new_linked.head.value
    assert excepted == actual

# Can properly insert multiple nodes into the linked list

def test_for_Linked_List_insert_multiple():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    expected = "head -> 4 -> 3 -> 2 -> NULL"
    actual = new_linked.__str__()
    assert expected == actual


# Will return true when finding a value within the linked list that exists

def test_find_value_in_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    actual = new_linked.includes(3)
    excepted = True
    assert actual == excepted

# Will return false when searching for a value in the linked list that does not exist

@pytest.fixture
def test_not_find_value_in_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    actual = new_linked.includes(6)
    excepted = False
    assert actual == excepted

# Can properly return a collection of all the values that exist in the linked list

# Can successfully add a node to the end of the linked list

def test_append_to_end_of_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    new_linked.append(1)
    expected = "head -> 4 -> 3 -> 2 -> 1 -> NULL"
    actual = new_linked.__str__()
    assert expected == actual

# Can successfully add multiple nodes to the end of a linked list

def test_append_multiple_values_to_end_of_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    new_linked.append(1)
    new_linked.append(0)
    expected = "head -> 4 -> 3 -> 2 -> 1 -> 0 -> NULL"
    actual = new_linked.__str__()
    assert expected == actual


# Can successfully insert a node before a node located i the middle of a linked list

def test_insert_before_a_value_in_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    new_linked.insert_before(3, 111)
    expected = "head -> 4 -> 111 -> 3 -> 2 -> NULL"
    actual = new_linked.__str__()
    assert expected == actual

# Can successfully insert a node before the first node of a linked list

def test_insert_before_first_value_in_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    new_linked.insert_before(4, 111)
    expected = "head -> 111 -> 4 -> 3 -> 2 -> NULL"
    actual = new_linked.__str__()
    assert expected == actual

# Can successfully insert after a node in the middle of the linked list

def test_insert_after_node_in_middle_of_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    new_linked.insert_after(3, 111)
    expected = "head -> 4 -> 3 -> 111 -> 2 -> NULL"
    actual = new_linked.__str__()
    assert expected == actual


# Can successfully insert a node after the last node of the linked list

def test_insert_after_node_in_end_of_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    new_linked.insert_after(2, 111)
    expected = "head -> 4 -> 3 -> 2 -> 111 -> NULL"
    actual = new_linked.__str__()
    assert expected == actual


# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list

def test_kth_from_end():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    expected = 4
    actual = new_linked.kth_from_end(2)
    assert expected == actual



def test_kth_from_end():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)

    new_linked2 = Linked_List()
    new_linked2.insert(22)
    new_linked2.insert(33)
    new_linked2.insert(44)
    expected = "head -> 4 -> 44 -> 3 -> 33 -> 2 -> 22 -> NULL"
    actual = Linked_List.zip_lists(new_linked, new_linked2).__str__()
    assert expected == actual
