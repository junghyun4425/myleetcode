# Problem Link: https://leetcode.com/problems/partition-equal-subset-sum/

'''
문제 요약: 배열을 두개로 나누었을 때(연속적일 필요없음) 서로의 합이 같아질 수 있는지 확인하는 문제.
ask: nums = [1,5,11,5]
answer: True (11 과 1,5,5 두개로 나누면 값이 같아짐)

해석:
아마 Brute Force 방식으로 풀면 시간제한에 걸릴거라 예상하고, 재귀함수로 해결하면 되는것을 알기에 이 방식으론 해결해 보진 않음.
바로 최적화를 들어가기 전에 몇가지 알아둬야 할 점은
1.인덱스 상관없이 일단 두개로 나눈값이 같다면 True를 반환.
2.배열의 합이 짝수인 경우만 가능하므로 홀수일땐 바로 False를 반환.
이를 활용해 재귀함수로 해결하고, 인덱스를 하나씩 증가시키면서 배열의 합에 반을 나눈값의 차가 0이되면 True를 반환함.
이때, 중복계산을 피하기 위해 DP방식으로 이전의 결과값을 저장해 둠.
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        dp = {}
        def recursion(i, summ):
            if (i, summ) in dp:
                return dp[(i, summ)]
            if summ < 0 or i >= len(nums):
                return False
            if summ - nums[i] == 0:
                return True
            res = recursion(i + 1, summ - nums[i]) or recursion(i + 1, summ)
            dp[(i, summ)] = res
            return res
        return recursion(0, total // 2)