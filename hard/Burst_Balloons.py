# Problem Link: https://leetcode.com/problems/burst-balloons/

'''
문제 요약: 숫자가 달린 풍선이 있을때 하나를 터트리면 왼쪽, 오른쪽의 값을 곱해서 코인을 줌. 최대로 얻을수 있는 코인의 개수는?
ask: nums = [3,1,5,8]
answer: 167

해석:
DFS로 풀게되면 퍼뮤테이션급의 계산량으로 N! 이상의 시간복잡도를 가질거라 예상.
계산의 최적화를 위해 중복된 계산을 피하는 방식으로 해결하려면 DP를 적용시켜야 하는데 이를 정확히 집어내기 어려웠음.
첫 시도는 DP를 i,j,k 3개를 하나의 튜플로 묶어서 hashmap에 결과를 저장하려 했음.
하지만 특정 부분만 계산의 절약이 될 뿐이고 실질적으로 많은 계산에 대해 절약되지 않음.
고민끝에 이런방법을 시도,
12345 가 있다고 가정하면, 12(3)45 와 같이 마지막에 남을 숫자를 3이라고 가정. (12,45를 left, right 윈도우라 정의함)
그러면 left = 12 와 right = 45가 없으니까 1*3*1 이 되고 왼쪽 오른쪽 윈도우에서 얻어온 값을 더해주면 됨.
즉, 중복계산을 피하기위해 윈도우사이즈가 2부터 N-1 까지 계산을 해줘야 함.
각 윈도우 사이즈마다 왼쪽 좌표 i 부터 끝좌표 j 가 있으며, 여기서도 사이에 있는 값을 선택해서 최대가 되는값을 찾아야함.
점화식으로 표현하면,
dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + multiple(i-1,k,j+1))       단, i < k <= j
코드 자체는 생각보다 간단하게 끝났지만 점화식 세우는데 Divide & Conquer 개념이 완전히 적응된게 아니라 오래걸림.

재밌는게 위의 방법대로 해도 Time Limit Exceeded 가 뜨게됨. 아마 최적화 하는 방법이 있는것 같음.
일단 내가 풀었던 방법과, 통과하는 솔루션 두개를 올려놓고 다음 리뷰때 복습해서 원인분석을 하는걸로. (지금은 피로감이 너무..)
'''

# Other Solution from someone
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for d in range(2, n):
            for i in range(0, n - d):
                j = i + d
                for k in range(i + 1, j):
                    last_burn = nums[i] * nums[k] * nums[j]
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + last_burn)
        return dp[0][n - 1]

# My Answer (Time limit exceeded with DP solution)
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n_len = len(nums)
        nums = [1] + nums + [1]
        dp = [[0]*(n_len+2) for _ in range(n_len+2)]
        for window in range(1, n_len+1):
            for i in range(1, n_len-window+2):
                j = i + window - 1
                for k in range(i, j+1):
                    cal = nums[i-1]*nums[k]*nums[j+1]
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + cal)
        return dp[1][n_len]
'''