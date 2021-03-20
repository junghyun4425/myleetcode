# Problem Link: https://leetcode.com/problems/reverse-vowels-of-a-string/

'''
문제 요약: 문자열에서 모음만 반대로 바꾸는 문제. (y는 모음으로 치지 않음)
ask: "leetcode"
answer: "leotcede"

해석:
Reverse String 문제에서 조금더 확장된 문제.
마찬가지로 l,r 두개의 포인터를 사용해서 추가메모리 없이 구현.
여기선 모음을 set()에 저장해서 검색 속도를 늘려 최적화를 시도함.
그외에 주의사항이 있다면 w가 모음이 아니었다는 것....
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)