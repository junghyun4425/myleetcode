# Problem Link: https://leetcode.com/problems/merge-sorted-array/

'''
문제 요약: 두개의 정렬된 숫자리스트를 하나로 합치는 문제. (단, 추가적 메모리는 사용하지 말것)
ask: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
answer: [1,2,2,3,5,6]

해석:
간단하지만 이상하게 꼬여 오래걸린 문제.
보통 공간복잡도 O(1)을 만족하려면 포인터 두개를 써서 해결하는게 일반적이기에 생각없이 right = m+n-1, left = m-1
로 설정해 뒤에서 바꿔가는 식으로 시도. 하지만 뭔가 풀면 풀수록 꼬여가기 시작.
예시는 맞지면 제출하면 별 색다른 예외로 몇번 실패를 맛보고 처음부터 다시 차근차근 생각해보기로 함.
그냥 p1 = m-1, p2 = n-1 로해서 배열 뒤에서부터 하나씩 넣어주면 너무 쉽게 풀림. (예외 생각할 일도 없음)
쉬운 난이도 중에서 가장 시간이 오래걸렸던 문제...
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1
        for i in range(m+n-1, -1, -1):
            if p1 < 0 or p2 < 0:
                break
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]