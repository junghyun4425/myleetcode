# Problem Link: https://leetcode.com/problems/candy/

'''
문제 요약: 아이에게 사탕을 주는데, ratings에 따라 좌우의 애들보다 적게 혹은 많이 받게끔 해서 주는 모든 캔디의 수를 구하는 문제.
ask: [1,0,2]
answer: 5 (모든 아이에게 최소 1개씩 줘야하는 조건이 있음. 따라서 순서대로 각각 2,1,2개의 캔디를 줘야함)

해석:
처음에 문제를 정확하게 이해하지 못해서 좌우측 모두 하나씩 검사하며 캔디수를 계산하는 방법으로 해봄. (Brute Force)
좌측이나 우측에서 한번이라도 캔디 수가 갱신되면 trigger를 통해 알려준 다음 다시 계산하도록 함. O(n^2)
이때 문제에 대한 이해도가 높아져서 다른 효율적인 방법을 찾기 시작함.

비슷한 문제는 아니지만 예전에 분할정복 문제에서 배열 두개로 이런식의 까다로운 문제를 해결했던 기억이 있었기에 조금은 수월하게 푼 문제.
인덱스 i를 기준으로 왼쪽과 오른쪽 둘다 신경써야 하는데, 배열을 두개쓰면 효율적으로 해결이 가능.
좌측으로 이동하는걸 계산하는 배열 하나와, 우측으로 이동하는걸 계산하는 배열 하나 총 배열 두개 구함.
그리고 둘중 큰값을 가지는 숫자가 최종적으로 그 아이가 받는 캔디의 수.를 (ratings이 계속 내려가는 경우와 계속 올라가는 경우 각각에 대해 최대값을 찾는 느낌)

배열을 하나만 쓰고도 가능하다 생각하여 다시 도전.
우선 좌측으로 이동하면서 캔디를 구하고, 다시 같은 배열로 우측으로 이동. 단, 이때는 이전값과 우측이동으로 올값 중에서 최대값을 가지면 해결.
max(candy[i], candy[i+1]+1)
앞에 값이 좌측에서 구한값, 뒤에값이 우측에서 출발했을때 새로 구하는 값.
'''

# Optimized
class Solution:
    def candy(self, ratings: List[int]) -> int:
        r_len = len(ratings)
        candy = [1] * r_len

        for i in range(1, r_len):
            if ratings[i - 1] < ratings[i]:
                candy[i] = candy[i - 1] + 1
        for i in reversed(range(r_len - 1)):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        return sum(candy)

# Brute Force
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        r_len = len(ratings)
        candy = [1] * r_len
        trig = True
        while trig:
            trig = False
            for i in range(r_len):
                if i < r_len-1 and ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                    candy[i] = candy[i+1]+1
                    trig = True
                if i > 0 and ratings[i] > ratings[i-1] and candy[i] <= candy[i-1]:
                    candy[i] = candy[i-1] + 1
                    trig = True
            print(candy)
        return sum(candy)
'''