
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
#    with open('quick-test.txt', 'rt') as input:
        with open('output.txt', 'wt') as output:
            num_cases = int(input.readline().strip())
            for _ in range(num_cases):
                num_walls = input.readline().strip()
                walls_list = input.readline().strip().split(" ")

                high_jumps, low_jumps = 0, 0

                if int(num_walls) == 1:
                    #answer = "0 0"
                    pass
                else:
                    for i in range(0,len(walls_list)-1):
                        if walls_list[i] > walls_list[i+1]:
                            low_jumps += 1
                        elif walls_list[i] < walls_list[i+1]:
                            high_jumps += 1
                        else:
                            # print("Nothing!")
                            pass

                answer = f"{high_jumps} {low_jumps}"
                print(f"Case {_+1}: {answer}")
    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
