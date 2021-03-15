# Problem Link: https://leetcode.com/problems/valid-anagram/

'''
문제 요약: 문자 s의 스펠링으로 t를 만들수 있으면 True를 반환하는 문제.
ask: s = "anagram", t = "nagaram"
answer: True

해석:
바로 생각나는건 정렬 또는 해쉬맵을 이용해 푸는 방식.
메모리를 조금 쓰고 성능을 높이기 위해 해쉬맵을 선택.
s의 단어는 해쉬맵에서 덧셈을 하고, t는 뺄셈을 해서 0이면 단어의 수가 같다는것을 의미.
따라서 해쉬맵에 0이 아닌값이 있으면 False를 반환하고 모두 0이라면 True를 반환.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hm = defaultdict(int)
        for i in range(len(s)):
            hm[s[i]] += 1
            hm[t[i]] -= 1
        for v in hm.values():
            if v != 0:
                return False
        return True