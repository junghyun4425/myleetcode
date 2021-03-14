# Problem Link: https://leetcode.com/problems/product-of-array-except-self/

'''
문제 요약: 자신을 제외한 나머지값들의 곱을 모두 구하는 문제. (나누기를 사용하지 않고 구현)
ask: [1,2,3,4]
answer: [24,12,8,6]

해석:
나누기가 가능하다면 모든 배열을 곱한다음 자신을 나누기만 하면 해결되지만, 문제의 의도는 그것이 아니기 때문에 다른방법을 고민함.
자신을 기준으로 왼쪽과 오른쪽의 곱들을 저장해두면 간단하게 해결 할 수 있다는 점을 활용함.
따라서 left 배열과 right배열을 만들어 자신을 기준으로 곱들을 기록해두는 배열로 사용.
자신을 제외한 곱들이기 떄문에 left와 right 두개의 배열을 서로 곱해주면 결과가 나옴.

Optimized version
자세히 보면 공간복잡도를 훨씬 줄일 수 있는 방법을 생각해 낼수 있음.
왼쪽 곱과 오른쪽 곱을 굳이 나눠서 해야할 필요하 없기 떄문에 하나의 배열공간에서 해결.
배열에 왼쪽곱셈을 우선 저장하고, 오른쪽 곱을 처리할때는 mul이라는 오른쪽곱의 결과를 계산해서 바로 ans에 곱해주면 해결.
mul이 1인 이유는 가장 오른쪽부터 시작하기 떄문에 아무값도 없기 떄문.
'''

# Second Try (Optimize Space complexity)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        ans = [1] * n_len
        for i in range(n_len-1):
            ans[i+1] = ans[i] * nums[i]
        mul = 1
        for i in reversed(range(n_len)):
            ans[i] *= mul
            mul *= nums[i]
        return ans

# First Try
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        left = [1] * n_len
        right = left[:]
        ans = []
        for i in range(n_len-1):
            left[i+1] = left[i] * nums[i]
        for i in reversed(range(n_len-1)):
            right[i] = right[i+1] * nums[i+1]
        for i in range(n_len):
            ans.append(left[i] * right[i])
        return ans
'''