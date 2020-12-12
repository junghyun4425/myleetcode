# Problem Link: https://leetcode.com/problems/container-with-most-water/

'''
문제 요약: 물을 받는 컨테이너의 height 가 배열로 주어진다. 이중에서 최대로 받을수 있는 물의 양을 구하는 문제.
ask: [1,8,6,2,5,4,8,7,3]
answer: 49   // 최소높이 7, 거리 7일때 가장 많은 물을 저장가능.

해석:
간단하게 이중포문으로 너비를 재면서 맥스값을 구함.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        h_len = len(height)
        max_a = 0
        for i in range(h_len):
            for j in range(h_len-1, i, -1):
                h = height[i] if height[i] < height[j] else height[j]
                a = h * (j-i)
                if max_a < a:
                    max_a = a
        return max_a