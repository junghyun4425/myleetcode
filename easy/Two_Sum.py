# Problem Link: https://leetcode.com/problems/two-sum/

'''
문제 요약: 두개의 숫자를 더해서 target이 되는 두 인덱스를 결과로 반환하기.
ask: [2,3,4,5] target: 5
answer: [0, 1]

해석:
무작정 for문 두개로 모든 경우의 수를 파악해서 구하는 방법이 있음.
for i in range(list) + for j in range(i, list) = 너무 느림.
다음으로 해시맵에 target 뺀값을 저장하는거임. 뺀값을 key로, index를 value로.
그러면 for문 하나에서 뺀값과 같은지 비교만 해보면 됨. 해시맵이라 이중포문보다 탐색이 빠름.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_len = len(nums)
        hmap = {nums[i]:i for i in range(list_len)}
        for i in range(list_len):
            v = target - nums[i]
            if v in hmap and i != hmap[v]:
                return [i, hmap[v]]