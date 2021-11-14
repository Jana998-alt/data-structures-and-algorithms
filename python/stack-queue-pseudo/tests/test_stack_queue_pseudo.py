from stack_queue_pseudo import __version__
import pytest
from stack_queue_pseudo.stack_queue_pseudo import (Node, PseudoQueue, Stack)
def test_version():
    assert __version__ == '0.1.0'


def test_for_enqueue_for_empty_queue():
    queue = PseudoQueue()
    queue.enqueue(1)
    actual = queue.__str__()
    excepted = "front -> 1 -> rear"
    assert actual == excepted

def test_for_enqueue_for_full_queue(queue):
    queue.enqueue(55)
    actual = queue.__str__()
    excepted = "front -> 55 -> 4 -> 3 -> 2 -> 1 -> rear"
    assert actual == excepted

def test_for_dequeue(queue):
    queue.dequeue()
    return_val = queue.dequeue()
    excepted_return_val = 2
    actual = queue.__str__()
    excepted = "front -> 4 -> 3 -> rear"

    assert actual == excepted, return_val == excepted_return_val


@pytest.fixture
def queue():
    new_queue = PseudoQueue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    new_queue.enqueue(4)

    return new_queue
