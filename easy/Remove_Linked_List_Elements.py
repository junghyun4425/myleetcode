# Problem Link: https://leetcode.com/problems/remove-linked-list-elements/

'''
문제 요약: 링크드리스트에서 val 값과 같은 값을 가지는 링크를 지우는 문제.
ask: 1->2->6->3->4->5->6, val = 6
answer: 1->2->3->4->5

해석:
숫자를 지우는데 중복이 있기때문에 도중에 지웠다고 멈춰서는 안됨.
처음엔 prev와 head 두 포인터로 진행해나가면서 작업을 수행했는데 head에 none이 나올때와 값을 삭제할때 두 포인터의 관계가 복잡해짐.
따라서 prev 하나로 next와 next.next를 활용해 간편하게 지워줌.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        start = ListNode(-1, head)
        prev = start
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return start.next