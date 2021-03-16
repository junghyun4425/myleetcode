# Problem Link: https://leetcode.com/problems/remove-invalid-parentheses/

'''
문제 요약: 올바른 괄호를 완성하기 위해서 제거해야하는 최소 괄호 개수에 대해 모든 경우를 반환하는 문제.
ask: s = "(a)())()"
answer: ["(a())()","(a)()()"]

해석:
이상하게 괄호문제가 나오면 정말 자신이 없어짐. 익숙하지 않아서 그런건지 모르겠지만 나중에 괄호문제만 종합해서 싹 다시 풀어봐야겠음.
그래서 조금 생각하다가 대충 DFS로 풀면될거같긴 한데.. 하고 그냥 솔루션의 이론부분을 봄.
이론을 보다보니 내가 자신없어하는 구간을 찾음!!
괄호의 반대쌍 ")(" 같은경우를 도저히 생각해내지 못하고있어서 포기한것임. 하지만 의외로 이걸 처리하는데 굉장히 간단했음.
단지 left > right 개수인 상태에서 ')'가 입력으로 올때 keeping하는 경우를 생각하지 않고 지워버리면 그만인것.
이렇게 해주면 left, right 숫자만으로 현재 괄호가 완성된것인지 알수 있음. (자신감을 찾음)
공유자원 set과 min_rm을 nonlocal로도 쓸수있지만 잘 쓰지 않도록 권장하는 분위기의 글을 읽은 이후로는 인스턴스 변수에 저장하고 쓰는식으로 바뀌게됨.
알고리즘 자체는 단순함.
인자로 들어온 다음의 string이 '(' 혹은 ')' 일때 삭제하는경우와 포함시킨경우 모두를 검사하는 방식.
둘다 아닐땐 상관없기 때문에 그냥 넘김.
성능 자체는 상위권이 아니기 때문에 아마도 가지치기 기법으로 쓸데없는 재귀를 호출하지 않도록 하는것 같음.
다음 복습할때 이 부분을 고민해보기.
'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.min_rm = float('inf')
        self.ans = set()
        s_len = len(s)
        def dfs(i, left, right, rm_cnt, path):
            if i == s_len:
                if left == right:
                    if self.min_rm > rm_cnt:
                        self.ans = {path}
                        self.min_rm = rm_cnt
                    elif self.min_rm == rm_cnt:
                        self.ans.add(path)
                return
            if s[i] == '(':
                dfs(i+1, left+1, right, rm_cnt, path+s[i])
                dfs(i+1, left, right, rm_cnt+1, path)
            elif s[i] == ')':
                if left > right:
                    dfs(i+1, left, right+1, rm_cnt, path+s[i])
                dfs(i+1, left, right, rm_cnt+1, path)
            else:
                dfs(i+1, left, right, rm_cnt, path+s[i])
        dfs(0,0,0,0,'')
        return list(self.ans)