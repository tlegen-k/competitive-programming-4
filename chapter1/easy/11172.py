
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
                num_left, num_right = input.readline().strip().split(" ")
#                print(f"left = {num_left}, right = {num_right}")
                if int(num_left) < int(num_right):
                    answer = "<"
                elif int(num_left) > int(num_right):
                    answer = ">"
                else:
                    answer = "="
                print(answer)
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
