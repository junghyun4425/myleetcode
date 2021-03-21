# Problem Link: https://leetcode.com/problems/wiggle-sort-ii/

'''
문제 요약: 숫자 배열을 wiggle방식으로 정렬하는 문제. (위글은 [1,2,1,2,1,2] 처럼 큰값, 작은값 혹은 작은값, 큰값 순으로 정렬됨을 말함)
ask: [1,5,1,1,6,4]
answer: [1,6,1,5,1,4] ([1,4,1,5,1,6]도 가능)

해석:
First Try
공간복잡도를 O(1)로 할수 있지 않을까하고 시도해본 방법.
토글을 설정해 처음엔 앞쪽에 값이 작아야하고, pointer 1증가한 다음엔 앞쪽의 값이 커야하는 방식으로 구현을 해봄.
대부분의 케이스에서 다 수행되나, 같은수가 연속적으로 존재하면 해결이 불가능.

Second Try
물론 저 방법을 응용하면 해결가능할것 같았지만 그냥 리셋하고 새로 구현해봄.
이번엔 O(n)의 스페이스를 사용하기로 결정. (배열에 들어오는 숫자가 5000 이하걸 활용함)
배열안에 존재하는 숫자들을 cnt배열에 카운팅. (5000이하라 가능함)
그리고 카운팅 배열의 역순으로(큰값들) odd부터 쭉 채워나감. odd가 끝났다면 even이 채워지게끔 구현.
이러면 큰수는 odd에 작은수는 even에 채워져 위글정렬이 완성됨.
'''

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_len = len(nums)
        cnt = [0] * 5001
        for n in nums:
            cnt[n] += 1
        odd, even = 1, 0
        for i in reversed(range(5001)):
            if odd >= n_len and even >= n_len:
                break
            while cnt[i]:
                cnt[i] -= 1
                if odd < n_len:
                    nums[odd] = i
                    odd += 2
                elif even < n_len:
                    nums[even] = i
                    even += 2