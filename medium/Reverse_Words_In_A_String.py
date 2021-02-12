# Problem Link: https://leetcode.com/problems/reverse-words-in-a-string/

'''
문제 요약: 문자를 word단위의 역순으로 만들어 반환하는 문제. (쓸데없는 공백은 모두 제거)
ask: "  Bob    Loves  Alice   "
answer: "Alice Loves Bob"

해석:
양옆 공백을 제거하기 위해서 strip() 함수를 사용.
그리고 split 함수를 사용하는데 \s+ 라는 정규표현식을 이용해 모든 공백을 제거.
마지막에는 추출해낸 단어들을 역순으로 join 해서 반환하면 끝.
'''
import re

class Solution:
    def reverseWords(self, s: str) -> str:
        sp = re.split(r"\s+", s.strip())
        return " ".join(sp[::-1])