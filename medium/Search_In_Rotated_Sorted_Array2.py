# Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

'''
문제 요약: pivot을 기점으로 반복되는 정렬된 숫자 리스트에서 target의 유를 반환하는 문제.무 (중복이 존재)
ask: [2,5,6,0,0,1,2], target = 0
answer: True

해석:
처음에는 이 문제를 보고 왜 난이도가 미디엄인지 몰랐던 문제.
순차적으로 서칭하면 O(n) 의 나쁘지않은 시간복잡도와 O(1) 의 공간복잡도를 가짐.
따라서 순차진행으로 풀었고, 이 문제를 리스트에 저장해 뒀다가 나중에 O(logn)의 시간복잡도를 가지게끔 풀어보기.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in nums:
            if target == i:
                return True
        return False