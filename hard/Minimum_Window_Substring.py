# Problem Link: https://leetcode.com/problems/minimum-window-substring/

'''
문제 요약: 문자열 2개 s와 t를 받아, t문자열이 s에 포함되는 가장 작은 길이의 문자를 반환하는 문제. (O(n)의 속도로 풀기)
ask: s = "ADOBECODEBANC", t = "ABC"
answer: "BANC"

해석:
해시맵으로 t에 존재하는 캐릭터를 카운트. O(n)을 만족하기 위해서 l, r 포인터 두개로 s 내 위치를 움직이면서 수행.
가장 짧은 위치를 알아야 하기 때문에 길이, index 두개를 ans로 사용하고 짧은 길이를 마주칠때마다 바꿈.
while문은 먼저 오른쪽 r을 s길이까지 옮기고 도중에 hmap을 만족(카운트가 모두 0되는 시점)하면 l을 옮겨줌.
l을 움직이면서 최소길이인 ans값을 갱신해주고, 만약 hmap에 있는걸 다시만나게 된다면 hmap 카운트를 늘려주면서 루프를 빠져나오는 방식.
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, cnt = 0, 0, 0
        ans = [float('inf'), 0, -1]
        m = {}
        for c in t:
            m[c] = m.get(c, 0) + 1
        s_len, m_len = len(s), len(m)

        while r < s_len:
            c = s[r]
            if c in m:
                m[c] -= 1
                if m[c] == 0:
                    cnt += 1
            while l <= r and cnt == m_len:
                c = s[l]
                if r - l + 1 < ans[0]:
                    ans = [r - l + 1, l, r]
                if c in m:
                    m[c] += 1
                    if m[c] > 0:
                        cnt -= 1
                l += 1
            r += 1
        return s[ans[1]:ans[2] + 1]