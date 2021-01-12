# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

'''
문제 요약: 링크드 리스트에서 중복숫자를 제거하는 문제.
ask: 1 -> 1 -> 2 -> 3 -> 3
answer: 1 -> 2 -> 3

해석:
링크드 리스트의 기본을 묻는 문제. 포인트 하나를 움직이면서, p1.next가 존재한다면 p1과 p1.next의 value를 비교.
만약 값이 같으면 p1을 한칸 옮겨주고 dup_start로(이전노드) p1을 가리켜 중간노드를 끊어줌.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p1 = head
        while p1:
            if p1.next and p1.val == p1.next.val:
                dup_start = p1
                while p1.next and p1.val == p1.next.val:
                    p1 = p1.next
                dup_start.next = p1.next
            else:
                p1 = p1.next
        return head