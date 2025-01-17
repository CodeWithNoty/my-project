class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
         return super().pop()
        else:
           raise IndexError("stack is empty")
        
    def peek(self):
       if not self.is_empty():
          return self[-1]
       else:
          raise IndexError("stack is empty")
       
    def size(self):
       return len(self)
    
    def insert(self,inx,data):
       raise AttributeError("No attribute 'insert' in Stack")
    
s1=Stack()
s1.push(2)
s1.push(4)
s1.push(6)
s1.push(8)
s1.push(10)
print("top value is  ",s1.peek())
# print("removed value is ",s1.pop())
# print("removed value is ",s1.pop())
# print("removed value is ",s1.pop())
# print("removed value is ",s1.pop())
# print("removed value is ",s1.pop())
# print("top value is  ",s1.peek())


       
