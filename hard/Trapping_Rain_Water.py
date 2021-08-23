# Problem Link: https://leetcode.com/problems/trapping-rain-water/

'''
문제 요약: 배열의 숫자가 높이를 나타내고, 그 사이 고인 빗물들의 높이의 합을 구하는 문제.
ask: [0,1,0,2,1,0,1,3,2,1,2,1]
answer: 6

해석:
가장 간단하게 해결할 수 있는 방법으로는 역시 Brute Force로, 각 위치마다 왼쪽과 오른쪽의 maximum 높이를 구해서 최소값을 통해 빗물의 높이를 구할수 있음.
하지만 이는 O(n^2)의 시간복잡도를 가지며 중복계산이 굉장히 많다는걸 확인할 수 있음.
중복을 회피하기 위해서 현 지점에서 왼쪽과 오른쪽에 maximum 높이값들을 보관하고 있으면 됨. (즉, DP방식을 사용)
그렇게하면 O(n)으로 쉽게 최적화가 가능하지만 DP말고도 스택으로 해결이 가능하기에 스택을 사용해 문제를 해결해봄.

스택을 사용할 경우 조금더 복잡한 방법으로 해결할수 있는데, 높이가 낮아지는 경우와 높아지는 경우 두가지를 봐야함.
스택에 저장되어있는 값보다 높이가 낮을경우, 스택에 현재 위치를 저장.
반대로 높이가 높다면, 빗물의 높이를 계산해야 함. 이떄 스택에 저장되어있는 높이중 현재 높이보다 낮거나 같은 경우에대해 모두 계산해야 함.
인덱스로 거리를 구하고, 현재 높이와 스택에 저장되어있는 높이를 구해 빗물의 높이를 구하여 계산해 결과를 저장.
DP방식이 조금더 쉬운편이라고 생각하지만, 스택을 활용해서 풀어보고 싶었기에 이를 선택해 해결.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        cur = 0
        stack = []
        while cur < len(height):
            while stack and height[cur] > height[stack[-1]]:
                i = stack.pop()
                if not stack:
                    break
                ans += (cur-stack[-1]-1) * (min(height[cur], height[stack[-1]]) - height[i])
            stack.append(cur)
            cur += 1
        return ans