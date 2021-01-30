# Problem Link: https://leetcode.com/problems/word-ladder/

'''
문제 요약: beginWord 가 endWord로 몇번의 스텝안에 바뀔수 있는지 묻는 문제. (한번에 한 char만 바꿀수 있고 wordList안의 문자로만 바꿀 수 있음.)
ask: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
answer: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

해석:
하나씩 바꿔가면서 최소의 depth(step)를 찾아야 하기 때문에 queue를 활용해 레벨단위로 진행.
전체적인 방법을 생각해 내긴 했지만, 문제는 하나의 char만 바뀐걸 비교해야 한다는 점.
처음 생각해낸게 한글자를 제외하고 나머지가 같은지를 찾아보려했지만, 문자 자체가 엄청 길어진다면 최악의 성능을 보임.

효율적인 방법을 찾아보기위해 구글링 해봤는데 의외로 모든 알파벳을 다 대입하는 조금은 무식해 보일수 있는 방안이 꽤나 효율적....
시간 복잡도가 O(26 * w_len^2 * list_len^2) 인 방안으로 조금이라도 성능에 좋은 영향을 끼치기 위해 wordList를 set으로 바꿔서 찾음.
그러면 복잡도는 O(26 * w_len^2 * list_len) 으로 그나마 괜찮아지는 상황이고 실제로 속도제한을 통과함.
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [beginWord]
        words = set(wordList)
        w_len = len(beginWord)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        step = 0
        while queue:
            queue2 = []
            while queue:
                cur = queue.pop(0)
                if cur == endWord:
                    return step+1
                for i in range(w_len):
                    for c in alphabet:
                        next_word = cur[:i] + c + cur[i+1:]
                        if next_word in words:
                            queue2.append(next_word)
                            words.remove(next_word)
            queue = queue2
            step += 1
        return 0