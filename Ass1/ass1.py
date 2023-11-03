import time
import math
import random
import numpy as np
import matplotlib.pyplot as plt
def iterate(base, pow):
    res = 1
    for i in range(pow):
        res *= base
    return res

def recur(base, pow):
    if pow == 1:
        return base
    res = recur(base, pow // 2)
    if pow % 2 == 0:
        return res * res
    else:
        return res * res * base

def mergeSort(n):
    if len(n) == 1:
        return n
    if len(n) == 2:
        if n[0] > n[1]:
            return [n[1], n[0]]
        else:
            return n
    splitArrays = np.array_split(n, 2)

    arr1 = mergeSort(splitArrays[0])
    arr2 = mergeSort(splitArrays[1])

    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result
    
def binarySearch(x, n):
    left = 0
    right = len(n) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if n[mid] == x:
            return True
        elif n[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
    
    
def findPairs(n, x):
    res = []
    n = mergeSort(n)
    for i in n:
        t = n
        t.remove(i)
        if binarySearch(x-i, t):
            res.append({i, x-i})
    return res

# x = []
# y = []
# nlogn = []

# for i in [5, 100, 1000, 10000, 100000]:
#     arr = []
#     for j in range(i):
#         arr.append(random.randint(-9, 9))
#     print(arr)
#     start = time.time()
#     findPairs(arr, 9)
#     period = time.time() - start
#     x.append(i)
#     y.append(period * 100000)
#     nlogn.append(i * np.log(i))

# plt.plot(x, y)
# plt.plot(x, nlogn)
# plt.show()


x = []
yiterate = []
yrecur = []
logn = []

for i in range(1, 200000, 10000):
    start = time.time()
    iterate(5, i)
    iteration = time.time() - start
    
    start = time.time()
    recur(5, i)
    recursion = time.time() - start

    x.append(i)
    yiterate.append(iteration* 100)
    yrecur.append(recursion*100)
    logn.append(np.log(i))

plt.plot(x, yiterate)
plt.plot(x, yrecur)
plt.plot(x, logn)
plt.show()
