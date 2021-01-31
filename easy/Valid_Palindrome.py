# Problem Link: https://leetcode.com/problems/valid-palindrome/

'''
문제 요약: 주어진 문장이 문자,숫자만 비교했을때 좌우대칭인지 확인하는 문제. (나머지 특수문자나 공백은 무시)
ask: "A man, a plan, a canal: Panama"
answer: True

해석:
우선 문자와 숫자가 아닌 값들을 제거하기 위해서 정규표현식을 활용. 모든 필요없는 케이스를 지워주고 처음과 끝부터 쭉 검사해나가면 해결.
다른방법으로 푼 사람을 확인했는데 파이썬 built-in함수에 isalnum() 이라는 함수가 있었으며 이걸 활용해서 푸는 방법도 있었음.
isalpha(), isdigit(), isalnum(), isspace() 등의 함수가 있다는걸 배웠으니 나중에 써먹어 보면 될듯.
'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = re.compile('[a-z0-9]+', re.I)
        s_clean = "".join(r.findall(s)).lower()
        for i in range(len(s_clean)//2):
            if s_clean[i] != s_clean[-i-1]:
                return False
        return True