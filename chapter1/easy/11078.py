
from time import time
import re

def readline(input):
    return input.readline().strip()

def one_int(input):
    return int(input.readline().strip())

def two_int(input):
    left, right = map(int, input.readline().strip().split())
    return left, right

def array_int(input):
    return list(map(int, input.readline().strip().split()))

def convertToNum(str):
    answer = []
    for character in str:
        number = ord(character) - 96
        answer.append(number)
    return answer

def sumOfArray(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum

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
                num_students = int(input.readline().strip())
                grades = []
                for stud in range(num_students):
                    grades.append(int(input.readline().strip()))
                max = - 100000
                max_diff = -100000
                for i in range(len(grades)-1):
                    if grades[i] > max:
                        max = grades[i]
                    if (max - grades[i+1] > max_diff):
                        max_diff = max - grades[i+1]
                print(max_diff)
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
