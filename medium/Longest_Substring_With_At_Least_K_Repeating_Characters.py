# Problem Link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

'''
문제 요약: 문자열에서 k개가 반복적으로 나타나는 substring의 최대 길이를 구하는 문제.
ask: s = "ababacba", k = 3
answer: 0

해석:
처음엔 substring이 안에 포함되기만 하면 되는줄 알고 쉽게 생각했다가, 순서를 지켜야하는걸 알고 오래 고민했던 문제.
Brute Force로는 starting point를 0부터 시작해서 연속된 개수를 세는 방법이 있겠지만 효율이 굉장히 떨어짐.
따라서 invalid 지점을 기준으로 divide and conquer 방식을 적용하기로 함.
먼저 해쉬맵에서 카운팅을 하고, 앞에서부터 진행해가며 invalid 지점을 찾음. 위의 예에선 c가 invalid.
c를 기준으로 나눈다음 다시 카운팅하고 k를 넘는 연속된 substring이 있는지 검사를 함.
만약 없다면 0이 나올것이고, 있다면 그 길이를 반환해 왼쪽과 오른쪽중 긴 substring을 반환함.
최대길이가 되는 경우는 모든 알파벳이 k개를 넘겼을때 그 길이를 반환하면 됨. ( r - l )
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def div_and_con(l, r):
            if r < k: return 0
            hm = defaultdict(int)
            for i in range(l, r):
                hm[ord(s[i]) - ord('a')] += 1
            for m in range(l, r):
                if hm[ord(s[m]) - ord('a')] >= k:
                    continue
                invalid = m+1
                while invalid < r and hm[ord(s[invalid]) - ord('a')] < k:
                    invalid += 1
                return max(div_and_con(l, m), div_and_con(invalid, r))
            return r - l
        return div_and_con(0, len(s))