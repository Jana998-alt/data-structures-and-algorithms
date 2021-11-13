# Stacks and Queues
A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.
stacks follow the FILO rule, that is: the first item added in the stack will be the last item popped out of the stack.
queues follow the LIFO rule, that is: the last item added to the stack will be the first item popped out of the stack.


## Challenge
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue.

## Approach & Efficiency
I did the TDD approach to this project, which made it really easy for me to track my progress and make sure I am doing the right things.
The big O was O(1) for all methods, because of the way the linked lists were built.

## API

### Stack methods

* push

Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.
* pop

Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

* peek
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack

* is empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.

### Queue

* enqueue
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

* dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue

* peek
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack

* is empty
Arguments: none
Returns: Boolean indicating whether or not the queue is empty
