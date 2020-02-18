
def accumulate(l):
    res = [l[0]]

    for i in range(1, len(l)):
        res.append(l[i] + res[i-1])

    res.append(res[-1])
    res.insert(0, 0)
    return res

def solve(l):
    count = 0

    if len(l) == 0:
        return 0

    acc_l = accumulate(l)

    # print ("{}".format(l))
    # print ("{}".format(acc_l))

    for i in range(1 + len(l)):
        for j in range(i, 1 + len(l)):
            part1 = acc_l[i]
            part2 = acc_l[j + 1] - acc_l[i]
            part3 = acc_l[-1] - acc_l[i + 1]
            if part1 == part2 and part2 == part3:
                count += 1
            # print ("{} {} {} {} {}".format(i, j, part1, part2, part3))


    return count

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    l  = [int(s) for s in input().split()]  # read a list of integers
    arr = []
    for j in range(l[0]):
        arr.append(int(input()))
        pass

    print("{} {}".format(i, solve(arr)))
    # check out .format's specification for more formatting options

