#! /usr/bin/python3

class Node:

    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.next = nxt
        self.prev = prev

class DLL:

    def __init__(self):
        self.begin = None
        self.end = None
        self.length = 0

    def push(self, val):
        if self._isempty():
            self.begin = Node(val)
            self.end = self.begin
            self.length += 1
        else:
            self.end.next = Node(val)
            self.end.next.prev = self.end
            self.end = self.end.next
            self.length += 1
        return self.end.value

    def pop(self):
        if self._isempty():
            return None
        if self._isonlyone():
            result = self.begin
            self.begin = self.end = None
            self.length -= 1
            return result.value
        else:
            result = self.end
            self.end = self.end.prev
            self._normalize()
            self.length -= 1 
            return result.value

    def shift(self, val):
        return self.push(val)        

    def unshift(self):
        if self._isempty():
            return None
        if self._isonlyone():
            result = self.begin
            self.begin = self.end = None
            self.length -= 1
            return result.value
        else:
            result = self.begin
            self.begin = self.begin.next
            self._normalize()
            self.length -= 1
            return result.value

    def remove(self, obj):
        if self._isempty():
            return None
        if self._isonlyone() and self.begin.value == obj:
            result = self.begin
            self.begin = None
            self.end = None
            self.length -= 1
            return 0
        if self.begin.value == obj:
            result = self.begin
            self.begin = self.begin.next
            self.length -= 1
            self._normalize()
            return 0 

        index = 0
        curr = self.begin
        while index <= self.length:
            if curr.value == obj:
                curr.prev.next = curr.next
                self._normalize()
                self.length -= 1
                return index 
            else:
                index += 1
                curr = curr.next
        return None 

    def first(self):
        return self.begin.value

    def last(self):
        return self.end.value

    def count(self):
        return self.length

    def get(self, index):
        if abs(index) < self.length:
            index = index if index >= 0 else abs(self.length + index)
            count = 0
            curr = self.begin
            while count <= index:
                if count == index:
                    return curr.value
                else:
                    curr = curr.next
                    count += 1
        return None

    def _normalize(self):
        if self.begin and self.end:
            self.begin.prev = None
            self.end.next = None

    def _isempty(self):
        if not self.begin and not self.end:
            return True
        else:
            return False

    def _isonlyone(self):
        if self.begin == self.end and self.begin:
            return True
        else:
            return False
