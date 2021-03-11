# Problem Link: https://leetcode.com/problems/contains-duplicate-ii/

'''
문제 요약: 같은값이 중복으로 나오면 그 위치의 길이가 k보다 같거나 작은지 확인하는 문제.
ask: nums = [1,2,3,1], k = 3
answer: true ( 3-0 <= 3 )

해석:
중복된 값의 위치를 밸류로하는 hashmap이 있으면 쉽게 해결이 가능.
그 위치와 현재 중복된 index의 위치 둘을 빼주고 k보다 작거나 같은지 확인하면 해결이 됨.
여기서 abs()를 쓰지 않아도 되는이유는 i값이 항상 hashmap에 저장된 값보다 크기 때문.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i, n in enumerate(nums):
            if n in hm:
                if i-hm[n] <= k:
                    return True
            hm[n] = i
        return False