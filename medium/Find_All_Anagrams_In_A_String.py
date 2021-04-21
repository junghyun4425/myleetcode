# Problem Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

'''
문제 요약: 문자 s에서 p로 이루어진 anagram의 시작점을 모두 나열하는 문제.
ask: s = "cbaebabacd", p = "abc"
answer: [0,6] (0번째 cba 와 6번째 bac 가 anagram을 만족함)

해석:
문제를 보자마자 바로 슬라이딩 윈도우로 해결하면 O(n)의 시간복잡도로 해결이 가능하다고 떠오름.
따라서 l, r 두가지 포인터를 사용해 윈도우를 옮겨가며 anagram이 맞는지 체크를 함.
이때, anagram이 맞는지 체크하기 위해서 탐색시간이 추가로 발생하는것에 대해 큰 고민을 함.
코드에 조건절을 여럿 추가해서라도 추가시간을 제거하기로 결정.
cnt 라는 변수는 p에 대한 모든 철자를 의미하고, 0이되어야 비로소 anagram을 만족함.
l부터 r까지 cnt가 0인 경우에는 l을 추가하고, 아니면 l과 r을 한칸씩 뒤로 옮기는 작업을 수행.
한칸씩 옮길때마다 cnt가 0인지 체크하고, 0일때 해쉬맵의 변화와 0이 아닐때 변화를 관리해줘야 해서 조건절이 굉장히 많아짐.
(코드의 시간복잡도 성능은 최상위)
나중에 복습할때는 이를 좀더 깔끔하게 해결하는 방법을 찾아보는걸로.
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        win_size = len(p)
        hm = defaultdict(int)
        for c in p:
            hm[c] += 1
        cnt = len(hm)
        l = 0
        for r, c in enumerate(s):
            if c in hm:
                hm[c] -= 1
                if hm[c] == 0:
                    cnt -= 1
            if r - l == win_size - 1:
                if cnt == 0:
                    ans.append(l)
                if s[l] in hm:
                    if hm[s[l]] == 0:
                        cnt += 1
                    hm[s[l]] += 1
                l += 1
        return ans