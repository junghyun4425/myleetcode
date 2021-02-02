# Problem Link: https://leetcode.com/problems/palindrome-partitioning/

'''
문제 요약: 문자의 palindrome 조합을 모두 찾아 반환하는 문제.
ask: "aab"
answer: [["a","a","b"],["aa","b"]]

해석:
그렇게 어려워 보이진 않는데 생각보다 헤맨 문제. 문자열을 하나씩 분할해서 DFS 방식으로 쭉 풀면 될것 같았는데 어떤 인자값을 전달해줘야 하는지 정하질 못했던 문제.
처음엔 시작index, 끝index 두개로 넘겨서 시도했으나, palindrome 조합을 모을때 생각보다 번거로워서 추가.
끝index는 이게 왜필요한지 생각도 않고 그냥 넣었었음... 그러다보니 로직이 자꾸 꼬임.
나중에 가서야 이게 필요없다는걸 깨닫고, for루프 안에서 끝index를 분할해서 재귀함수를 수행하게 함.
그냥 전반적으로 집중이 잘 안된듯함.
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        s_len = len(s)

        def checkPal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(pals, i):
            if i >= s_len:
                ans.append(pals)
                return
            for j in range(i, s_len):
                if checkPal(i, j):
                    backtrack(pals + [s[i:j + 1]], j + 1)

        backtrack([], 0)
        return ans
