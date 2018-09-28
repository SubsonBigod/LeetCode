class Solution:
    """ 61
    给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
    """
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        o_head = head
        length = 0
        while head is not None:
            length += 1
            if head.next is None:
                break
            head = head.next
        head.next = o_head
        n_tail = o_head
        for _ in range(length - (k % length) - 1):
            n_tail = n_tail.next
        n_head = n_tail.next
        n_tail.next = None
        return n_head
