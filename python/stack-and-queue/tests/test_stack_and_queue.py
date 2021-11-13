from stack_and_queue import __version__
import pytest
import unittest
from stack_and_queue.stack_and_queue import (Node, Stack)



def test_version():
    assert __version__ == '0.1.0'


# Can successfully push onto a stack
def test_for_push_to_stack(stack):
    expected = "top -> 99 -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL"
    stack.push(99)
    actual = stack.__str__()
    assert expected == actual

# Can successfully push multiple values onto a stack

def test_for_push_multiple_to_stack(stack):
    expected = "top -> 77 -> 88 -> 99 -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL"
    stack.push(99)
    stack.push(88)
    stack.push(77)
    actual = stack.__str__()
    assert expected == actual

# Can successfully pop off the stack

def test_for_pop_from_stack(stack):
    expected = "top -> 3 -> 4 -> 5 -> NULL"
    expected2 = "2"
    stack.pop()
    actual2 = stack.pop()
    actual = stack.__str__()
    assert expected == actual, expected2 == actual2

# Can successfully empty a stack after multiple pops

def test_for_pop_till_empty_stack(stack):
    expected = "top -> NULL"
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.__str__()
    assert expected == actual

# Can successfully peek the next item on the stack

def test_for_peek_stack(stack):
    actual = stack.peek()
    expected = 1
    assert expected == actual


# Can successfully instantiate an empty stack

def test_for_instantiate_stack():
    new_stack = Stack()
    actual = new_stack.__str__()
    expected = "top -> NULL"
    assert expected == actual

# Calling pop or peek on empty stack raises exception

# def test_for_pop_or_peek_on_empty_stack_raises_exception(empty_stack):
#     empty_stack.pop()
#     assert unittest.TestCase.assertRaises(ValueError)



# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue
# Calling dequeue or peek on empty queue raises exception


# fixtures
@pytest.fixture
def stack():
    new_stack = Stack()
    new_stack.top = Node(1)
    new_stack.top.next = Node(2)
    new_stack.top.next.next = Node(3)
    new_stack.top.next.next.next = Node(4)
    new_stack.top.next.next.next.next = Node(5)
    # "top -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL"
    return new_stack

@pytest.fixture
def empty_stack():
    empty_stack = Stack()
    return empty_stack
