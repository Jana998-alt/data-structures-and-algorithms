from linked_list import __version__
import pytest


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

def test_not_find_value_in_linked_list():
    new_linked = Linked_List()
    new_linked.insert(2)
    new_linked.insert(3)
    new_linked.insert(4)
    actual = new_linked.includes(6)
    excepted = False
    assert actual == excepted

# Can properly return a collection of all the values that exist in the linked list

