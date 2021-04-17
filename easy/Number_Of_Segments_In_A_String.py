# Problem Link: https://leetcode.com/problems/number-of-segments-in-a-string/

'''
문제 요약: 스페이스로 나뉜 단어들이 몇개인지 세는 문제. (단어간 분리는 스페이스로만 이뤄짐)
ask: s = "Hello, my name is John"
answer: 5

해석:
내장함수를 사용하면 한줄에 끝나기 떄문에, 직접 해보기로 함.
일단 주어진 문제가 굉장히 간단함.
어떤 단어가 나올때 이전값이 공백이라면 단어 하나를 추가해주는 방법으로 하면 굉장히 깔끔하게 해결이 가능.
여러가지 방법이 존재하고 몇가지 방법으로 해결해 봤지만, 이 방법이 코드 자체는 알아보기가 쉽기 때문에 이렇게 마무리를 함.
'''

class Solution:
    def countSegments(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == " ") and s[i] != " ":
                cnt += 1
        return cnt