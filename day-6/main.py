f = open("file.txt")
dt2 = f.read().split('\n\n')
t = []
for o in dt2:
    t.append(o.split("\n"))


def ans1(data):
    s = 0
    for i in data:
        dt = {}
        cnt = 0
        for x in i:
            for l in x:
                if l not in dt.keys():
                    dt[l] = 1
                else:
                    dt[l] += 1
        s+=len(dt)
    return s


def ans2(data):
    s = 0
    for i in data:
        dt = {}
        cnt = 0
        for x in i:
            for l in x:
                if l not in dt.keys():
                    dt[l] = 1
                else:
                    dt[l] += 1
        for l in dt.keys():
            if dt[l] == len(i):
                cnt += 1
        s += cnt
    return s


print(ans1(t))
print(ans2(t))
