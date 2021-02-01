# Problem Link: https://leetcode.com/problems/word-ladder-ii/

'''
문제 요약: beginWord 가 endWord로 가는 최소 경로를 모두 출력. (한번에 한 char만 바꿀수 있고 wordList안의 문자로만 바꿀 수 있음.)
ask: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
answer: [
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

해석:
여태 풀었던 hard난이도 문제중 가장 멘탈이 나간 문제. 이전 Word_Ladder 문제와 비슷하겠거니 생각했지만 의외로 엄청 생각해야 할게 많았음.
우선 이전의 코드에 몇가지를 추가하면 다 될것 같았음. BFS로 그래프를 만들고, 그 그래프를 DFS로 찾아가는 방식.
안일하게 점검도 안해보고 쭉 코딩했다가 상당히 많은 변수에 부딪힘.
1.wordList 안에 시작문자가 존재함. (지워줘야 함)
2.이전에 중복 방지를 위해 Set을 만들어 하나씩 지워줬는데 이걸 사용하면 같은 레벨에 있는 word들이 참고를 못함.
    즉, 중복을 허용해야 하는 부분이 있는데 제거하니까 그래프가 완성되질 못함.
3.깊이값이 필요없을줄 알았는데 필요함. (DFS에서 출력할때)
4.visited 같은 역할을 할게 필요함. 물론 레벨마다 visited_at_this_level 같은걸 따로만들어서 레벨구간 끝날때 합쳐야함.
등등 굉장히 많은 변수에 계속 예외를 만나 실패하다 오늘은 여기까지만 하고 내일 다시 도전해 보기로 함.
이때는 여러 조건들을 고려해 범용적이게 문제를 풀기로 결정.

2일차.
이전에 "abcd...xyz" 라는 아파벳 키워드를 다 돌아봤던것을 메모리를 더 사용해 성능을 늘리기로함.
wordList에 존재하는 모든 단어들을 해시맵에 넣는 작업. 단, 한글자씩 * 로 대체해서 비교하기 편하게 구현.
ex) wordList = [hit, hot] hmap = {"h*t": ["hit", "hot"], "*it": ["hit"], "*ot": ["hot"], ...}
메모리공간 낭비가 심하지만 코드가 깔끔해지고 해시맵이고 이전처럼 이중 for문을 돌지 않아도 되기 때문에 성능향상.
BFS로 그래프를 완성하면 다음엔 DFS방식으로 그 깊이만큼의 리스트들을 추출해 냄.
결국 어제 문제점들을 모두 보완하면서 해결.
'''

from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        if endWord not in wordList:
            return []
        wordMap = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                star_w = w[:i] + "*" + w[i + 1:]
                wordMap[star_w].append(w)
        queue = [beginWord]
        found = False
        visited = {beginWord}
        graph = defaultdict(set)
        depth = 0
        while queue and not found:
            depth += 1
            queue2 = []
            visited_level = set()
            while queue:
                w = queue.pop(0)
                for i in range(len(w)):
                    star_w = w[:i] + "*" + w[i + 1:]
                    for nextWord in wordMap[star_w]:
                        if nextWord == w:
                            continue
                        if nextWord not in visited:
                            if nextWord == endWord:
                                found = True
                            graph[w].add(nextWord)
                            queue2.append(nextWord)
                            visited_level.add(nextWord)
            queue = queue2
            visited = visited.union(visited_level)

        def dfs(cur_w, path, cur_d):
            if cur_d > depth:
                return
            if cur_d == depth and cur_w == endWord:
                ans.append(path)
                return
            for node in graph[cur_w]:
                dfs(node, path + [node], cur_d + 1)

        dfs(beginWord, [beginWord], 0)
        return ans