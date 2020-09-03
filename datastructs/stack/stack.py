#! /usr/bin/python3

class Node:

    def __init__(self, val):
        self.value = val
        self.next = None 

class Stack:

    def __init__(self):
        self.first = None
        self.length = 0

    def push(self, val):
        prev = self.first
        self.first = Node(val)
        self.first.next = prev
        self.length += 1
        return self.first.value
    
    def pop(self):
        if self.first:
            result = self.first
            self.first = self.first.next
            self.length -= 1
            return result.value
        else:
            return None

    def count(self):
        return self.length

    def top(self):
        if self.first:
            return self.first.value
        else:
            return None
