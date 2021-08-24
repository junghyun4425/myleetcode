# Problem Link: https://leetcode.com/problems/regular-expression-matching/

'''
문제 요약: RegExp 구현하는 문제. '.'은 모든 하나의 문자, '*'은 앞의 문자가 0~무한 개의 문자를 의미함.
ask: s = "aab", p = "c*a*b"
answer: True

해석:
처음에는 최적화를 생각하지 않고 Brute Force 방식으로 해결해봄.
1. Brute Force
'.' 은 한글자만 포함하면 되기 때문에 굉장히 쉽게 해결이 가능하지만 '*'은 경우의 수가 너무 다양함. 모든 경우의 수를 정의해 보자면,
    -'*' 에 맞는 문자가 0개
    -'*' 에 맞는 문자가 1개
    -'*' 에 맞는 문자가 2개 이상
이 모든 것을 고려하기 위해 우선, 첫번째 글자가 맞는지 확인부터 함. s와 p의 첫번째 글자가 맞는지, 틀린지에 따라 결과를 판단하기가 쉽기 떄문.
그리고 p의 두번째 문자가 '*' 인경우 '*'에 맞는 문자가 0개일때와 하나 이상일때를 판별함. 하나 이상일때는 재귀함수로 s를 하나씩 줄여가는 방법을 사용.
만약 '*' 가 아니라면 간단하게 다음으로 넘어가는 방식.
물론 결과는 stack overflow겠지만 문제해결을 했다는것에 의의를 둔 방법이므로 성공적.

2. DP
Brute Force 방식으로 해결해봤다면 굉장히 쉽게 해결이 가능함.
그 이유는 알고리즘 그대로 사용하되, 메모이제이션 방식으로 중복계산만 없애주면 효율이 극대화 되기 떄문.
이번엔 인덱스를 사용해 s[:i], p[:j] 일때 중복을 제거. 따라서 (i, j) 를 기준으로 ans가 True인지 False인지를 저장해놓음.
그렇게 참조하고, 저장되어있는 값이 없다면 계산하고를 반복해 해결.
'''

# DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        dp = {}

        def helper(i, j):
            if (i, j) not in dp:
                if j == p_len:
                    ans = i == s_len
                else:
                    first = i < s_len and p[j] in (s[i], '.')
                    if j + 1 < p_len and p[j + 1] == '*':
                        ans = helper(i, j + 2) or (first and helper(i + 1, j))
                    else:
                        ans = first and helper(i + 1, j + 1)
                dp[(i, j)] = ans
            return dp[(i, j)]

        return helper(0, 0)

# Brute Force (Recursion)
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(s, p):
            if not p:
                return not s
            first = p[0] in (s[0], '.')
            if len(p) >= 2 and p[1] == '*':
                return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
            else:
                return first and self.isMatch(s[1:], p[1:])
        return helper(s, p)
'''