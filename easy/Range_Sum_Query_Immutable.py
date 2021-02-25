# Problem Link: https://leetcode.com/problems/range-sum-query-immutable/

'''
문제 요약: 배열의 범위에 존재하는 값들을 모두 더해서 반환해주는 클래스를 구현하는 문제.
ask:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
answer:
[null, 1, -1, -3]

해석:
덧셈을 범위내에서 해야하기 때문에 Brute Force 방식으로 구현하면 반복연산이 계속해서 중복되는 문제가 생김.
따라서 중복계산을 줄여주기 위해 DP방식으로 해결.
이전에 값들을 모두 더해서 sums 라는 배열에 저장한 뒤, range에 따라 합들의 위치를 빼주면 범위별 합을 쉽게 구할 수 있음.
sums[i] = sums[0] + sums[1] + ... sums[i]
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = nums[:]
        for i in range(1, len(nums)):
            self.sums[i] += self.sums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)