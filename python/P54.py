class ListNode:
    def __init__(self,value ,next = None):
        self.value = value
        self.next = next

def mergeTwoLists(l1,l2):
    dummy = ListNode()
    curr = dummy

    while l1 and l2:
        if l1.value < l2.value:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if l1:
        curr.next = l1
    elif l2:
        curr.next= l2
    
    return dummy.next
def mergeKlists(lists):
    if not lists:
        return None
    
    interval = 1
    while interval <len(lists):
        for i in range(0,len(lists) - interval , interval*2):
            lists[i] = mergeTwoLists(lists[i] , lists[i+interval] if i +interval <len(lists) else None )

        interval *=2
    
    return lists[0]


