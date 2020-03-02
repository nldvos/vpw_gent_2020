
def solve(planets, stops):
    # print (stops, planets)

    if stops == 0:
        # print('in final stop: {}'.format(abs(planets[0] - planets[-1])))
        return abs(planets[0] - planets[-1])

    res = 0

    for i in range(1,len(planets) - stops):
        # new_planets = [abs(a - planets[i]) for a in planets[i + 1:]]
        new_planets = [a for a in planets[i:]]
        # print(new_planets)

        cost = min(abs(planets[i] - planets[0]), solve(new_planets, stops-1))

        # print ('planets[i]: {}'.format(planets[i]))
        # print(new_planets)
        # print (cost)
        # print ()

        if cost > res:
            res = cost

    return res

if __name__=="__main__":
    t_cases = int(input())
    for case in range(t_cases):
        n = int(input())
        for i in range(n):
            in_1 = [int(a) for a in input().split()]
            in_2 = [int(a) for a in input().split()]

            stops = in_1[1]
            planets = [0]*(len(in_2)+2)
            planets[1:-1] = in_2[:]

            res = solve(planets, stops)
            print("{}: {}".format(i+1, res))
