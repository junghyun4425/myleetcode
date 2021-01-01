# Problem Link: https://leetcode.com/problems/length-of-last-word/

'''
문제 요약: 받은 문자열의 맨 마지막 단어의 글자수를 반환하는 문제 (없으면 0을 반환)
ask: "Hello World"
answer: 5

해석:
가장 뒷자리의 문자에 붙은 없어도 되는 공백을 rstrip() 내장함수로 지워주고 공백이 나올때까지 루프.
다른 간단한 방법으로는 정규 표현식을 활용해 바로 얻어낼 수 있음.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if not s:
            return 0

        cnt = 0
        for c in s[-1::-1]:
            if c == " ":
                break
            cnt += 1
        return cnt