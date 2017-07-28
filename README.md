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

## Stack

A stack is a collection of nodes with operations occuring at one end only. It behaves like a real-world stack or pile of books - books can only be taken from  or placed on the top of the pile in a First In Last Out (LIFO) operations.

![stack](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/440px-Data_stack.svg.png)

Stacks are handy for remembering state eg undo and redo

- **Module:** [stack.py](src/stack.py)

- **Tests:** [test_stack.py](tests/test_stack.py)

- **Resources:**
https://codefellows.github.io/sea-python-401d5/assignments/stack.html
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
https://en.wikibooks.org/wiki/Data_Structures/Stacks_and_Queues


The Stack implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **push(val)**   | insert the value ‘val’ at the head of the stack. | O(1)           |
| **pop()**      | removes the first value off the head of the stack and return it      |   O(1)        |

_____________

## Double Linked List

A doubly linked list is made of nodes which contain a reference (or pointer) to the next node in the list, and the previous node in the list plus data. 

![doubly linked list](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)

Advatange of a doubly linked list is two directional pointers allow traversal of the list in either direction.

The disadvantages of using a doubly linked list is they use more memory than a singly linked list and adding or removing a node requires changing more pointers.

- **Module:** [dll.py](src/dll.py)

- **Tests:** [test_dll.py](tests/test_dll.py)

- **Resources:**
https://codefellows.github.io/sea-python-401d5/assignments/doubly_linked_list.html
https://codefellows.github.io/sea-python-401d5/lectures/double_linked_list.html
https://en.wikipedia.org/wiki/Doubly_linked_list


The list implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **push(val)**   | will insert the value ‘val’ at the head of the list. | O(1)           |
| **pop()**      | will pop the first value off the head of the list and return it     |   O(1)        |
| **append(val)**   | will insert the value ‘val’ at the tail of the list. | O(1)           |
| **shift()**      | will pop the first value off the tail of the list and return it     |   O(1)        |
| **remove(val)** | will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise an appropriate Python exception.   |    O(n)            |

_____________


## Queue

A queue is an ordered collection of nodes with operations only allowing the addition of new nodes to the tail and removing nodes from the head of the collection. The Queue is called a First In First Out (FIFO) data structure for this reason. 

<img alt="Queue" align="middle" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png" width="500">

Queues are used in computer science exactly like they are in the physical world, that is, they are a buffer and store data until it will later get processed. They have limited access (only insert at the tail) and they can always be added to (the length is unlimited).

- **Module:** [a_queue.py](src/a_queue.py)

- **Tests:** [test_queue.py](tests/test_queue.py)

- **Resources:**
https://codefellows.github.io/sea-python-401d5/assignments/queue.html
https://codefellows.github.io/sea-python-401d5/lectures/queue.html
http://www.princeton.edu/~achaney/tmve/wiki100k/docs/Queue_(data_structure).html


The Queue implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **enqueue(value)**   | adds value to the queue | O(1)           |
| **dequeue()**      | removes the correct item from the queue and returns its value (should raise an error if the queue is empty)  |   O(1)        |
| **peek()**   | returns the next value in the queue without dequeueing it. If the queue is empty, returns None | O(1)           |
| **size()**      | return the size of the queue. Should return 0 if the queue is empty     |   O(1)        |

_____________

## Deque

Deque is a queue that can be accessed from both ends.

![Deque](http://www.codeproject.com/KB/recipes/669131/deque.png)

Deques are useful when modeling any kind of real-world waiting line. This is where entities (bits, people, cars, words, particles etc) arrive with a certain frequency and the front of the line is serviced at a different frequency. 

- **Module:** [deque.py](src/deque.py)

- **Tests:** [test_deque.py](tests/test_deque.py)

- **Resources:**
http://stackoverflow.com/questions/3880254/why-do-we-need-deque-data-structures-in-the-real-world
https://codefellows.github.io/sea-python-401d5/lectures/deque.html
https://codefellows.github.io/sea-python-401d5/assignments/deque.html

The Deque implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **append(val)**   | adds value to the end of the deque | O(1)           |
| **appendleft(val)**      | adds a value to the front of the deque  |   O(1)        |
| **pop()**   | removes a value from the end of the deque and returns it (raises an exception if the deque is empty) | O(1)           |
| **popleft()**      | removes a value from the front of the deque and returns it (raises an exception if the deque is empty)     |   O(1)        |
| **peek()**      | returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)   |   O(1)        |
| **peekleft()**      | returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)     |   O(1)        |
| **size()**      | returns the count of items in the queue (returns 0 if the queue is empty) |   O(1)        |

