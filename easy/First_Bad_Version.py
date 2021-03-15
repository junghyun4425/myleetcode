# Problem Link: https://leetcode.com/problems/first-bad-version/

'''
문제 요약: isBadVersion(m)함수가 주어지고 이는 잘못된 버전을 알려주는 함수. 잘못된 버전의 시작지점을 찾는 문제.
ask: n = 5, bad = 4
answer: 4

해석:
isBadVersion을 linear하게 하나씩 서치해도 되지만 logn까지 줄일수 있는 Binary Search를 활용함.
중앙값을 찾아서 True면 왼쪽으로 False면 오른쪽으로 이동함.
l == r 이 되는 지점이 False에서 True가 된 지점이기 때문에 이를 반환하면 해결.
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return r
