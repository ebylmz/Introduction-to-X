import random
import time

def naiveSearch(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer
# we will leverage the fact that our list is SORTED
def binarySearch(l, target, low = None, high = None):
    if low == None:
        low = 0
        high = len(l) - 1

    if low > high:
        return -1
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binarySearch(l, target, low, midpoint - 1)
    else:
        return binarySearch(l, target, midpoint + 1, high)


# proves binary search better than naive search
if __name__ == "__main__":
    length = 1000
    sortedList = set() # use set to prevent dublicate values
    
    while len(sortedList) < length:
        sortedList.add(random.randint(-3 * length, 3 * length))
    
    sortedList = sorted(list(sortedList)) # sort the list for binary search

    # search each item on the sortedList and compare their execution time
    start = time.time()
    for target in sortedList:
        naiveSearch(sortedList, target)
    end = time.time()
    print("Naive search time: ", (end - start) / length, " seconds")

    start = time.time()
    for target in sortedList:
        binarySearch(sortedList, target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, " seconds")