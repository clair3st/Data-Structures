# Data-Structures [![Build Status](https://travis-ci.org/clair3st/Data-Structures.svg?branch=master)](https://travis-ci.org/clair3st/Data-Structures) [![Coverage Status](https://coveralls.io/repos/github/clair3st/Data-Structures/badge.svg?branch=master)](https://coveralls.io/github/clair3st/Data-Structures?branch=master)
Implementation of simple data structures in Python.

_____________

## Linked List

A singly linked list is made of nodes which contain a reference (or pointer) to the next node in the list and data. They are one of the simpliest data structures and can be used to implement other abstract data types including lists, stacks, queues etc.

![linked list](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/816px-Singly-linked-list.svg.png)

Advatange of a Linked list is a dynamic data structure which can grow while program is running (unlike arrays). Insertion and deletion methods are easy to implement, and it is a simple building block for other more complex data structures. 

The disadvantages of using a linked list is they use more memory than an array. Nodes must be read in order from the head to the tail (sequential access). Hard to reverse traverse a single linked list.

- **Module:** [linked_list.py](src/linked_list.py)

- **Tests:** [test_linked_list.py](tests/test_linked_list.py)

- **Resources:**
https://codefellows.github.io/sea-python-401d5/assignments/linked_list.html
http://greenteapress.com/thinkpython/html/chap17.html
https://medium.freecodecamp.com/a-gentle-introduction-to-data-structures-how-linked-lists-work-5adc793897dd#.34gncxsx5

The list implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **push(val)**   | insert the value ‘val’ at the head of the list. | O(1)           |
| **pop()**      | removes the first value off the head of the list and return it      |   O(1)           |
| **size()** | return the length of the list      |    O(1)            |
| **search(val)** | return the node containing ‘val’ in the list, if present, else None      |    O(n)            |
| **remove(node)** | remove the given node from the list, wherever it might be (node must be an item in the list)      |    O(n)            |
| **display()** | return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”  |    O(n)            |
 
___________________
