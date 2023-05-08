
from time import time
import re

def digSum(n):
    if n == 0:
        return 0
    if (n % 9 == 0):
        return 9
    else:
        return (n % 9)
def getMultipleMax(arr):
    indices = []
    maxim = max(arr)
    for i in range(len(arr)):
        if arr[i] == maxim:
            indices.append(i)
    return indices

if __name__ == '__main__':
    start = time()

    with open('input.txt', 'rt') as input:
        with open('output.txt', 'wt') as output:
            num_cases = int(input.readline().strip())
            for _ in range(num_cases):
                relevance_array = []
                indices = []
                sites_array = []
                answer = []
                for i in range(10):
                    line = input.readline().strip().split()
                    sites_array.append(line[0])
                    relevance_array.append(int(line[1]))
                indices = getMultipleMax(relevance_array)
                print(f"Case #{_+1}:")
                for i in range(len(indices)):
                    print(sites_array[indices[i]])
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
