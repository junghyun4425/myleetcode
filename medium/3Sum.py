# Problem Link: https://leetcode.com/problems/3sum/

'''
문제 요약: 숫자 리스트에서 셋을더한 합이 0 되는 조합을 찾는 문제.
ask: [-1, 0, 1, 0]
answer: [[-1, 0, 1]] (중복은 제거)

해석:
하나의 값 i 를 고정시키고 나머지 두개의 포인트를 l, r 로 두어 모든 경우의수를 계산하는것보다 효율적으로 서치.
그러기 위해선 먼저 정렬하여 i, l, r번째 값의 합이 0보다 작으면 l을, 크면 r을 옮김.
이렇게 풀면 O(n^2)의 속도로 서칭이 가능. 단, 중복된 값을 회피해야 같은 세개의 조합을 더하지 않기 때문에 이 부분을 고려함.
i는 continue로 넘겨주고, l은 while문으로, r은 l을 옮겨주기 때문에 굳이 중복제거를 하지 않아도 됨.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n_len = len(nums)
        nums.sort()
        ans = []

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            l, r = i + 1, n_len - 1
            while l < r:
                if v + nums[l] + nums[r] < 0:
                    l += 1
                elif v + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans