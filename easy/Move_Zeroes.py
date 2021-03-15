# Problem Link: https://leetcode.com/problems/move-zeroes/

'''
문제 요약: 배열의 0 들을 모두 뒤로 옮기는 문제. (0을 제외한 숫자들이 그 상태의 정렬을 유지하게끔)
ask: [0,1,0,3,12]
answer: [1,3,12,0,0]

해석:
0제외 숫자들의 정렬된 상태를 그대로 유지하는 조건을 못보고 left, right 두개의 포인터로 풀었다가 Fail.
정렬을 유지하면서 푸는 더 쉬운 방법이 포인터 하나만 가지고도 가능.
0이 아닌 포지션을 의미하는 non_zero 변수에 0이 아닌 개수를 카운팅함.
이는 곧 숫자들이 들어갈 위치를 말함. 0은 사라져도 되기 떄문에 가능한 일.
그리고 마지막에 길이 - non_zero 만큼 0을 넣어주면 끝.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_len = len(nums)
        non_zero = 0
        for i in range(n_len):
            if nums[i] != 0:
                nums[non_zero] = nums[i]
                non_zero += 1
        for i in range(non_zero, n_len):
            nums[i] = 0