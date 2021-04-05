# Problem Link: https://leetcode.com/problems/find-the-difference/

'''
문제 요약: 문자열 t는 s의 셔플링한 결과에 어떤 문자 하나를 추가한 결과를의미. 추가된 문자를 알아내는 문제.
ask: s = "abcd", t = "abcde"
answer: e

해석:
랜덤셔플이기 때문에 카운팅해야 하므로 해쉬맵을 활용해 s의 철자들을 카운팅함.
t를 탐색하면서 해쉬맵 카운팅값이 0보다 작아질때까지 뺄셈을 하고, 0보다 작아지면 그 문자가 정답이므로 반환.
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hm = defaultdict(int)
        for c in s:
            hm[c] += 1
        for c in t:
            hm[c] -= 1
            if hm[c] < 0:
                return c