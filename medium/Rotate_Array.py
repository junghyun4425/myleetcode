# Problem Link: https://leetcode.com/problems/rotate-array/

'''
문제 요약: 배열을 k번 rotate 한 결과로 만드는 문제. (Space complexity O(1)로 구현)
ask: nums = [1,2,3,4,5,6,7], k = 3
answer: [5,6,7,1,2,3,4]

해석:
먼저 Brute Force 방식으로 해결해봄. 2중 루프를 동아야 하기 때문에 O(nk) 시간복잡도가 나옴.
굉장히 비효율적이기 때문에 메모리를 사용하지 않고 해결하는 방법을 연구.
한가지 재밌는 패턴을 발견했는데, k를 경계로 둘 사이에 정렬된게 나누어져 있다는 점.
즉, 0 ~ k, k ~ len 까지 정렬이 되어있다는 점에서 배열부분을 두갈래로 나눠서 바꿔붙이면 된다는 것.
하지만 추가 배열메모리를 사용해야 하기때문에 이를 해결할 수 있는 다른방법으로 reverse를 활용함.
전체를 반대로 뒤집고, k를 기점으로 양쪽에서 각각 뒤집으면 결과가 나오게 됨.
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_len = len(nums)
        k %= n_len
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        reverse(0, n_len-1)
        reverse(0, k-1)
        reverse(k, n_len-1)