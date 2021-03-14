# Problem Link: https://leetcode.com/problems/palindrome-linked-list/

'''
문제 요약: 링크드 리스트가 palindrome 한지 확인하는 문제. (제약조건은 공간복잡도 O(1))
ask: 1->2->2->1
answer: True

해석:
쉬운 난이도 치고는 제법 머리를 많이 굴린 문제.
당연히 저 제약조건만 없다면 금방 해결할 수 있었겠지만 이부분을 해결하려고 별생각을 다함.
첫번째로 재귀함수 + nonlocal로 해결.
head와 재귀함수를 통해 반대 방향으로 오는 recursion_head 두개를 비교해가면서 해결해봤지만 아무래도 nonlocal의 영향으로 성능이 좋지 않음.

다른 대안으로 slow, fast move 를 활용하기로 함. fast가 2칸씩 움직이고 slow가 한칸씩 움직이는데, fast가 끝에 도달하면 slow는 가운데 도착.
slow를 가운데로 오면서 pre라는 포인터로 역방향으로 가도록 노드의 .next값을 바꿔줌.
그러면 가운데서부터 slow는 오른쪽으로, pre는 왼쪽으로 진행하면서 .val값을 비교함.
결과는 재귀함수 + nonlocal보다 시간, 메모리 양쪽에서 뛰어난 성능 향상을 가짐.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, pre = pre, slow.next, slow
        if fast:
            slow = slow.next
        while slow and slow.val == pre.val:
            slow = slow.next
            pre = pre.next
        return not slow