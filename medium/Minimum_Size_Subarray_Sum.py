# Problem Link: https://leetcode.com/problems/minimum-size-subarray-sum/

'''
문제 요약: target보다 크거나 같은 값을 합으로 가지는 sub-array 최소 길이를 구하는 문제.
ask: target = 7, nums = [2,3,1,2,4,3]
answer: 2

해석:
subarray를 구하는 문제라면 일단 두개의 포인터를 활용하는걸 먼저 떠올리게 됨.
subarray이기 때문에 정렬하지 않고 해결해야 하며, 음수가 없기때문에 포인터 두개로 쉽게 해결이 가능.
l에서부터 r까지의 합을 total에 구하고, 값이 커지면 그 길이를 ans에 저장.
값이 커졌기 때문에 target보다 작아질때까지 l을 하나씩 줄여가며 total을 줄임.
r을 끝까지 가면 가장 작은 사이즈의 subarray 길이를 구할 수 있음.
값이 단한번도 target을 못넘었을 경우엔 0을 반환.
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n_len = len(nums)
        ans = float('inf')
        l = total = 0
        for r in range(n_len):
            total += nums[r]
            while target <= total:
                ans = min(ans, r+1-l)
                total -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0