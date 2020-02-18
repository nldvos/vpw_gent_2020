
def still_possible(actual_cost, costs, target):
    for i in costs[actual_cost]:
       if i < target:
           return True
    return False


def check_result(cost, target):
    return target in cost

def combine(c1, c2, costs, target):
    for i in costs[c1]:
        for j in costs[c2]:
            if i + j <= target:
                costs[c1+c2].add(i+j)
            if i * j <= target:
                costs[c1+c2].add(i*j)
    return

def solve(l):
    digits = set()
    for i in range(l[0]):
        digits.add(l[i+1])
    target = l[l[0] + 1]

    costs = {}
    costs[0] = set()
    costs[1] = digits

    if target in digits:
        return 1

    result = 0

    actual_cost = 2
    while still_possible(actual_cost - 1, costs, target):
        costs[actual_cost] = set()
        for d in digits:
            costs[actual_cost].add(int(actual_cost*str(d)))

        for i in range(1, actual_cost // 2 + 2):
            c1 = i
            c2 = actual_cost - i

            combine(c1, c2, costs, target)

        if check_result(costs[actual_cost], target):
            return actual_cost
        actual_cost += 1

    return 0

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    l  = [int(s) for s in input().split()]  # read a list of integers
    print("{}".format(solve(l)))
    # check out .format's specification for more formatting options

