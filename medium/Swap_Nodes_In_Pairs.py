# Problem Link: https://leetcode.com/problems/swap-nodes-in-pairs/

'''
문제 요약: 링크드 리스트가 주어졌을때, 좌우 숫자를 바꿔서 반환하는 문제 (제약: 숫자만 바꾸는게 아니라 노드를 바꿔야함)
ask: 1 -> 2 -> 3 -> 4
answer: 2 -> 1 -> 4 -> 3

해석:
노드를 가리키는 포인터 두개를 가지고 홀수일때와 짝수일때 구분해서 해결.
홀수일때는 반복문 종료하고 바로 반환.
짝수일때는 p1의 위치를 한칸 더 뒤로 옮겨줘야 가운데 들어가는 값이 사라지지 않음.
(ex, p1.next를 바꿔주지 않고 p1, p2를 옮기면 2 -> 1 -> 3 과 같은 결과가 나옴)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p1, p2 = head, head.next
        head = head.next

        while p2:
            p1.next = p2.next
            p2.next = p1

            # Odd n
            if (not p1.next) or (not p1.next.next):
                break
            # Even n
            p2 = p1
            p1 = p1.next
            p2.next = p1.next
            p2 = p1.next

        return head