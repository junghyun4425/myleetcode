# Problem Link: https://leetcode.com/problems/count-of-range-sum/

'''
문제 요약: [lower, upper] 에 포함되는 값을 가진 range sum 의 개수를 구하는 문제.
ask: nums = [-2,5,-1], lower = -2, upper = 2
answer: 3 ([0,0], [2,2], [0,2] 세가지)

해석:
예전에 이보다 좀더 쉬운 문제를 해쉬맵을 통해서 풀었던 기억이 있어서 쉽게 접근했던 문제.
summ을 통해 배열을 하나씩 더해가면서 record에 lower부터 upper까지의 값을 빼가면서 존재하는지 확인함.
summ - [lower ~ upper] 의 결과가 record안에 있다면 그 범위에 속하는 range sum이 있음을 의미하며 이는 한개이상이 될 수 있음.
모든 경우의수를 cnt에 다 더해주어 그 결과를 구함.
시간복잡도는 O(n*(upper-lower+1)) 이 되기떄문에 효율이 좋다고는 말할수 없지만 공간복잡도가 O(n)으로 최상위 효율을 가짐.
다음번엔 공간복잡도를 O(n^2)지만 시간복잡도를 O(nlogn)으로 가지는 segment tree를 이용해 풀어보는 것으로 복습을 할것.
'''

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        record = defaultdict(int)
        record[0] = 1
        cnt = 0
        summ = 0
        for n in nums:
            summ += n
            for target in range(lower, upper+1):
                if summ - target in record:
                    cnt += record[summ-target]
            record[summ] += 1
        return cnt