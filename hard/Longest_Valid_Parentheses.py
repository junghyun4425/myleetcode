# Problem Link: https://leetcode.com/problems/longest-valid-parentheses/

'''
문제 요약: 가장 긴 완벽한 괄호쌍의 길이를 반환하는 문제.
ask: ))()()()())
answer: 8

해석:
Using Stack
처음에 스택을 활용해 O(n)의 시간복잡도로 풀려고 도전. 스택에 '(' 의 캐릭터를 넣어서 풀려했지만 ()(() 나왔을때 해결이 불가능. (4가 반환이돼서 오답)
따라서 스택에 문자대신 위치값인 숫자를 저장해서 해결. 처음에 -1을 넣는 이유는 계산상 i값과 이전값을 빼주면서 거리를 구하기 때문에 0 이전값이 필요.
문제를 보고 DP로도 풀수 있다는걸 느꼈기 때문에 시간나면 DP를 활용해 풀어보도록 할 생각.

DP
스택으로 푸는게 더 빠를정도로 DP가 생각보다 복잡했던 방법. 방법 자체는 간단하나, 비교문과 out_of_index 되지 않도록 관리하는게 구현하는데 복잡성을 늘림.
몇가지 케이스로 나뉘는데, '(' 들어왔을 경우는 아직 괄호가 완성되기 전이기 때문에 신경쓰지 않아도 됨.
')' 인 경우는 이전값에 따라 결과가 달라지는데 이를 점화식으로 표현하면,
dp[i] = dp[i-2] + 2                                 if s[i-1] == '('
      = dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]       if s[i-1] == ')' and s[i-dp[i-1]-1] == '('
      = 0                                           otherwise
')'를 발견했을 때 중간에 () 와 같이 완성된 괄호들이 있을경우 그 모든 경우를 뛰어넘고 '(' 를 찾아줘야 최대길이를 정확히 잴 수 있음.
고로 s[i-dp[i-1]-1] 이 '(' 인가를 확인해야 함.
만약 만족할 경우, 길이는 dp[i-1] + 2 가 되며 혹시 이전 dp에 저장된 숫자가 있다면 더해줘야하므로 dp[i-dp[i-1]-2] 를 추가적으로 더해줌.
이를 만족하지 못하는 경우들은 모두 0이므로 넘어가도 상관없음.
'''

# Solution with DP
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s_len = len(s)
        dp = [0] * s_len
        max_len = 0
        for i in range(s_len):
            if s[i] == ')':
                if i > 0 and s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i > 1 else 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i - dp[i-1] >= 2 else 0)
                max_len = max(max_len, dp[i])
        return max_len

# Solution with Stack
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len
'''