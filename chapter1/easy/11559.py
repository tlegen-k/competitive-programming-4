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
            while True:
                first_line = input.readline().strip().split()
                if not first_line:
                    break

                n_part   = int(first_line[0])
                budget   = int(first_line[1])
                n_hotels = int(first_line[2])
                n_weeks  = int(first_line[3])
                hotels   = []
                prices   = []
                for _ in range(n_hotels):
                    price = int(input.readline().strip())
                    prices.append(price)
                    availab = input.readline().strip().split()
                    availab = [int(x) for x in availab]
                    hotels.append(availab)
                #print(hotels)
                
                index_possib_hotels = []            
                for i in range(len(hotels)):
                    if max(hotels[i]) >= n_part:
                        index_possib_hotels.append(i)

                # if there is no enough space in any hotel not possible
                if len(index_possib_hotels) == 0:
                    print("stay home")
                min_cost = 2000001
                for item in index_possib_hotels:
                    if prices[item] * n_part < min_cost:
                        min_cost = prices[item] * n_part
                if min_cost > budget:
                    print("stay home")
                else:
                    print(min_cost)



    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
