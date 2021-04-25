# Problem Link: https://leetcode.com/problems/assign-cookies/

'''
문제 요약: 아이들이 필요로하는 과자의 양을 나타낸 g와 과자의 양 s가 있을때, 몇명에게 최대로 줄수 있는지 알아내는 문제.
ask: g = [1,2,3], s = [1,1]
answer: 1

해석:
가장 간단하게 해결할 수 있는 방법은 정렬을 활용하는 것.
정렬해서 최대로 과자를 줄수있는 아이들의 수를 구할 수 있음.
요구량이 작은 아이부터 주되, 과자가 작은양이면 다른 아이들에게도 줄수 없기 때문에 다음 과자로 넘어가면서 확인하는 방식.
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_len = len(g)
        i = 0
        for a in s:
            if g[i] <= a:
                i += 1
            if i == g_len:
                return i
        return i