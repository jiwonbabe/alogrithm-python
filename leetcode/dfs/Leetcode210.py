from typing import List


class Solution:
    # find Visiting or Unvisited
    def findNotVisited(self, adj: List[List[int]], index: int, order: List[int]) -> int:
        if len(adj[index]) == 0:
            return -1
        for i in adj[index]:
            if i not in order:
                return i
        return -1

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # make adjancy list
        adj = []
        for i in range(numCourses):
            filtered = list(map(lambda x: x[0], filter(lambda x: x[1] == i, prerequisites)))
            adj.append(filtered)

        stack = []
        order = []
        # dfs
        for i in range(numCourses):
            # different component check
            if i not in order:
                stack.append(i)
                target_index = i
                while len(stack) != 0:
                    not_visited = self.findNotVisited(adj, target_index, order)
                    if not_visited == -1:
                        order.append(stack.pop())
                        if len(stack) == 0:
                            break
                        target_index = stack[-1]
                    else:
                        # cycle check
                        if not_visited in stack:
                            return []
                        else:
                            stack.append(not_visited)
                        target_index = not_visited

        order.reverse()
        return order
    
solution = Solution()
print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
