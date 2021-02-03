# Problem Link: https://leetcode.com/problems/palindrome-partitioning-ii/

'''
문제 요약: 문자를 최소한의 나누기로 palindrome를 만들 때 나눈 최소값을 반환하는 문제.
ask: "aab"
answer: 1 (aa / b 한번의 나눔으로 모든쌍을 palindrome으로 구성)

해석:
역시 이전의 Palindrome_Partitioning 방식으로 수행하면 시간 초과.
불필요한 연산을 최소화하기 위해 값들을 palindrome인지 확인하는 2차원 배열 생성. pals[i][j] 에서 i는 s의 시작점, j는 끝점.
pals[i][j] = True       if (i == j) or (s[i] == s[j] and pals[i+1][j-1])
           = False      if s[i] != s[j]
여기서, pals[i+1][j-1] 이 의미하는 바는 사이에 존재하는 값이 palindrome인지 아닌지를 판단.
palindrome의 존재 유무를 모두 저장해놨으니, 다음은 minimum cut 개수를 구할 차례.

우선 bottom-up 방식으로 s[:1] 부터 s 까지 하나씩 늘려가며 최소값을 계산함.
만약 s[:i] 가 palindrome이라면 dp[i] = 0이 들어갈테고, 아니라면 이전값에 하나를 더한게 최소로 자른 값.
이때, 이전값은 s[0],s[l] 양측을 제외한 가운데에서 cut 비용을 최소로 하는 값이 나올 수 있기 떄문에 for문으로 최소값을 탐색.
dp의 점화식은,
dp[i] = 0                       if pals[0][i] == True
      = dp[i-1]+1               if pals[0][i] == False
      = min(dp[x-1]+1, dp[i])   if pals[x][i] == True, 1 < x < i

한가지 재밌는 방법을 발견.
캐시를 사용해서 더 직관적인 방법으로 이해가 가능.
다만 단점은, 캐시가 단순히 해쉬맵 역할만 하는 저장공간으로 사용하기 때문에 완전히 최적화되진 않아서 DP방식보다 퍼포먼스면에선 뒤쳐짐.
이 문제에 대해 재귀함수로 캐시를 구현하면 어떤식으로 할까 궁금했었는데 재밌는 방법을 보게됨.
'''
# DP
class Solution:
    def minCut(self, s: str) -> int:
        s_len = len(s)
        pals = [[False] * s_len for _ in range(s_len)]
        for i in range(s_len):
            pals[i][i] = True
        for subs_len in range(2, s_len + 1):
            for i in range(0, s_len - subs_len + 1):
                j = i + subs_len - 1
                if subs_len == 2:
                    pals[i][i + 1] = s[i] == s[j]
                else:
                    pals[i][j] = s[i] == s[j] and pals[i + 1][j - 1]

        dp = [float('inf')] * s_len
        for l in range(s_len):
            if pals[0][l]:
                dp[l] = 0
            else:
                dp[l] = dp[l - 1] + 1
            for i in range(1, l):
                if pals[i][l]:
                    dp[l] = min(dp[i - 1] + 1, dp[l])
        return dp[-1]

# Cache
'''
class Solution:
    def minCut(self, s: str) -> int:
        s_len = len(s)
        cache = defaultdict(lambda: float('inf'), {c:0 for c in s})
        pals = defaultdict(bool, {c:True for c in s})

        def check_pal(s):
            if s in pals: return pals[s]
            pals[s] = s == s[::-1]
            return pals[s]

        def dfs(i):
            if check_pal(s[i:]):
                return 0
            if s[i:] in cache:
                return cache[s[i:]]
            for j in range(i+1, s_len+1):
                if not check_pal(s[i:j]):
                    continue
                cnt = 1 + dfs(j)
                cache[s[i:]] = min(cache[s[i:]], cnt)
            return cache[s[i:]]

        return dfs(0)
'''