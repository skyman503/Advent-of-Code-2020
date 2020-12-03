f = open("file.txt", mode="r")
data = [x.rstrip() for x in f.readlines()]


def ans1(data):
    cnt = 0
    idy = 1
    idx = 3
    while idy < len(data):
        if data[idy][idx % len(data[0])] == '#':
            cnt += 1
        idx += 3
        idy += 1
    return cnt


def ans2(data):
    idy = 1
    idx = 1
    cnt = 0
    s = 1
    while idy < len(data):
        if data[idy][idx % len(data[0])] == '#':
            cnt += 1
        idx += 1
        idy += 1
    s *= cnt
    cnt = 0
    idy = 1
    idx = 3
    while idy < len(data):
        if data[idy][idx % len(data[0])] == '#':
            cnt += 1
        idx += 3
        idy += 1
    s *= cnt
    cnt = 0
    idy = 1
    idx = 5
    while idy < len(data):
        if data[idy][idx % len(data[0])] == '#':
            cnt += 1
        idx += 5
        idy += 1
    s *= cnt
    cnt = 0
    idy = 1
    idx = 7
    while idy < len(data):
        if data[idy][idx % len(data[0])] == '#':
            cnt += 1
        idx += 7
        idy += 1
    s *= cnt
    cnt = 0
    idy = 2
    idx = 1
    while idy < len(data):
        if data[idy][idx % len(data[0])] == '#':
            cnt += 1
        idx += 1
        idy += 2
    s *= cnt

    return s


print(ans1(data))
print(ans2(data))
