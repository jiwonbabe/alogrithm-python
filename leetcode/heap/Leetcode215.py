from typing import List


class Solution:
    def insertToMaxHeap(self, max_heap: List[int], n: int):
        # just insert as an last element
        max_heap.append(n)
        # swim
        i = len(max_heap) - 1
        while i > 1 and max_heap[i] > max_heap[int(i / 2)]:
            max_heap[i], max_heap[int(i / 2)] = max_heap[int(i / 2)], max_heap[i]
            i = int(i / 2)

    def findLargerChild(self, max_heap: List[int], i: int) -> int:
        if 2 * i + 1 > len(max_heap) - 1:
            # 오른쪽 자식이 없는 경우
            return 2 * i
        else:
            if max_heap[2 * i] >= max_heap[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def deleteMaxFromMaxHeap(self, max_heap: List[int]):
        # swap first and last node
        max_heap[1], max_heap[len(max_heap) - 1] = max_heap[len(max_heap) - 1], max_heap[1]
        # delete last node
        max_heap.pop()
        # sink
        i = 1
        length = len(max_heap) - 1
        while 2 * i <= length:
            larger_child_index = self.findLargerChild(max_heap, i)
            # 중간에 자리를 찾았으면 탈출
            if max_heap[i] >= max_heap[larger_child_index]:
                break
            # 못 찾았으면 자리 바꾸고
            max_heap[i], max_heap[larger_child_index] = max_heap[larger_child_index], max_heap[i]
            # 포인터 변경
            i = larger_child_index

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # make max heap
        # sink 할때 2k 계산해야 하니까 1부터 시작해야 함.
        max_heap = [0]
        for n in nums:
            self.insertToMaxHeap(max_heap, n)
        # delete max in max_heap
        for i in range(k-1):
            self.deleteMaxFromMaxHeap(max_heap)
        return max_heap[1]

solution = Solution()
solution.findKthLargest([3,2,1,5,6,4],
2)