import sys

class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution(object):
    def createListNode(self, data):
        return ListNode(data)
    
    def deleteDuplicates(self, head):
        if head is None:
            return None
        
        # Use a dummy node to simplify edge cases
        dummy = ListNode(0, next=head)
        prev = dummy
        current = head
        
        # First pass to find the duplicate number
        while current is not None:
            if current.next is not None and current.val == current.next.val:
                dup_num = current.val
                print("Duplicate Number: " + str(dup_num))
                break
            current = current.next
        
        # Second pass to remove all instances of the duplicate number
        current = dummy
        while current is not None:
            if current.next is not None and current.next.val == dup_num:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next  # Return the next of dummy to get the actual head

solution = Solution()

root = solution.createListNode(1)
root.next = solution.createListNode(2)
root.next.next = solution.createListNode(2)
root.next.next.next = solution.createListNode(2)
root.next.next.next.next = solution.createListNode(3)
root.next.next.next.next.next = solution.createListNode(4)

root = solution.deleteDuplicates(root)

current = root
while current is not None:
    print(current.val, end=" ")
    current = current.next
