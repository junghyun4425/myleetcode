# Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/

'''
문제 요약: 숫자 배열에서 연속된 숫자의 최대길이를 반환하는 문제. (단, O(n) 시간 복잡도를 가지게 시도)
ask: [100,4,200,1,3,2]
answer: 4 (1,2,3,4)

해석:
우선 hashmap 또는 set 과같이 검색에 상수 시간복잡도를 가지는 자료구조를 활용해야 함.
하지만 여기서 뭔가 좋은 아이디어가 안떠오름... 해시맵으로 n-1값들을 연결시켜보려 해도 결국은 O(n^2)이 나옴..
결국 정렬로 해결하고 어떤식으로 풀었나 확인을 함.
O(n) solution인데 O(n^2) 솔루션처럼 생겼지만, 자세히 보면 n-1 일때 루프를 돌지 않게 하는게 핵심.
O(n)에 다와갔는데 포기한게 아쉬웠던 문제. for문안에 while문 넣어도 O(n)이 될수 있다는걸 다시한번 명심하고 연구해 보도록 해야함!!
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        n_set = set(nums)
        for n in n_set:
            if n-1 not in n_set:
                cur = n
                size = 1
                while cur+1 in n_set:
                    cur += 1
                    size += 1
                max_len = max(max_len, size)
        return max_len