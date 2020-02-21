
def solve(existing_cases, case):
    for c in existing_cases:
        solved = True

        # print(c)
        # print(case + c)
        for character in case + c:
            if character == ' ':
                continue
            # print(character, c.count(character), case.count(character))
            if case.count(character) != c.count(character):
                solved = False
                break
        if solved:
            return "Yes", c

    return "No", "No matching case"

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    existing_cases = []
    new_cases = []

    p_exist = int(input())
    for j in range(p_exist):
        existing_cases.append(input())
    existing_cases.sort()

    p_new = int(input())
    for j in range(p_new):
        new_case = input()
        ok, anagram = solve(existing_cases, new_case)
        print("{}: {}".format(ok, anagram))
    # check out .format's specification for more formatting options

