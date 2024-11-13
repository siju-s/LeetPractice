class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # if cycle, return -1
        # Topological sort - build adj list and use queue
        # Number of edges to node
        indegree = [0] * numCourses

        adjList = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adjList[src].append(dst)

        q = deque()    
        result = []
        finishedCourses = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        
        while q:
            src = q.popleft()
            result.append(src)
            finishedCourses += 1           
            for neighbor in adjList[src]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
     

        return result[::-1] if finishedCourses == numCourses else []
        