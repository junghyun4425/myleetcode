# Problem Link: https://leetcode.com/problems/first-unique-character-in-a-string/

'''
문제 요약: 문자열에서 가장 빠른 순서의 중복이 아닌 철자 위치를 반환하는 문제.
ask: s = "leetcode"
answer: 0

해석:
해쉬맵을 사용해 문자를 카운팅하고 하나만 존재하는 빠른순서로 찾아내면 O(n)의 시간복잡도로 결과를 얻을 수 있음.
해쉬맵을 사용하지 않으면 좀더 복잡해지겠지만 해쉬맵을 알면 간단히 풀리는 문제.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = defaultdict(int)
        for c in s:
            hm[c] += 1
        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i
        return -1