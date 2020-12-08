

# 1.4 Finding the largest or smallest N items
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

largest = heapq.nlargest(3, nums)
smallest = heapq.nsmallest(3, nums)
print(smallest)  # [-4, 1, 2]
print(largest)  # [42, 37, 23]

# another example | using key parameter
portfoilio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.10},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfoilio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfoilio, key=lambda s: s['price'])
print(cheap)
print(expensive)

# another example
heap = list(nums)
heapq.heapify(heap)
print(heap)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

# nsmallest, nlargest:
#   if n==1 then it's faster to use min,max functions
#   if n is close to N then it's faster to sort and slice
