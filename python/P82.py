def Print(queue):
    while (len(queue) > 0):
        print(queue[0],end=" ")
        queue.pop(0)
def reverseQueue(q):
    if len(q) == 0:
        return
    fr = q[0]
    q.pop(0)
    reverseQueue(q)
    q.append(fr)
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
reverseQueue(queue)
print(queue)
