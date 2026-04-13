class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # count frequencies of each task
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]  # Convert counts to negatives

        heapq.heapify(maxHeap) # create maxHeap

        # use max heap to always process the most frequent element first

        time = 0

        # A FIFO queue (deque) that holds tasks waiting for their cooldown. 
        q = deque() #pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            # If all tasks are on cooldown, jump to the next available time 
            if not maxHeap:
                time = q[0][1]

            else:
            # process next most frequent task ( we add 1 to reduce the task count since its negative)
                cnt = 1 + heapq.heappop(maxHeap)
                # if the task is not fully executed then we add it to the cooldown queue with its available time
                if cnt:
                    q.append([cnt, time + n])
            
            # If a task’s cooldown is over, move it back into the heap.
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time




        