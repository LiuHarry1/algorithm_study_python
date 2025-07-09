# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        nodeB = headA

        while nodeA != nodeB:
            if nodeA:
                nodeA =  nodeA.next
            else:
                nodeA = headB

            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA
            # nodeA = (nodeA == None)? headB: nodeA.next
            # nodeB = (nodeB == None)? headA: nodeB.next

        return nodeA
