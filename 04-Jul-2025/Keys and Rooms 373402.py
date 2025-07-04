# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()

        queue = collections.deque([0])
        visited.add(0)

        while queue:
            room = queue.popleft()
            for i in rooms[room]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)     
        return len(visited) == len(rooms)



        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        