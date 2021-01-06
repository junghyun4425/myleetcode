# Problem Link: https://leetcode.com/problems/simplify-path/

'''
문제 요약: 입력으로 들어오는 Unix 스타일의 절대경로를 간단하게 정리하여 반환하는 문제.
ask: path = "/a/./b/../../c/"
answer: "/c"

해석:
처음엔 나누는방법을 생각 못하고 수많은 if문을 비효율적으로 사용해서 스택에 저장하여 해결하려 함.
도저히 이건 아닌거 같다 생각하고 고민 끝에 '/'로 나누면 상당히 쉽게 풀리는걸 깨달음...
특정 패턴이 보이면 나눠놓고 보자 라는 교훈?을 긴 시간동안 몸소 체득.
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        sp = path.split('/')
        sp = [d for d in sp if d != '.' and d != '']
        stack = []

        for d in sp:
            if d == '..':
                if stack: stack.pop()
            else:
                stack.append(d)
        return '/' + "/".join(stack)