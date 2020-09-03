#! /usr/bin/python3

class Node:

    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class Q:

    def __init__(self):
        self.begin = None
        self.end = None
        self.length = 0

    def push(self, val):
        if self._isempty():
            self.end = Node(val)
            self.begin = self.end
            self.length += 1
            return self.begin.val
        else:
            self.end.next = Node(val, None, self.end)
            self.end = self.end.next
            self.length += 1
            return self.end.val

    def shift(self, val):
        return self.push(val)

    def pop(self):
        if self._isempty():
            return None
        if self._isonlyone():
            result = self.begin
            self.begin = self.end = None
            self.length -= 1
            return result.val
        else:
            result = self.begin
            self.begin = self.begin.next
            self.begin.prev = None
            self.length -= 1
            return result.val

    def unshift(self):
        return self.pop()

    def first(self):
        return self.begin.val

    def last(self):
        return self.end.val

    def count(self):
        if not self._isempty():
            count = 1
            curr = self.begin
            while curr.next:
                curr = curr.next
                count += 1
            return count
        return 0

    def _isempty(self):
        if self.begin == self.end == None:
            return True
        else:
            return False

    def _isonlyone(self):
        if self.begin == self.end and self.begin:
            return True
        else:
            return False

