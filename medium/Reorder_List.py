# Problem Link: https://leetcode.com/problems/reorder-list/

'''
문제 요약: 링크드 리스트의 처음과 끝이 순서대로 오는 형식의 순서로 만드는 문제. (단, val값을 바꾸는게 아닌 노드 자체를 바꿔야 함)
ask: 1 -> 2 -> 3 -> 4
answer: 1 -> 4 -> 2 -> 3

해석:
Array의 형식을 가지는 해쉬맵을 만들어서 해결. d 라는 딕셔너리 형식으로 키를 index, 밸류를 Node로 저장.
사이클이 되는걸 방지하기 위해서 저장할때 node의 next를 모두 None으로 만들어 단일 노드로 저장.
이후, 처음과 끝에서 부터 하나씩 줄여나가면서 노드들을 연결시키면 해결.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        d = {}
        index = 0
        while cur:
            d[index] = cur
            cur = cur.next
            d[index].next = None
            index += 1
        i, j = 0, index-1
        new_head = ListNode(-1)
        while i < j:
            new_head.next = d[i]
            new_head.next.next = d[j]
            new_head = new_head.next.next
            i += 1
            j -= 1
        if i == j:
            new_head.next = d[i]