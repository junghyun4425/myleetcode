# Problem Link: https://leetcode.com/problems/isomorphic-strings/

'''
문제 요약: 두개의 문자열이 isomorphic 한지 확인하는 문제. (바뀔때 동일단어 단위로 바뀔수 있는지)
ask: s = "egg", t = "add"
answer: True (e -> a // g -> d)

해석:
해쉬맵을 사용하면 간단히 해결할 수 있는 문제. 위의 예제에서 e의 대칭은 a.
만약 e의 대칭으로 a가 아닌 다른 문자가 온다면 False를 반환하면 됨.
하나 주의해야할 점은, s를 기준으로 t를 보면 끝이 아니라 t를 기준으로 s를 살펴봐야함.
고로 두가지 경우를 체크해야 확실한 결과를 얻을 수 있음.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(s, t):
            hm = {}
            for i in range(len(s)):
                if s[i] not in hm:
                    hm[s[i]] = t[i]
                else:
                    if hm[s[i]] != t[i]:
                        return False
            return True
        return check(s, t) and check(t, s)