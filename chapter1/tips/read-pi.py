from mpmath import mp

entry = input("Please enter precision to print number Pi:")

mp.dps = int(entry) + 1

print(mp.pi)
