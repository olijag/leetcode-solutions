# https://leetcode.com/problems/add-two-numbers/description/?envType=list&envId=m9svb8n2

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def toReversedList(node: Optional[ListNode]) -> list:
            values = []
            while node:
                values.append(node.val)
                node = node.next
            values.reverse()
            return values

        def listToInteger(lst: list) -> int:
            return int("".join(map(str, lst)))

        l1_to_int = listToInteger(toReversedList(l1))
        l2_to_int = listToInteger(toReversedList(l2))

        answer = l1_to_int + l2_to_int
        res_list = [int(x) for x in str(answer)][::-1]

        # Convert list back to reversed linked list
        dummy_node = ListNode(0)
        current_node = dummy_node
        for num in res_list:
            current_node.next = ListNode(num)
            current_node = current_node.next

        return dummy_node.next
    

if __name__ == "__main__":
    solution = Solution()
