# Problem Link: https://leetcode.com/problems/wiggle-subsequence/

'''
문제 요약: 최대 길이의 wiggle subsequence 를 구하는 문제. (위글이란 1 10 5 10 와 같이 커졌다 작아졌다를 반복하는 숫자열)
ask: [1,17,5,10,13,15,10,5,16,8]
answer: 7

해석:
First Try (Brute Force)
문제를 정확히 이해하고 최적화하기 위해 먼저 생각나는대로 Brute Force방식으로 구현해봄.
증가와 감소를 반복해야 최대길이가 하나씩 증가하는 구조이기 때문에 인자로 positive와 같이 이전에 있었던 결과를 받아와 줌.
이전에 positive였다면 다음은 더 작은값이 올때만 길이를 증가시켜주는 방식.
시작부터 끝까지 존재하는 모든 경우를 재귀함수 호출하기 때문에 속도가 굉장히 느림.

Second Try (DP)
Brute Force방식에서 바로 계산의 최적화는 어렵다고 판단.
최적화를 위해서는 가지치기를 하거나 중복계산을 피해야 하는데 이를 위해선 기존의 구조를 바꿔야만 하기 떄문.
따라서 기존에 계산했던 모든 경우의수를 호출하는 대신 두개의 DP를 두고 중복계산을 피하도록 설계.
up, down 두개의 배열을 두고 서로 참조하면서 최대 길이를 구하게 함.
up은 배열에서 값이 증가하는 경우 체크하며, down에서 구했던 계산에서 1씩 증가해 최대값을 찾음.
이를 점화식으로 나타내보면,
up[i] = max(up[i], down[j] + 1)             if 0 <= j < i and nums[i] > nums[j]
down[i] = max(down[i], up[j] + 1)           if 0 <= j < i and nums[i] < nums[j]
현재 길이 i에 대해서 이전에 계산해놓은 최대길이를 참조하는 방식으로 결과를 구해냄.
'''

# Second Try (DP)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n_len = len(nums)
        up = [0] * n_len
        down = [0] * n_len
        for i in range(n_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j]+1)
        return 1 + max(up[-1], down[-1])

# First Try (Time Limit Exceeded)
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n_len = len(nums)
        def recursion(idx, positive):
            max_cnt = 0
            for i in range(idx+1, n_len):
                if (positive and nums[i] > nums[idx]) or (not positive and nums[i] < nums[idx]):
                    max_cnt = max(max_cnt, 1 + recursion(i, not positive))
            return max_cnt
        return 1 + max(recursion(0, True), recursion(0, False))
'''