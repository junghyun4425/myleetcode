# Problem Link: https://leetcode.com/problems/missing-number/

'''
문제 요약: 숫자 배열에는 0~n까지의 숫자가 정렬되지 않은채로 존재하며, 숫자 하나가 없고 이를 찾는 문제. (모두있다면 n+1이 정답)
ask: [3,0,1]
answer: 2

해석:
아이디어가 바로 떠올라서 쉽게 풀었던 문제.
배열의 길이를 n이라 했을때, 등차수열의 합은 n(n+1)/2 임을 알면 결과를 알수있음.
여기에 현재 배열의 합을 빼면 남은 숫자가 missing number.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums)+1) // 2) - sum(nums)