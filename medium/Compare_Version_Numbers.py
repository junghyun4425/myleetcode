# Problem Link: https://leetcode.com/problems/compare-version-numbers/

'''
문제 요약: 버전 두개를 비교해 어느 버전이 더 높은지 판단하는 문제. (v1이 높으면 1을, 같으면 0, 반대는 -1을 반환)
ask: v1 = "1.01", v2 = "1.001"
answer: 0

해석:
우선 버전을 . 으로 split 한 다음 숫자들을 int형으로 바꿔서 비교해 줌. (int로 바꾸는 이유는 앞에 0과같은 숫자를 제거하기 위함)
그리고 더 짧은 경우가 있는데, 이는 0으로 채워넣고 서로를 비교하게 됨.
도중에 어느쪽이 크다는걸 발견하면 바로 1 혹은 -1로 반환하고, 끝까지 모두 숫자가 같다면 0을 반환함.
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1_len, v2_len = len(v1), len(v2)
        for i in range(max(v1_len, v2_len)):
            n1 = int(v1[i]) if i < v1_len else 0
            n2 = int(v2[i]) if i < v2_len else 0
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0