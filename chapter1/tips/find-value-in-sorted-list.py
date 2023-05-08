def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

arr = [i for i in range(1000000)]
print(len(arr))

#search for 10
x = 10
result = binary_search(arr, 1, len(arr)-1, x)
print(result)


arr = [3, 5, 10, 43, 47, 50, 67, 79, 81, 86, 101]
x = 50
result = binary_search(arr, 1, len(arr)-1, x)

print(result)
