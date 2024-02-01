#!/usr/bin/python3

"""Singly LL and Node
Singly Linked List and Node
"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Singly LL class"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        data = []
        while current is not None:
            data.append(str(current.data))
            current = current.next_node
        return "\n".join(data)

    def sorted_insert(self, value):
        new = Node(value, None)

        if self.__head is None:
            self.__head = new
            # print(new.data, new, new.next_node)
            return
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            prev = self.__head
            current = self.__head.next_node
            while current is not None:
                # print(current.data, current, current.next_node)
                # Bug worth unforgetfulness was here
                if current.data > value:
                    prev.next_node = new
                    new.next_node = current
                    return
                prev = current
                current = current.next_node
            prev.next_node = new
