# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x):
        # Time Complexity:  O(n)
        # Space Complexity: O(1) (Because creating ListNode use constant space and we are reusing existing Nodes)

        # Create two partitions to store Nodes less than/greater than or equal to x
        less, greater = ListNode(0), ListNode(0)

        less_head = less            # For returing final combined list
        greater_head = greater      # For linking last node of "less" to first node of "greater"

        cur = head

        while cur:
            # Place the Nodes into corresponding partitions
            if cur.val >= x:
                greater.next = cur
                greater = greater.next
            else:
                less.next = cur
                less = less.next
            cur = cur.next

        less.next = greater_head.next   # Link the two partitions
        greater.next = None             # Point to None to signify list end

        return less_head.next