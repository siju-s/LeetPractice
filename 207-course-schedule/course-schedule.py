class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        adjList = [[] for i in range(numCourses)]
        q = deque()

        for src, dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finishedCourses = 0
        while q:
            course = q.popleft()

            for neigh in adjList[course]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    q.append(neigh)

            finishedCourses += 1

        return finishedCourses == numCourses            

        