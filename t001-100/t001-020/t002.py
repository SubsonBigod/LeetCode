
from t000 import ListNode, list_to_link, link_to_list


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        over = (l1.val + l2.val) // 10
        remainder = (l1.val + l2.val) % 10
        result = ListNode(remainder)
        res = result
        l11 = l1.next
        l22 = l2.next
        while l11 is not None or l22 is not None:
            curr_sum = over
            if l11 is not None:
                curr_sum += l11.val
                l11 = l11.next
            if l22 is not None:
                curr_sum += l22.val
                l22 = l22.next
            over = curr_sum // 10
            remainder = curr_sum % 10
            res.next = ListNode(remainder)
            res = res.next
        if over == 1:
            res.next = ListNode(1)
        return result


if __name__ == "__main__":
    func = Solution().addTwoNumbers
    assert [7, 0, 8] == link_to_list(
                  func(
                      list_to_link([2, 4, 3]),
                      list_to_link([5, 6, 4])
                  ))
    assert [9, 9, 4] == link_to_list(
                  func(
                      list_to_link([4, 3]),
                      list_to_link([5, 6, 4])
                  ))
    assert [7, 0, 4] == link_to_list(
                  func(
                      list_to_link([2, 4, 3]),
                      list_to_link([5, 6])
                  ))
    assert [8, 6, 4] == link_to_list(
                  func(
                      list_to_link([3]),
                      list_to_link([5, 6, 4])
                  ))
    assert [8, 4, 3] == link_to_list(
                  func(
                      list_to_link([2, 4, 3]),
                      list_to_link([6])
                  ))
    assert [4, 5, 6, 4] == link_to_list(
                  func(
                      list_to_link([3]),
                      list_to_link([1, 5, 6, 4])
                  ))
    assert [7, 2, 4, 3] == link_to_list(
                  func(
                      list_to_link([1, 2, 4, 3]),
                      list_to_link([6])
                  ))
    assert [0] == link_to_list(
                  func(
                      list_to_link([0]),
                      list_to_link([0])
                  ))
    assert [0, 1] == link_to_list(
                  func(
                      list_to_link([5]),
                      list_to_link([5])
                  ))
    assert [0, 0, 1] == link_to_list(
                  func(
                      list_to_link([1]),
                      list_to_link([9, 9])
                  ))
    assert [0, 0, 1] == link_to_list(
                  func(
                      list_to_link([9, 9]),
                      list_to_link([1])
                  ))
    assert [0, 0, 0, 1] == link_to_list(
                  func(
                      list_to_link([1]),
                      list_to_link([9, 9, 9])
                  ))
    assert [0, 0, 0, 1] == link_to_list(
        func(
            list_to_link([9, 9, 9]),
            list_to_link([1])
        ))
