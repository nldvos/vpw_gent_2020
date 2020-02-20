
def solve(a):
    if len(a) == 0: # not necessary
        return 0, 0
    return min(a), max(a)

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(int(input()))
    mi, ma = solve(arr)

    print("{} {} {}".format(i, mi, ma))
