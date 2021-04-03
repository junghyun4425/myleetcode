# Problem Link: https://leetcode.com/problems/ransom-note/

'''
문제 요약: magazine에 존재하는 string으로 ransomNote를 만들수 있는지 확인하는 문제.
ask: ransomNote = "aa", magazine = "ab"
answer: False

해석:
해쉬맵을 활용해 해결한 문제.
magazine에 존재하는 모든 철자들을 해쉬맵에 카운팅하고, ransomNote를 만족할만한 개수가 들어있는지 확인.
개수가 0 이하로 떨어진다면 다음에 마주할때 False를 리턴하고 만족한다면 loop를 빠져나와서 True를 반환.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = defaultdict(int)
        for c in magazine:
            hm[c] += 1
        for c in ransomNote:
            if c not in hm or hm[c] == 0:
                return False
            hm[c] -= 1
        return True