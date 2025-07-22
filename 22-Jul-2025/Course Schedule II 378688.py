# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        result = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = collections.deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)

        while queue:
            c = queue.popleft()
            result.append(c)

            for neighbours in graph[c]:
                indegree[neighbours] -= 1
                if indegree[neighbours] == 0:
                    queue.append(neighbours)
        
        if len(result) == numCourses:
            return result
        else:
            return []

        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        