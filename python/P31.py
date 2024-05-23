import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, id(head), head))
    dummy = ListNode()
    curr = dummy

    while heap:
        val, node_id, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, id(node.next), node.next))

    return dummy.next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

merged = mergeKLists([list1, list2, list3])


curr = merged
while curr:
    print(curr.val, end=" ")
    curr = curr.next
