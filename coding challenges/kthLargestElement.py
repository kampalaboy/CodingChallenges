arr = [2,4,3,5,15,10,9]
k = 4

import heapq
def kLargest(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

print(kLargest(arr,k))