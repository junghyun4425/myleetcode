# Problem Link: https://leetcode.com/problems/rectangle-area/

'''
문제 요약: 사각형1: (A,B)=좌측아래, (C,D)=우측위 / 사각형2: (E,F)=좌측아래, (G,H)=우측위
가 주어질떄 사각형의 총 넓이를 구하는 문제.
ask: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
answer: 45

해석:
처음 시도할때는 조건절로 여러부분에 대해서 시도를 하려함. 사각형1이 사각형2에 포함될때, 완전히 다를때, 서로 걸쳐있을때.
하다보니 max(A,B) 라는걸 써서 좀더 편하게 할 수 있었는데, 생각해보니 작은값의 max와 큰값의 min을 활용하면 쉽게 구할 수 있다고 생각함.
고민 끝에 왼쪽과 오른쪽의 큰값 작은값을 찾아서 비교하면서 풀게되었고 쉽게 해결 됨.
'''

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area = (C-A) * (D-B) + (G-E) * (H-F)
        sub = 0
        max_bottom = max(B, F)
        max_left = max(A, E)
        min_top = min(D, H)
        min_right = min(G, C)
        if max_bottom < min_top and max_left < min_right:
            sub = (min_right - max_left) * (min_top - max_bottom)
        return area - sub