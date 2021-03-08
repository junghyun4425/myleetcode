'''
개요: 병합정렬을 실제로 구현하기.
설명:
병합정렬을 이해하고 바로 구현.
최적화 생각없이 진행했을때의 코드 결과.
배열정보를 받아서 바로 재귀함수를 돌리려니까 배열을 인자로 넘겨버리는 굉장히 비효율적인 방법으로 해결함.
일단 한번에 정렬까지 성공하기는 했지만, 차라리 함수를 하나 더만들어서 배열이 아닌 인덱스로 정렬하게끔 하는게 필요함.

따라서 다음 리뷰를 할때는 인덱스를 넘겨서 효율적으로 정렬는걸 해봐야함.

시간복잡도: Best - O(nlogn) / Worst - O(nlogn)
공간복잡도: O(n)
'''

class MergeSort:
    def sort(self, arr):
        a_len = len(arr)
        if a_len == 1:
            return arr
        m = a_len // 2
        left = self.sort(arr[:m])
        right = self.sort(arr[m:])
        return self.merge(left, right)

    def merge(self, arr1, arr2):
        a1_len, a2_len = len(arr1), len(arr2)
        merge_arr = []
        i = j = 0
        while i < a1_len and j < a2_len:
            if arr1[i] > arr2[j]:
                merge_arr.append(arr2[j])
                j += 1
            else:
                merge_arr.append(arr1[i])
                i += 1
        if i < a1_len:
            merge_arr.extend(arr1[i:])
        if j < a1_len:
            merge_arr.extend(arr2[j:])
        return merge_arr

if __name__ == "__main__":
    arr = [5,4,6,5,4,3,8,7,1]
    merge = MergeSort()
    new_arr = merge.sort(arr)
    print(new_arr)