# Problem Link: https://leetcode.com/problems/longest-absolute-file-path/

'''
문제 요약: 디렉터리에 존재하는 모든 파일 경로의 길이중 가장 긴 값을 반환하는 문제. (\n은 디렉터리안을, \t는 몇번째 디렉터리에 포함되는지를 설명함)
ask: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
answer: 20 ("dir/subdir2/file.ext"의 길이)

해석:
스택을 사용하면 간단하게 해결할 수 있는 문제.
우선 "\n" 으로 split 한 파일, 경로 이름으로 나눠서 탐색.
다음으로 "\t"의 개수를 카운팅 한다음, stack의 길이보다 더 짧다면 stack을 pop() 해서 경로를 맞춰줌. (스택의 길이가 디렉토리의 깊이를 의미함)
만약 스택에 저장한 string안에 '.' 이 존재한다면 파일을 의미하기 때문에 길이를 측정.
한가지 주의해야 할 점은, 스택에 저장해놓은 값들은 순수히 파일or디렉토리의 길이를 말함. 즉, 디렉토리를 구분하는 '/' 길이를 포함시켜줘야 함.
스택의 길이가 깊이를 의미하기 때문에 len(stack)-1 이 '/' 을 카운팅한 결과가 됨.
'''

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        cur_len = 0
        max_len = 0
        for s in input.split("\n"):
            tabs = s.count("\t")
            while tabs < len(stack):
                cur_len -= stack.pop()
            stack.append(len(s) - tabs)
            cur_len += len(s) - tabs
            if '.' in s:
                max_len = max(max_len, cur_len + len(stack) - 1)
        return max_len