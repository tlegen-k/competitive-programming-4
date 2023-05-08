def toString(List):
    return ''.join(List)


def permute(input, l, r):
    if l == r:
        print(toString(input))
    else:
        for i in range(l, r):
            input[l], input[i] = input[i], input[l]
            permute(input, l+1, r)
            input[l], input[i] = input[i], input[l]


string = "ABCDEFGHIJ"
n = len(string)
a = list(string)

permute(a,0,n)
