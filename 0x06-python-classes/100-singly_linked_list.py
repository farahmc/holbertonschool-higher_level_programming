#!/usr/bin/python3
"""
class Node that defines a node of a singly linked list
"""


class Node:
    """
    class Node
    """

    def __init__(self, data, next_node=None):
        """
        Instantiate with data and next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Return data of Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set data of Node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Return node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set node
        """
        if value is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Define a singly linked list
    """

    def __init__(self):
        """
        Instantiate
        """
        self.__head = head

    def sorted_insert(self, value):
        """
        Insert a node to the linked list at the correct position
        """
        pass
