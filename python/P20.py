from collections import deque

class Stack:
    def __init__(self):
        self.dequeue = deque()

    def push(self,item):
        self.dequeue.append(item)

    def pop(self):
        return self.dequeue.pop()
    
    def size(self):
        return len(self.dequeue)
    
    def isempty(self):
        return not self.dequeue
    
    def top(self):
        if self.isempty():
            return None
        else:
            return self.dequeue[-1]
        

if __name__ == '__main__':
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print("current", st.size())
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
    print("curr",st.size())