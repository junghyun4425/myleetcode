# Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

'''
문제 요약: 히스토그램 정보가 담긴 숫자 배열에서 가장 크게 만들 수 있는 사각형의 넓이를 반환하는 문제.
ask: [2,1,5,6,2,3]
answer: 10 (5 x 2)

해석:
가둘수 있는 가장많은 빗물담기 같은 막대그래프형 문제에서 효율적으로 풀수 있는 방법은 막대가 짧아졌을때와 커졌을때 두가지 경우를 고려.
막대가 점점 커진다면, 이전의 막대는 계속해서 사이즈가 늘어날 것. 반대의 경우는 낮은 막대가 나오면 그보다 큰 막대들은 더이상 확장이 불가능.
따라서 큰 막대가 나올땐 stack에 그 사이즈를 저장하고 작은 막대가 나오면 스택에서 보다 큰막대들의 넓이를 계산하고 pop out 시킴.

예시의 답이 맞아서 제출했지만 [2,1,2] 의 경우에 오답이 생김. 답은 3인데 나의 답안이 2가 나옴.
그 이유는 cnt값으로 스택에서의 길이만 계산하기 때문에 최소길이의 막대가 중간에 있다면 이전값의 길이를 포함하지 못함.
따라서 스택에 start(index)라는 부가정보를 넣어서 막대가 갑자기 작아지는 경우, 스택에서 pop out함과 동시에 그 자리 index를 다음 스택 저장에 사용해 최대 길이를 측정.
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h_len = len(heights)
        stack = []
        ans = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                s = stack.pop()
                ans = max(ans, s[1] * (i - s[0]))
                start = s[0]
            stack.append((start, h))
        for s in stack:
            ans = max(ans, s[1] * (h_len - s[0]))
        return ans