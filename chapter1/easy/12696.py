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
            num_cases = int(input.readline())
            total_bags = 0
            for _ in range(num_cases):
                line = input.readline().strip().split()
                length = float(line[0])
                width = float(line[1])
                depth = float(line[2])
                weight = float(line[3])
                if length > 56.00 or width > 45.00 or depth > 25.00:
                    if length + width + depth <= 125.00:
                        if weight > 7.00:
                            print(0)
                        else:
                            print(1)
                            total_bags += 1
                    else:
                        print(0)
                elif weight > 7.00:
                    print(0)
                else:
                    print(1)
                    total_bags += 1
            print(total_bags)
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
