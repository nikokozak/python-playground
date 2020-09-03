
class Node:

    def __init__(self, val, nxt):
        self.val = val
        self.next = nxt

class SLL:

    def __init__(self):
        self.begin = None
        self.end = None
        self.length = 0

    def push(self, val):
        if not self.begin:
            self.begin = Node(val, None)
            self.end = self.begin
            self.length += 1
        else:
            self.end.next = Node(val, None)
            self.end = self.end.next
            self.length += 1

    def pop(self):
        if self.end:
            result = self.end
            self.end = self.findByIndex(-2)
            self.end.next = None
            self.length -= 1
            return result.val
        else:
            return None

    def shift(self, val):
        self.push(val)

    def unshift(self):
        result = self.begin
        if self.length >= 1:
            self.begin = result.next
            self.length -= 1
            return result.val
        else:
            self.length -= 1
            return None

    def remove(self, val):
        if val == 0:
            return self.unshift()
        elif val == -1 or val == self.length - 1:
            return self.pop()
        else:
            result = self.findByIndex(val)
            prev = self.findByIndex(val - 1)
            nxt = self.findByIndex(val + 1)
            prev.next = nxt
            self.length -= 1
            return result.val

    def delete(self, val):
        if self.begin.val == val:
            return self.unshift()
        elif self.end.val == val:
            return self.pop()
        else:
            for i in range(1, self.length - 1):
                if self.findByIndex(i).val == val:
                    return self.remove(i)

    def count(self):
        return self.length

    def get(self, val):
        return self.findByIndex(val).val

    def findLast(self):
        finished = False
        currentNode = self.begin
        while not finished:
            if currentNode.next:
                currentNode = currentNode.next
            else:
                finished = True
        return currentNode

    def findByIndex(self, index):
        result = self.begin
        index = index if index >= 0 else self.length + index
        if (index > self.length - 1):
            return None
        for i in range(index):
            result = result.next if result.next else result
        return result
        
    def debug(self):
        print(self.begin.val, self.end.val)

