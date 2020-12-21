# Problem Link: https://leetcode.com/problems/next-permutation/

'''
문제 요약: 순열 다음에 나올 순서의 조합을 완성하는 문제.
ask: [4,5,3,2,1]
answer: [5,1,2,3,4]

해석:
순열이 만들어지는 내부 알고리즘을 정확히 파악할 수 있는가에 대한 문제. 이부분을 모른다면 난이도는 hard라 볼수 있음. (구현 자체는 어려움이 없으므로)
우선 처음 찾은 규칙이 다른 예제에서는 들어맞지 않아서 실패. 나름 정답과 근접했다고 생각했으나 정답까지 도달하지 못해 순열의 원리를 인터넷에서 공부.
우측에서 부터 나아가 값이 떨어지는 부분을 찾은 다음, 그 값과 가장 근접한 큰 수를 오른쪽을 향해 찾고 그 값으로 바꿔야함.
그리고 그 나머지 뒤에 숫자들의 순서를 뒤집으면 다음의 순열이 완성.
수학적 센스가 부족해서 혼자힘으로 못풀은 느낌이기에 이런 문제들을 더 많이 접해보고 공부해야 함.
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        n_len = len(nums)
        dec, inc = -1, -1
        for i in range(n_len - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                dec = i - 1
                break
        for i in range(dec + 1, n_len):
            if nums[dec] >= nums[i]:
                inc = i - 1
                break

        if dec < 0:
            nums.sort()
        else:
            swap(dec, inc)
            for i in range((n_len - (dec + 1)) // 2):
                swap(dec + 1 + i, -1 - i)
