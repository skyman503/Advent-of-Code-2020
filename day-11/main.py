from copy import deepcopy
f = open("file.txt")
data = [list(l.strip()) for l in f.readlines()]


def ans1(data):
    while 1:
        tmp = deepcopy(data)
        change = False
        for i in range(len(data)):
            for j in range(len(data[0])):
                cnt = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if not (x == 0 and y == 0):
                            tmpi = i + x
                            tmpj = j + y
                            if 0 <= tmpi < len(data) and 0 <= tmpj < len(data[0]) and data[tmpi][tmpj] == '#':
                                cnt += 1
                if data[i][j] == 'L':
                    if cnt == 0:
                        tmp[i][j] = '#'
                        change = True
                elif data[i][j] == '#' and cnt >= 4:
                    tmp[i][j] = 'L'
                    change = True
        if not change:
            break
        data = deepcopy(tmp)
    ans = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                ans += 1
    return ans


def ans2(data):
    while 1:
        tmp = deepcopy(data)
        change = False
        for i in range(len(data)):
            for j in range(len(data[0])):
                cnt = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if not (x == 0 and y == 0):
                            tmpi = i + x
                            tmpj = j + y
                            while 0 <= tmpi < len(data) and 0 <= tmpj < len(data[0]) and data[tmpi][tmpj] == '.':
                                tmpi += x
                                tmpj += y
                            if 0 <= tmpi < len(data) and 0 <= tmpj < len(data[0]) and data[tmpi][tmpj] == '#':
                                cnt += 1
                if data[i][j] == 'L':
                    if cnt == 0:
                        tmp[i][j] = '#'
                        change = True
                elif data[i][j] == '#' and cnt >= 5:
                    tmp[i][j] = 'L'
                    change = True
        if not change:
            break
        data = deepcopy(tmp)
    ans = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '#':
                ans += 1
    return ans


print(ans1(data))
print(ans2(data))
