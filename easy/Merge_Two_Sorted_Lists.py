# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/

'''
문제 요약: 정렬된 숫자 리스트 두개를 순서대로 합친 리스트를 반환하는 문제.
ask: 1 -> 2 -> 4, 1 -> 3 -> 4
answer: 1 -> 1 -> 2 -> 3 -> 4 -> 4

해석:
2개의 리스트를 합칠때 새로 만들 리스트 ans 와 위치를 옮겨다니는 pointer 두개를 선언.
순서대로 합치는 방법은 merge sort 방식과 같기 때문에 간단히 해결.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        pointer = ans
        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = ListNode(l1.val)
                pointer = pointer.next
                l1 = l1.next
            else:
                pointer.next = ListNode(l2.val)
                pointer = pointer.next
                l2 = l2.next
        pointer.next = l1 if l1 else l2
        return ans.next
