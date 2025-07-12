
def mergeKLists(self, lists):

    def merge(l1, l2):

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l2.next
            else:
                curr.next =l2
                l2 = l2.next
            curr = cur.next

        curr.next = l1 if l1 else l2

        return dummy.next


    interval =1
    n = len(lists)
    while interval < n:
        for i in range(0, n -interval, interval*2):
            list[i] = merge(list[i], list[i+interval])
        interval *=2

    return list[0]