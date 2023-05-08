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
    regex = re.compile('[^a-zA-Z]')

    with open('input.txt', 'rt') as input:
        with open('output.txt', 'wt') as output:
            while True:
                line1 = input.readline()
                line2 = input.readline()
                if not line2: break # EOF

                line1_stripped = regex.sub('',line1).lower()
                line2_stripped = regex.sub('',line2).lower()

                line1_num = convertToNum(line1_stripped)
                line2_num = convertToNum(line2_stripped)

                sum1 = sumOfArray(line1_num) 
                sum2 = sumOfArray(line2_num)

                sum1_one_digit = digSum(sum1)
                sum2_one_digit = digSum(sum2)

                if sum1_one_digit <= sum2_one_digit:
                    answer = sum1_one_digit/sum2_one_digit
                else:
                    answer = sum2_one_digit/sum1_one_digit
                print("{:0.2f} %".format(answer*100))
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
