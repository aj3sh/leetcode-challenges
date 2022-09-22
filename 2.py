"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_out: int = 0
        root_node, prev_node = ListNode(), None
        current_node = root_node
            
        while l1 != None or l2 != None:
            # adding all for current node
            node_sum = carry_out + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            
            # adding to List Node
            current_node.val = node_sum % 10
            current_node.next = ListNode()
            prev_node, current_node = current_node, current_node.next
            
            # taking out carry
            carry_out = node_sum // 10
            
            # traversing to next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry_out != 0:
            current_node.val = carry_out
        elif prev_node:
            prev_node.next = None
        
        return root_node
            
# Time Complexity: O(n)
# Space Complexity: O(1)