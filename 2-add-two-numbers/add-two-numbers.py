class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None
    ) -> ListNode | None:

        number1 = 0
        place = 1
        while l1:
            number1 += l1.val * place
            place *= 10
            l1 = l1.next

        number2 = 0
        place = 1
        while l2:
            number2 += l2.val * place
            place *= 10
            l2 = l2.next

        total = number1 + number2

        # Build the result linked list from the total's digits.
        if total == 0:
            return ListNode(0)

        dummy = ListNode()
        current = dummy

        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total //= 10

        return dummy.next