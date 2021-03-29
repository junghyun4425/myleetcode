# Problem Link: https://leetcode.com/problems/intersection-of-two-arrays/

'''
문제 요약: 두개의 배열에 intersection을 구하는 문제.
ask: nums1 = [1,2,2,1], nums2 = [2,2]
answer: [2]

해석:
파이썬 collections에 포함된 set 기본 자료구조를 알면 해결이 가능한 문제.
두 리스트를 중복이 불가능한 set 자료구조에 각각 넣고, 집합연산 intersection을 수행하면 해결.
intersection을 안쓰고 수행하려면 nums1 기준으로 하나씩 nums2에 존재하는지 확인하면 됨.
set도 해쉬기능이 포함되어있기에 성능상 문제되진 않음.
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))