# Problem Link: https://leetcode.com/problems/arithmetic-slices/

'''
문제 요약: Arithmetic slice로 자를수 있는 최대 개수를 세는 문제. (3개 이상의 숫자이고, 모든 연속된 숫자들의 차이가 같을때)
ask: nums = [1,2,3,4]
answer: 3 ([1,2,3], [2,3,4], [1,2,3,4] 총 3개)

해석:
Brute Force로 얼핏봐서는 굉장히 시간복잡도가 높은 상황. (모든 연속값들의 차이를 비교해줘야 해서 O(n^3))
하나의 차이를 두고, 뒤에 존재하는 모든 차이들을 찾아서 카운팅을 해야함.
하지만 이를 DP로 풀게될 경우 O(n)으로 해결이 가능함.
한번에 3개의 값을 가지고 하나씩 카운팅을 증가시키는 방식. (이때 총합을 위해 summ이라는 변수하나가 추가적으로 필요)
3개에 이어 4개, 5개까지 카운팅은 이전에 저장했던 개수(DP값)를 활용해 중복계산또한 피할 수 있음.
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n_len = len(nums)
        dp = 0
        summ = 0
        for i in range(2, n_len):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                summ += dp
            else:
                dp = 0
        return summ