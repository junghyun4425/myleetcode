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
'''