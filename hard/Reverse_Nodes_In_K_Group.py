# Problem Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

'''
문제 요약: 숫자가 포함된 링크드 리스트에서 k그룹씩 순서를 뒤집어 반환하는 문제. (단, memory space O(1)을 지키고, 노드안의 값을 바꿀순 없음)
ask: 1 -> 2 -> 3 -> 4 -> 5, k = 3
answer: 3 -> 2 -> 1 -> 4 -> 5

해석:
처음에는 직관적이게 k개씩 바꾸고 다음으로 넘어가는 방식으로 구현. 포인터가 여섯개나 필요하며 코드 자체를 보는데 난해함.
그래서 재귀함수를 통해 3개씩 끊어가면서 next_head를 리턴해 그룹간 연결하는 방식으로 구현.
재귀함수를 쓰면 뒤집는 함수를 구현하는데 3개정도의 포인터만 필요해서 코드 직관성도 생각보다 높고 훨씬 깔끔함.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        k_head = head
        for i in range(k):
            if not k_head:
                return head
            k_head = k_head.next
        next_head = self.reverseKGroup(k_head, k)

        for i in range(k):
            p = head.next
            head.next = next_head
            next_head = head
            head = p
        return next_head