# Problem Link: https://leetcode.com/problems/third-maximum-number/

'''
문제 요약: 세번째로 큰 값을 찾는 문제. (같은 값은 무시, O(n) 시간복잡도 구현의 Follow up이 존재함)
ask: [3,2,1]
answer: 1

해석:
O(n)으로 해결해야하기 떄문에 추가적인 메모리를 사용.
우선 최대값을 구해주고, 나머지 2개의 포인터로 최대값을 갱신해나가는 방법으로 해결.
max함수로 O(n) + 배열의 최대값 검사로 O(n) 이기 때문에 최종적으로 시간복잡도는 O(n)이 됨.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max(nums)
        max2 = max3 = float("-inf")
        for n in nums:
            if n == max1 or n == max2 or n == max3:
                continue
            if max2 < n:
                max3, max2 = max2, n
            elif max3 < n:
                max3 = n
        return max3 if max3 != float('-inf') else max1