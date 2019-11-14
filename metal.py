import itertools

def d(s, dist):
    m = 0
    for comb in itertools.combinations(s, 2):
        res = dist[comb[0]][comb[1]]
        if res > m:
            m = res
    return m

def calculate(s1, s2, dist):
    return d(s1, dist) + d(s2, dist)

def solve(dist, n):
    indices = range(0,n)
    mi = 999999999999999999
    for i in range(1,n):
        for comb in itertools.combinations(set(indices), i):
            first = set()
            second = set(indices)
            first_augmented = first.union(comb)
            second_demented = second.difference(comb)
            res = calculate(first_augmented, second_demented, dist)
            if res < mi:
                mi = res
    return mi



# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for x in range(1, t + 1):
    n  = int(input())
    dist = [0]*n
    for i in range(0,n):
        dist[i] = [0]*n
    for i in range(0,n-1):
        dist_i = [int(s) for s in input().split(" ")]
        for j in range(1,n-i):
            dist[i][i+j] = dist_i[j-1]
            dist[i+j][i] = dist_i[j-1]
    print("{} {}".format(x, solve(dist, n)))

