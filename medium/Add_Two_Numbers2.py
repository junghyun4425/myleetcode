# Problem Link: https://leetcode.com/problems/add-two-numbers-ii/

'''
문제 요약: 한자리 수 씩 나열된 링크드 리스트 두개를 더하는 문제.
ask: l1 = [2,4,3], l2 = [5,6,4]
answer: [8,0,7]

해석:
간단하게 링크드 리스트에 존재하는 숫자들을 탐색을통해 합쳐서 더한다음 다시 만들어 줌.
사실 스택으로 풀면 str int 전환하지 않고 한자리수 씩 풀어나가는 방법도 있긴 하지만, 제약조건에 따로 언급이 없었음.
따라서 가장 효율적인 숫자를 합쳐서 계산하고 리스트를 다시 만들어 해결함.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = 0
        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next
        res = str(n1 + n2)
        head = ans = ListNode(res[0])
        for c in res[1:]:
            ans.next = ListNode(c)
            ans = ans.next
        return head