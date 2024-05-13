class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def create_listnode(self, data):
        return ListNode(data)
    
    def reverse_section(self, head, left, right):
        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Find the node before the start of the section to reverse
        while prev.next and prev.next.val != left:
            prev = prev.next
        
        # Start reversing from this node
        reverse_start = prev.next
        current = reverse_start.next
        prev_end = reverse_start
        
        # Continue until the end of the section to reverse
        while prev_end.val != right:
            prev_end = prev_end.next
        next_end = prev_end.next
        
        # Reverse the section
        prev_node = reverse_start
        while current != next_end:
            temp = current.next
            current.next = prev_node
            prev_node = current
            current = temp
        
        # Reconnect the reversed section back to the list
        prev.next = prev_node
        reverse_start.next = next_end
        
        return dummy.next
    
solution = Solution()
root = solution.create_listnode(1)
root.next = solution.create_listnode(2)
root.next.next = solution.create_listnode(3)
root.next.next.next = solution.create_listnode(4)
root.next.next.next.next = solution.create_listnode(5)
root.next.next.next.next.next = solution.create_listnode(6)

start = 1
end = 3

result = solution.reverse_section(root, start, end)  # Capture the returned head

current = result
while current is not None:
    print(current.val, end=" ")
    current = current.next
