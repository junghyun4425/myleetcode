# Problem Link: https://leetcode.com/problems/linked-list-cycle/

'''
문제 요약: 리스트가 사이클이면 마지막 노드에서 사이클인 지점의 노드를 반환하는 문제. (단, 메모리 공간 복잡도는 O(1)로 제한)
ask: head = [3,2,0,-4], pos = 1 (pos는 사이클 지점, 값으로 주어지지 않음)
answer: 1 (Node index 1)

해석:
지난번 Linked_List_Cycle 문제에서 사이클 도는 지점을 찾는 문제. 여기서도 추가 메모리 사용이 어렵기에 이전에 사용한 방법을 응용해봄.
여러번의 예시를 그려 확인해본 결과 몇가지 원칙을 수립할 수 있었음.
1. 사이클이 처음으로 돌아가는 경우라면, 무조건 사이클 지점이 시작되는 곳에서 만남.
2. 사이클이 시작지점에서 한칸뒤라면, 사이클 지점 바로 뒤쪽(맨 마지막 노드) 에서 만남.
3. 사이클이 시작지점에서 두칸뒤라면, 사이클 지점 뒤쪽의 뒤쪽 에서 만남.
즉, 1칸씩, 2칸씩 이동하는 경우 만나는 지점을 시작지점과 사이클이 시작되는곳의 거리만큼 떨어져있음. 따라서 head부터 만날때까지 한칸씩 이동해주면 해결됨.

너무 궁금해서 이 문제의 원리를 찾아봄. 찾아보니 플로이드 사이클 디텍션 이라는 공식을 찾게됨.
그 설명이 잘되어있어 링크를 남김.
https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        while p1 and p1.next:
            p2 = p2.next
            p1 = p1.next.next
            if p1 == p2:
                p2 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None