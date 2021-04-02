# Problem Link: https://leetcode.com/problems/linked-list-random-node/

'''
문제 요약: 링크드 리스트가 들어오면 이를 기반으로 랜덤한 값을 출력하는 클래스를 구현하는 문제. (추가 메모리 사용 없이)
ask:
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
answer:
[null, 1, 3, 2, 2, 3]

해석:
추가메모리를 사용할수 없기 떄문에 입력으로 들어오는 링크드 리스트를 그대로 활용해야 함.
따라서 head를 인스턴스 변수에 따로 저장하고, 사이즈를 구함.
Random 함수가 호출되면 size에 맞는 값을 randrange()함수로 찾아냄.
링크드 리스트의 랜덤한 인덱스만큼 탐색해서 값을 반환하면 끝.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.size = 0
        while head.next:
            self.size += 1
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        idx = randrange(0, self.size+1)
        node = self.head
        while idx > 0:
            idx -= 1
            node = node.next
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()