_____________

## Binary Heap

A binary heap is a heap data structure that takes the form of a binary tree. Heaps where the parent node is greater than or equal to the child node are called max-heaps; those where it is less than or equal to are called min-heaps.

Heaps are commonly implemented with an array. Any binary tree can be stored in an array, but because a binary heap is always a complete binary tree (only the bottom layer can be partially unfilled), it can be stored compactly. No space is required for pointers; instead, the parent and children of each node can be found by arithmetic on array indices. 

![Binary Heap](https://upload.wikimedia.org/wikipedia/commons/6/60/Binary_heap_indexing.png)

The advantages of a binary heap is due to the heap property it provides efficient search. I also sorts the tree in place and is easy to retrieve top N items


- **Module:** [binheap.py](src/binheap.py)

- **Tests:** [test_binheap.py](tests/test_binheap.py)

- **Resources:**
https://codefellows.github.io/sea-python-401d5/lectures/heap.html
https://codefellows.github.io/sea-python-401d5/assignments/binary_heap.html
https://en.wikipedia.org/wiki/Binary_heap

The heap implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **push(val)**   | puts a new value into the heap, maintaining the heap property. | Ave: O(1), Worst: O(log n)           |
| **pop()**      | removes the “top” value in the heap, maintaining the heap property.      |   O(log n)           |
| **display()** | returns a string representation of the tree     |    O(n)            |

_____________

## Priority Queue

Priority Q is like a regular queue with the added element of a 'priority'. Elements with a higher priority is severed before elements of a lower priority. If two elements have the same priority they are served based on their order in the queue.

<img alt="Priority Q" align="middle" src="https://netmatze.files.wordpress.com/2014/08/priorityqueue.png?w=590&h=470" width="500">

Priority Queues are very useful for situations when you need to process items in a particular order, but not necessarily in full sorted order and not all at the same time.


- **Module:** [priorityq.py](src/priorityq.py)

- **Tests:** [test_priorityq.py](tests/test_priorityq.py)

- **Resources:**
https://codefellows.github.io/sea-python-401d5/assignments/priority_queue.html
https://en.wikipedia.org/wiki/Priority_queue

The priorityq implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **insert(val, [priority])**   | puts a new value into the queue, maintaining the heap property. |  O(log n)           |
| **pop()**      | removes the most important item from the queue.      |   O(log n)           |
| **peek()** | returns the most important item without removing it from the queue    |    O(1)            |

_____________

## Graph

Graphs allow for a representation of relationship between different nodes. There are two parts to a graph, the nodes themselves and the connections (referred to as edges) which represent the relationship between each node. Connections can be directed (the relationship exists in only one direction) or undirected (the relationship exisits in both directions)

![Undirected Graph](http://www.algolist.net/img/graphs/graph-def-2.png) ![Directed Graph](http://www.algolist.net/img/graphs/graph-def-3.png)

- **Module:** [graph.py](src/graph.py)

- **Tests:** [test_graph.py](tests/test_graph.py)

- **Resources:**
https://codefellows.github.io/sea-python-401d5/assignments/graph_1.html?highlight=graph
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
https://medium.freecodecamp.com/a-gentle-introduction-to-data-structures-how-graphs-work-a223d9ef8837

The graph implementation supports the following methods:

| Method        | Description   | Time Complexity  |
| ------------- |-------------| :---------------:|
| **nodes()**   | return a list of all nodes in the graph. | O(n)          |
| **edges()**   | return a list of all edges in the graph.     |   O(n)            |
| **add_node(n)**      | adds a new node 'n' to the graph.     |   O(1)       |
| **add_edge(n1, n2)** |  adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not already present in the graph, they should be added.    |    O(1)             |
| **del_node(n)**      | deletes the node 'n' from the graph, raises an error if no such node exists.     |   O(1)            |
| **del_edge(n1, n2)**      | deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no such edge exists.    |   O(1)           |
| **has_node(n1, n2)**      | True if node 'n' is contained in the graph, False if not.    |   O(1)           |
| **neighbors(n1, n2)**      | returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g.    |   O(1)           |
| **adjacent(n1, n2)**      | returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g.    |   O(1)           |

_____________

## Binary Search Tree

Binary Search Tree (BST) is a data structure used to map from key to value. A binary search tree relies on the property that keys that are less than the parent are found in the left subtree, and keys that are greater than the parent are found in the right subtree.

If the tree is empty, then a new node inserted into the tree becomes the tree’s root. The next node inserted will have its key compared to the key of the root node. If lower, it will occupy the “left” attribute of the root node. If higher, it occupies the “right” attribute. If a node tries to occupy the “left” or “right” attribute of the root and that attribute is already occupied, it moves down the tree to that node and has its key compared again.

![Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png) 

Binary Search Trees are a popular data structure choice in computing because of its efficient sorting and searching of data. On average, each comparison allows searching to ignore half of the tree. As such, each search takes time proportional to the logarithm of the number of items stored in the tree.

- **Module:** [bst.py](src/bst.py)

- **Tests:** [test_bst.py](tests/test_bst.py)

- **Resources:**
https://codefellows.github.io/sea-python-401d6/assignments/bst_1.html
https://codefellows.github.io/sea-python-401d5/assignments/bst_3_traversals.html
https://codefellows.github.io/sea-python-401d5/assignments/bst_3_delete.html
https://codefellows.github.io/sea-python-401d6/lectures/binary_search_tree1.html
https://en.wikipedia.org/wiki/Tree_traversal

This BST implementation `Bst()` supports the following methods.

 Method        | Description   | Time Complexity  
 ------------- |-------------| :---------------:
 **insert(val)**   | insert the value val into the BST. If val is already present, it will be ignored. |    Best: O(log n),<br> Worst: O(n)      
 **search(val)**   | return the node containing that value, else None     |    Best: O(log n), <br>Worst: O(n)         
 **size()**      | will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.     |    O(1)     
 **depth()** |  will return an integer representing the total number of levels in the tree. If there are no values, depth is 0, if one value the depth should be 1, if two values it will be 2, if three values it may be 2 or 3, depending, etc.     |      O(1)        
 **contians(val)**      | will return True if val is in the BST, False if not     |      Best: O(log n), <br>Worst: O(n)        
 **balance()**      | will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.    |     O(1)     
 **in_order():** |return a generator that will return the values in the tree using in-order traversal, one at a time. | O(n)
**pre_order():** |return a generator that will return the values in the tree using pre-order traversal, one at a time. | O(n)
**post_order():** | return a generator that will return the values in the tree using post-order traversal, one at a time. | O(n)
**breadth_first():** | return a generator that will return the values in the tree using breadth frist traversal, one at a time. | O(n)
**delete(val):** |removes a node from the list. | O(logn)
   

**Tree traversals**

This is the process of visiting each node in the tree once. Trees may be traversed in multiple ways so the output of nodes depends on the method used.

 - Depth first Traversals:
    - Pre-order traversal: F, B, A, D, C, E, G, I, H. <br>
    ![Pre-order](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Sorted_binary_tree_preorder.svg/440px-Sorted_binary_tree_preorder.svg.png)
    - In-order traversal: A, B, C, D, E, F, G, H, I. <br>
    ![In-order](https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Sorted_binary_tree_inorder.svg/440px-Sorted_binary_tree_inorder.svg.png)
    - Post-order traversal: A, C, E, D, B, H, I, G, F. <br>
    ![Post-order](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Sorted_binary_tree_postorder.svg/440px-Sorted_binary_tree_postorder.svg.png)
- Breadth first Traversal:
    - Level-order: F, B, G, A, D, I, C, E, H. <br>
    ![Level-order](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Sorted_binary_tree_breadth-first_traversal.svg/440px-Sorted_binary_tree_breadth-first_traversal.svg.png)
