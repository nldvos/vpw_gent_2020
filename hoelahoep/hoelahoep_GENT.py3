num_boxes = 0
num_bows = 0
inhoud = []
max_length = 0
start = 0


def solve_(box, number):
    global max_length, num_boxes, num_bows, inhoud, start
    print("box " + str(box))
    if max_length == num_boxes:
        return
    for i in range(num_bows*2):
        print(inhoud[box][i])
        if inhoud[box][i][0] == number:
            if inhoud[box][i][1] == start and box > max_length:
                max_length = box
                return
            else:
                return solve_(box+1, inhoud[box][i][1])

def solve():
    global num_bows, inhoud, max_length, num_boxes, start
    for i in range(num_bows*2):
        print("bow " + str(i))
        start = inhoud[0][i][0]
        if inhoud[0][i][1] == start and max_length < 1:
            max_length = 1
            continue
        solve_(1, inhoud[0][i][1])
        if max_length == num_boxes:
            break
    return max_length + 1

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    num_bows = 0
    inhoud = []
    max_length = 0
    start = 0
    num_boxes = int(input())
    num_bows = int(input())
    inhoud = [[(0, 0) for i in range(num_bows*2)] for j in range(num_boxes)]
    for i in range(num_boxes):
        for j in range(0, num_bows):
            inp = input().split()
            inhoud[i][j*2] = (int(inp[0]), int(inp[1]))
            inhoud[i][j*2+1] = (int(inp[1]), int(inp[0]))
    print("{}".format(solve()))

