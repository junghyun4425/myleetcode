# Problem Link: https://leetcode.com/problems/reverse-linked-list-ii/

'''
문제 요약: 링크드 리스트의 m번 부터 n번 까지 뒤집어 반환하는 문제.
ask: 1 -> 2 -> 3 -> 4 -> 5, m=2, n=4
answer: 1 -> 4 -> 3 -> 2 -> 5

해석:
1차원적인 방법으로 start, last를 찾고 재귀함수를 통해 하나씩 뒤집어가는 방법으로 시도했었음.
하지만 굉장히 많은 예외를 마주치면서 if문이 늘어나고 결국 방법을 바꾸기로 결정.
새로운 방법은 노드를 바꾸는게 아니라 그냥 값만 바꾸는 방법.
left는 바꿔야하는 시점 이후에 오히려 증가해야하기 때문에 인자로 넣지 않음.
right는 반대로 감소해야 하므로 재귀를 통해 돌아오면서 수행.
절반까지 오면 멈춰야 하기 때문에 half라는 트리거를 활용해 멈춤.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        half = False
        left = head
        def recursion(right, l):
            nonlocal half, left
            if l == n:
                return
            if l < m:
                left = left.next
            right = right.next
            recursion(right, l+1)
            if left == right or right.next == left:
                half = True
            if not half:
                left.val, right.val = right.val, left.val
                left = left.next
        recursion(head, 1)
        return head