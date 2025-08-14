# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj_list = defaultdict(list)
        for i, j in prerequisites:
            indegree[i] += 1
            adj_list[j].append(i)
        
        queue = deque() 
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            crs = queue.popleft()
            numCourses -= 1
            if numCourses == 0:
                return True 

            for ncrs in adj_list[crs]:
                indegree[ncrs] -= 1
                if indegree[ncrs]  == 0:
                    queue.append(ncrs)
        return False