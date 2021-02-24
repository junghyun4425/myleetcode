# Problem Link: https://leetcode.com/problems/container-with-most-water/

'''
문제 요약: 물을 받는 컨테이너의 height 가 배열로 주어진다. 이중에서 최대로 받을수 있는 물의 양을 구하는 문제.
ask: [1,8,6,2,5,4,8,7,3]
answer: 49   // 최소높이 7, 거리 7일때 가장 많은 물을 저장가능.

해석:
간단하게 이중포문으로 너비를 재면서 맥스값을 구함.
O(n^2) 이면 통과가 불가능한 문제였기에 발전된 방향으로 다시생각해서 문제를 품. 도저히 줄이는 방법이 생각 안나서 힌트를 봄.
음... 알고리즘을 푼다는 문제라기 보다는 '하나의 간단한 원칙' 을 꿰뚫을 수 있냐없냐의 문제였음.

간단한 원칙은, 좌우(l,r) 막대중 짧은 막대에 위치한 index를 한칸 좁히는 것. 그 이유는 긴막대의 포인트 옮겨봤자 너비는 더 커질수 없기 때문임.
(왜냐면 area를 구할때 '짧은 막대길이 x 막대간 너비' 이기 때문임)
어렵게 생각해 이런 간단한 원칙을 몰랐다는건 조금 아쉬웠던 문제.

Review
오랜 고민끝에 풀어낸 문제라 한달이 지난 지금 봐도 알고리즘이 바로 떠올랐던 문제.
처음부터 다시 풀어봤지만 두개의 포인터로 최대넓이만 찾아가는 알고리즘을 알고있었기에 빠르게 풀수 있었음.
'''

# Third Try: Same algorithm to second trial. For reviewing
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_a = 0
        while l < r:
            max_a = max(max_a, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_a

# Second Try: Two points algorithm
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        h_len = len(height)
        max_a = 0
        l, r = 0, h_len - 1
        while l != r:
            a = (r - l) * (height[l] if height[l] < height[r] else height[r])
            max_a = a if a > max_a else max_a
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_a
'''

# First Try: Brute Force
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
'''