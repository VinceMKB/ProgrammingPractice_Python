import sys

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def create_listnode(self, data):
        return ListNode(data)
    
    def swapPairs(self, head):
        dummy = self.create_listnode(-1)
        dummy.next = head
        prev = dummy

        while head != None and head.next != None:
            #Nodes to be swapped
            first = head
            second = head.next

            #Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            #Reinitializing the head and prev for next swap
            prev = first
            head = first.next
            
        return dummy.next


solution = Solution()
root = solution.create_listnode(1)
root.next = solution.create_listnode(2)
root.next.next = solution.create_listnode(3)
root.next.next.next = solution.create_listnode(4)

result = solution.swapPairs(root)

current = result
while current is not None:
    print(current.val, end=" ")
    current = current.next

