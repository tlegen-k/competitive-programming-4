# Given n random integers, print the distinct (unique) integers in sorted order.

input = [1,2,3,4,4,3,16,3,1]

distinct = set()

for item in input:
    if item not in distinct:
        distinct.add(item)


print(distinct)
