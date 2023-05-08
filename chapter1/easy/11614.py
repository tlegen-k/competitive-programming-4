from time import time
import math

def readline(input):
    return input.readline().strip()

def one_int(input):
    return int(input.readline().strip())

def two_int(input):
    left, right = map(int, input.readline().strip().split())
    return left, right

def array_int(input):
    return list(map(int, input.readline().strip().split()))

if __name__ == '__main__':
    start = time()
    with open('input.txt', 'rt') as input:
        with open('output.txt', 'wt') as output:
            num_lines = int(input.readline().strip())
            for _ in range(num_lines):
                descrim = 1+8*float(input.readline())
                answer = (-1 + math.sqrt(descrim))/2
                print(int(answer))
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
