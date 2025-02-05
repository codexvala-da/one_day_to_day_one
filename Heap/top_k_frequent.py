## Explaination: https://leetcode.com/problems/top-k-frequent-elements/
## We can use a dictionary to store the frequency of each element
## Then we can use a heap to store the top k elements based on the frequency
## Finally we return the elements from the heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(lambda:0)
        for i in nums:
            d[i]+=1
        heap = []
        for i in d:
            heapq.heappush(heap,(-d[i],i))
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans