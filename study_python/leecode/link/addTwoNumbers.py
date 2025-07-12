class ListNode():

    def __init__(self, val):
        self.val =val
        self.next = None



def addTwoNumbers(self, l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    dummy = ListNode(-1)
    curr = dummy
    carry =0

    while l1 or l2 or carry:

        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        total_sum = l1_val + l2_val + carry
        carry = total_sum//10
        digit = total_sum%10

        curr.next = ListNode(digit)

        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None


    return dummy.next

if __name__ == '__main__':
    pass