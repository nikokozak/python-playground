#! /usr/bin/python3

class Node:

    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class SLL:

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, val):
        if self.isempty():
            self.begin = Node(val)
            self.end = self.begin
            return self.end.val
        self.end.next = Node(val)
        self.end = self.end.next
        return self.end.val

    def shift(self, val):
        return self.push(val)

    def unshift(self):
        if self.isempty():
            return None
        if self.begin == self.end:
            result = self.begin
            self.begin = self.end = None
            return result.val
        result = self.begin
        self.begin = self.begin.next
        return result.val 

    def first(self):
        return self.begin.val

    def last(self):
        return self.end.val

    def get(self, index):
        return None if not self.getByIndex(index) else self.getByIndex(index).val

    def pop(self):
        if self.isempty():
            return None
        if self.begin == self.end:
            result = self.begin
            self.begin = self.end = None
            return result.val
        result = self.end
        self.end = self.getByIndex(-2)
        self.end.next = None
        return result.val

    def remove(self, val):
        if not self.begin and not self.end:
            return None
        def recurrRemove(val, index=0, curr=self.begin):
            if curr.val == val:
                if self.begin == self.end:
                    self.begin = self.end = None
                else:
                    if self.begin == curr:
                        self.begin = self.begin.next
                    else:
                        prev = self.getByIndex(index - 1)
                        prev.next = curr.next
                return index
            if curr.next == None and not curr.val == val:
                return None
            return recurrRemove(val, index + 1, curr.next)
        return recurrRemove(val)

    def getByIndex(self, index):
        index = index if index >= 0 else self.count() + index
        if index >= self.count():
            return None
        def recurrIndex(index=index, curr=self.begin):
            if not curr:
                return None
            if index == 0:
                return curr
            return recurrIndex(index - 1, curr.next)
        return recurrIndex()

    def count(self):
        def recurrCount(curr=self.begin):
            if not curr:
                return 0 
            if self.begin == self.end:
                return 1
            if not curr.next:
                return 1
            return 1 + recurrCount(curr.next)
        return recurrCount()

    def isempty(self):
        if self.begin == self.end == None:
            return true
        else:
            return false 



