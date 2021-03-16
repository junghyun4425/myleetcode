# Problem Link: https://leetcode.com/problems/word-pattern/

'''
문제 요약: pattern과 문자열 s의 패턴이 일치하는지 확인하는 문제. (s는 띄워쓰기로 구분, pattern은 공백없음)
ask: pattern = "abba", s = "dog cat cat dog"
answer: true

해석:
s를 배열로 split한 다음 두개간의 패턴을 비교하면 됨.
우선 길이가 다르면 패턴이 일치할수 없으니 False를 반환.
한가지 주의할점은, pattern과 s를 양쪽의 기준에서 비교해줘야 한다는 점. pattern을 기준으로만 검사하면,
pattern = "abba", s = "dog dog dog dog"
의 경우에서 True가 되어버림. 따라서 s를 기준으로 한번더 수행.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s): return False
        def comp(pattern, s):
            rules = {}
            for i, p in enumerate(pattern):
                if p not in rules:
                    rules[p] = s[i]
                else:
                    if rules[p] != s[i]:
                        return False
            return True
        return comp(pattern, s) and comp(s, pattern)