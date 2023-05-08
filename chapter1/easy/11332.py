from time import time
import re

def digSum(n):
    if n == 0:
        return 0
    if (n % 9 == 0):
        return 9
    else:
        return (n % 9)

if __name__ == '__main__':
    start = time()

    with open('input.txt', 'rt') as input:
        with open('output.txt', 'wt') as output:
            for line in input:
                if line.strip() == "0":
                    break
                else:
                    print(digSum(int(line)))

    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
