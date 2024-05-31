import heapq

num =[10,5,20,15,8,25]

sorted_num = []

heap = [-x for x in num]
heapq.heapify(heap)
while heap:
    sorted_num.append(-heapq.heappop(heap))

print(sorted_num)

