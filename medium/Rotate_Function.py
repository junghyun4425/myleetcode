# Problem Link: https://leetcode.com/problems/rotate-function/

'''
문제 요약: 배열의 숫자들을 rotation 하면서 index와 배열의 값 곱셈의 합이 최대가 되는 값을 찾는 문제.
ask: nums = [4,3,2,6]
answer: 26
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

해석:
First Try
처음에는 문제를 정확히 파악하기 위해 간단히 시도해보는 Brute Force 방식으로 해결.
모든 숫자들을 로테이션 돌리면서 구해보면 결과는 쉽게 나오겠지만 O(n^2)의 시간복잡도를 가지기 때문에 여기선 Time Limit Exceeded.

Second Try
보통 시간 부족인 경우 중복계산을 제거하거나 어떤 패턴을 찾는 방법이 있음.
여기서는 중복계산을 피할수 있는 방법이 마땅히 보이지 않고 숨겨져 있기에 패턴을 파악하면 중복계산을 피할 수 있음.
따라서 F(x) 라는 함수를 가정해서 함수가 어떤식으로 계산되는지 일반식으로 표현해 보고자 함.
F(0) = (0 * a0) + (1 * a1) + (2 * a2)
F(1) = (1 * a0) + (2 * a1) + (0 * a2)
...
F(1) - F(0) = a0 + a1 - (2 * a2)
F(1) = sum(a0+a1+a2) + F(0) - (3 * a2)
따라서,
F(i) = sum(nums) + F(i-1) - (n * nums[-i])
라는 일반식으로 표현이 가능하며, 이를 대입하면 O(n) 의 시간복잡도로 문제를 해결이 가능.
'''

# Second Try (Pattern with DP)
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n_len = len(nums)
        summ = sum(nums)
        prev = sum([i * n for i, n in enumerate(nums)])
        ans = prev
        for i in range(1, n_len):
            prev = prev + summ - n_len * nums[-i]
            ans = max(ans, prev)
        return ans

# First Try (Brute Force)
'''
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n_len = len(nums)
        muls = range(n_len)
        ans = float("-inf")
        for i in range(len(nums)):
            ans = max(ans, sum([nums[(i+j) % n_len] * j for j in range(n_len)]))
        return ans
'''