class Stack:
    def __init__(self, length):
        self.stack = []
        self.count = 0
        self.maxlength = length

    def isFull(self):
        if self.count == self.maxlength:
            return True
        else:
            return False

    def spaceAvailable(self):
        return self.maxlength-self.count

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def traverse(self):
        values = self.stack.copy()
        values.reverse()
        values = [str(i) for i in values]
        return "->".join(values)

    def add(self, value):
        if not self.isFull():
            self.stack.append(value)
            self.count += 1
            return "Value added!"
        return "Space is not available."

    def get(self):
        if not self.isEmpty():
            s = self.stack.pop(-1)
            self.count -= 1
            return s
        return "Stack is Empty."

    def Top(self):
        if not self.isEmpty():
            return self.stack[-1]
        return "Stack is empty"


class Solution:
    def ispar(self,x):
        # code here
        x = list(x)
        balanced = False
        bracket = {"}": "{", "]": "[", ")": "("}
        s = Stack(len(x))
        for i in x:
            if i in list(bracket.values()):
                s.add(i)

            if (i in list(bracket.keys())) and (i not in list(bracket.values())):
                if s.Top() != bracket[i]:
                    return balanced
                else:
                    if s.Top()==bracket[i]:
                        s.get()
            # print(s.traverse())
        if s.isEmpty():
            return not balanced
        else:
            return balanced


so = Solution()
print(so.ispar("{}{(}))}"))