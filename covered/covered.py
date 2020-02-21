
# import time

def covers(h, s):

    if (h[0] - s[0])**2 + (h[1] - s[1])**2 < h[2]**2:
            return True
    return False


def solve(students, hotspots):
    n = 0
    for s in students:
        for h in hotspots:
            if covers(h, s):
                n = n+1
                break
    return n

if __name__=="__main__":
    # t1 = time.time()
    n = int(input())
    for case in range(n):
        n_sites = int(input())

        for site in range(n_sites):
            n_hotspots = int(input())

            students = []
            hotspots = []

            for i in range(n_hotspots):
                l = input().split()
                x = int(l[0])
                y = int(l[1])
                r = int(l[2])
                hotspots.append([int(x), int(y), int(r)])

            l = input().split()
            X = int(l[0])
            Y = int(l[1])

            for x in range(X):
                line = input()
                for y in range(Y):
                    if line[y] == '#':
                        students.append([x, y])

            n_covered = solve(students, hotspots)
            if n_covered == 1:
                print("Site %d: %d student gets coverage"%(site+1, n_covered))
            else:
                print("Site %d: %d students get coverage"%(site+1, n_covered))


    # t2 = time.time()
    # print("elapsed time: %f s" % (t2 - t1))
