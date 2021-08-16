# Problem Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

'''
문제 요약: 배열안 이동할때마다 하나를 제외한 숫자를 1씩 더하게 되는데, 모든 값을 같게하는 최소 움직임을 구하는 문제.
ask: [1,2,3]
answer: 3 ( [1,2,3] => [2,3,3] => [3,4,3] => [4,4,4] )

해석:
배열의 길이가 n 이라고 했을때, 한번 움직이는 경우 n-1 만큼 총합이 증가하게 됨. 얼핏보면 쉽지 않아보이지만, 수식을 만들어보면 간단해짐.
x가 이동횟수를 의미한다고 하면, x번 움직였을때 총합은 sum(nums) + x * (n-1) 이 됨.
이때, x가 최소가 되기 위해서는 배열 내 최소값이 모든 배열의 숫자와 동일해 졌을때를 만족하는 경우여야 함.
이 값은 (min(nums)+x) * n 로 계산이 가능.
sum(nums) + x * (n-1) = (min(nums)+x) * n
의 결과가 나오고, x에 대한 식으로 정리하면,
x = sum(nums) - n * min(nums)
'''

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)