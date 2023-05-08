
from time import time

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
                col, row = map(int, input.readline().strip().split())
                print((col//3)*(row//3))
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
