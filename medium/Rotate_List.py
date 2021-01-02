# Problem Link: https://leetcode.com/problems/rotate-list/submissions/

'''
문제 요약: 숫자를 값으로 가진 링크드 리스트의 순서를 k번 만큼 뒤집어 head를 반환하는 문제.
ask: 1 -> 2 -> 3 -> 4 -> 5, k = 2
answer: 4 -> 5 -> 1 -> 2 -> 3

해석:
우선 리스트를 탐색해서 size를 알아내고 tail을 링크드 리스트의 끝을 가리킴.
k를 반복되는 숫자만큼 제거시키고 새로운 꼬리가 가리킬 곳을 구함.
그리고 기존의 꼬리를 head에 연결시켜 순환 링크드 리스트를 만듬.
head를 new_tail 다음곳으로 옮긴뒤, new_tail이 가리키는 곳을 None으로 만들면 끝.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head.next == None:
            return head
        tail = new_tail = head
        l_len = 1
        while tail.next:
            tail = tail.next
            l_len += 1

        k = l_len - (k % l_len)
        for _ in range(k - 1):
            new_tail = new_tail.next

        if k != 0:
            tail.next = head
            head = new_tail.next
            new_tail.next = None
        return head