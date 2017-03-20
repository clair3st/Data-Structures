# Data-Structures
Implementation of simple data structures in Python.

_____________

## Linked List

A singly linked list is made of nodes which contain a reference (or pointer) to the next node in the list. Each node also contains data.

- *Module:* [linked_list.py](src/linked_list.py)

- *Tests:* [test_linked_list.py](tests/test_linked_list.py)

- *Resources:* https://codefellows.github.io/sea-python-401d5/assignments/linked_list.html
http://greenteapress.com/thinkpython/html/chap17.html
https://medium.freecodecamp.com/a-gentle-introduction-to-data-structures-how-linked-lists-work-5adc793897dd#.34gncxsx5

The list implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |:-------------:| :---------------:|
| *push(val)*   | insert the value ‘val’ at the head of the list. | O(1)           |
| *pop()*      | removes the first value off the head of the list and return it      |   O(1)           |
| *size()* | return the length of the list      |    O(1)            |
| *search(val)* | return the node containing ‘val’ in the list, if present, else None      |    O(n)            |
| *remove(node)* | remove the given node from the list, wherever it might be (node must be an item in the list)      |    O(n)            |
| *display()* | return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”  |    O(n)            |
 
___________________