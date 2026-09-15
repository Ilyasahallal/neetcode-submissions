class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimum=None
        self.minimums=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum == None:
            self.minimum = val
        else :
            self.minimums.append(self.minimum)   
            if val<self.minimum :
                self.minimum = val
            

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.minimum = None
        else :
            self.minimum=self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
