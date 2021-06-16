from typing import List


class Solution:

    def insertToMinHeap(self, min_heap: List[int], node: int):
        min_heap.append(node)
        k = len(min_heap) - 1
        # swim
        while k >= 1 and (min_heap[int(k / 2)] > min_heap[k]):
            min_heap[k], min_heap[int(k / 2)] = min_heap[int(k / 2)], min_heap[k]
            k = int(k / 2)


    def addAndDeleteRoot(self, min_heap: List[int], node: int):
        min_heap.append(node)
        min_heap[1], min_heap[len(min_heap) - 1] = min_heap[len(min_heap) - 1], min_heap[1]
        # 다시 정렬
        min_heap.pop()
        k = 1
        # sink
        while 2*k <= len(min_heap)-1:
            if 2*k+1 > len(min_heap) -1:
                if min_heap[k] > min_heap[2*k]:
                    min_heap[k], min_heap[2*k] = min_heap[2*k], min_heap[k]
            else:
                if min_heap[2*k]< min_heap[2*k+1]:
                    if min_heap[k] > min_heap[2*k]:
                        min_heap[k], min_heap[2 * k] = min_heap[2 * k], min_heap[k]
                else:
                    if min_heap[k] > min_heap[2 * k+1]:
                        min_heap[k], min_heap[2 * k +1] = min_heap[2 * k+1], min_heap[k]
            k = 2*k


    def addToMinHeap(self, min_heap: List[int], i: List[int]):
        if len(min_heap) == 1:
            min_heap.append(i[1])
        else:
            if min_heap[1] > i[0]:
                # insert
                self.insertToMinHeap(min_heap, i[1])
            else:
                # delete and insert root
                self.addAndDeleteRoot(min_heap, i[1])


    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # start time 기준으로 정렬
        intervals.sort(key=lambda e: e[0])
        min_heap = [0]
        for i in intervals:
            self.addToMinHeap(min_heap, i)
        return len(min_heap)-1


solution = Solution()
print(solution.minMeetingRooms([[0,30],[5,10],[15,20]]))
