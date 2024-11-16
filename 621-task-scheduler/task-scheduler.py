class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Keep count of frequencies and move them to Max PQ

        freq = Counter(tasks)
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        # store map of -count, time
        q = deque()
          
        while maxHeap or q:
            time += 1
            if not maxHeap:
                # jump to time
                time = q[0][1] 

            else:
                count = heapq.heappop(maxHeap) + 1
                if count:
                    q.append([count, time + n])
                
            # remove from queue when time matches 
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
            


        return time    




