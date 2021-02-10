# Problem Link: https://leetcode.com/problems/lru-cache/

'''
문제 요약: LRU_Cache 를 구현하는 문제. (캐시에 없으면 -1을 반환)
ask:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
answer: [null, null, null, 1, null, -1, null, -1, 3, 4]

해석:
쉽게 풀수 있을거라 생각했는데 생각보다 난해했던 문제. 애초에 LRU 알고리즘을 배열로 구현해서 성능은 떨어지는 편.
구현하는 것 자체가 굉장히 재밌었고, 다음에 시간이 나면 배열을 힙큐로 바꿔서 풀어볼 생각.
'''

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.cur_capacity = 0
        self.lru = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.lru.remove(key)
        self.lru.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.cur_capacity < self.capacity:
            if key in self.cache:
                self.lru.remove(key)
            else:
                self.cur_capacity += 1
            self.lru.append(key)
            self.cache[key] = value
        elif self.cur_capacity == self.capacity and key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            self.cache[key] = value
        else:
            del self.cache[self.lru[0]]
            self.lru.pop(0)
            self.cache[key] = value
            self.lru.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)