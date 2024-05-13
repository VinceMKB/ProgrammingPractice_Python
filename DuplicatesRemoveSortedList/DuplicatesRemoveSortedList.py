import sys

class ListNode(object):
    def __init__(self, val = 0, next = None):
            self.val = val
            self.next = next


class Solution(object):
      def creatreListNode(self, data):
            return ListNode(data)
      
      def deleteDuplicates(self, head):
            if head is None:
                  return None
            
            current = head
            while current.next is not None:
                if current.val == current.next.val:
                    current.next = current.next.next
                else:
                    current = current.next

            return head
                      
solution = Solution()

head = solution.creatreListNode(1)
head.next = solution.creatreListNode(2)
head.next.next = solution.creatreListNode(2)
head.next.next.next = solution.creatreListNode(4)

head = solution.deleteDuplicates(head)

current = head
while current is not None:
    print(current.val, end=" ")
    current = current.next

