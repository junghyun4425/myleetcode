# Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

'''
문제 요약: 정렬된 숫자배열이 입력으로 오면 두 숫자의 합이 target과 같아지는 index 두개를 반환하는 문제. (정답은 하나만 존재)
ask: numbers = [2,7,11,15], target = 9
answer: [1,2] (첫번째, 두번째 숫자)

해석:
정렬이 되어있고 하나의 숫자를 뺀 결과가 배열안에 있는지 체크하는 문제.
즉, 가장 작은수(왼쪽)와 가장 큰수(오른쪽)를 더해서 target보다 작으면 왼쪽을 한칸 올려주고, 반대의 경우는 오른쪽을 한칸 내려줌.
두개의 포인터로 O(n) 의 시간 복잡도를 가지는 솔루션.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1