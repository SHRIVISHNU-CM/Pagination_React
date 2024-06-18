class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isEmpty():
            return None
        else:
            popednode = self.head
            self.head = self.head.next
            popednode.next = None
            return popednode.data
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
    def display(self):
        iternode = self.head
        if self.isEmpty():
            print("stack underflow")
        else:
            while(iternode != None):
                print(iternode.data,end=" ")
                iternode = iternode.next
                if(iternode !=None):
                    print("->",end=" ")
            return
if __name__=="__main__":
    mystack = Stack()
    mystack.push(11)
    mystack.push(16)
    mystack.push(32)
    mystack.push(44)
    mystack.display()

    print("\n Top element is " ,mystack.peek())
    mystack.pop()
    mystack.display()
    print("\nTop element is", mystack.peek())
            