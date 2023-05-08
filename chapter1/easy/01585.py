
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
            num_cases = int(input.readline().strip())
            for _ in range(num_cases):
                line = input.readline().strip()
                score_counter = 0
                score_final = 0
                for i in range(len(line)):

                    if (line[i] == "O"):
                        score_counter += 1
                        score_final += score_counter
                    else:
                        score_counter = 0
                print(score_final)
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
