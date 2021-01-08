# Problem Link: https://leetcode.com/problems/sort-colors/

'''
문제 요약: 색 정보(0, 1, 2)가 담긴 정수배열을 정렬하는 문제 (단 추가적 메모리는 O(1)만 사용할 )
ask: [2,0,2,1,1,0]
answer: [0,0,1,1,2,2]

해석:
처음에는 단순히 추가적인 메모리 사용없이 정렬을 짜는 문제로 인식했기에, O(1) 복잡도를 구성하는 방식의 퀵소트를 구현.
결과가 상당히 느리기 때문에 다른방식으로 해결.
두개의 포인터로 0과 2를 찾아서 바꿔주면 O(2n)시간복잡도와 O(1)의 공간복잡도를 가짐. (1은 알아서 가운데로 쌓임)
'''

# Using Pointers
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        l, r = 0, len(nums) - 1
        for i in range(r + 1):
            if nums[i] == 0:
                swap(l, i)
                l += 1
        for i in range(r, l - 1, -1):
            if nums[i] == 2:
                swap(r, i)
                r -= 1

# Quick Sort
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]

        def partition(l, r):
            pivot = nums[l]
            i = l
            for j in range(l+1, r+1):
                if nums[j] <= pivot:
                    i += 1
                    swap(i, j)
            swap(l, i)
            return i

        def quickSort(l, r):
            if l < r:
                p = partition(l, r)
                quickSort(l, p-1)
                quickSort(p+1, r)
        quickSort(0, len(nums)-1)
'''