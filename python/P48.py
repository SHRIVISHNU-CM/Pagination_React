import heapq

nums = [10,5,20,15,8,25]

sorted_num = []
heap = nums[:]
print(heap)

heapq.heapify(heap)

while heap:
    sorted_num.append(heapq.heappop(heap))
print(sorted_num)