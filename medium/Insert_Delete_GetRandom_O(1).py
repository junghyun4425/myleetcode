# Problem Link: https://leetcode.com/problems/insert-delete-getrandom-o1/

'''
문제 요약: 숫자를 추가하고 추가된 숫자들로부터 랜덤한 값을 가져오는 클래스를 구현하는 문제.
ask:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
answer:
[null, true, false, true, 2, true, false, 2]

해석:
set을 사용해 중복 없이 간편하게 저장이 가능. set은 해쉬맵 원리이기 때문에 각종 연산에 대해 O(1)의 시간복잡도를 가짐.
랜덤값은 random모듈을 사용해서 해결.
성능 자체가 낮게 나와서 고민해본 결과 random.choice함수에서 list로 바꿀떄 O(n)의 시간복잡도를 가지는것 떄문이라 결론내림.
따라서 다음에 성능 최적화를 위해 배열하나와 hashmap을 구현해서 index를 해쉬맵에다 저장해놓는 방법으로 구현해볼것.
이러면 randrange()로 범위를 뽑은다음 index에 의해 랜덤값을 가져오니까 O(1)에 수행이 가능할거라 예상함.
'''

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.vals:
            return False
        self.vals.add(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.vals:
            return False
        self.vals.discard(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.vals))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()