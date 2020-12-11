f = open("file.txt", mode="r")
data =[int(x.rstrip()) for x in f.readlines()]


def ans1(data):
    cnt1 = 0
    cnt3 = 0
    tmp = data
    tmp.append(0)
    tmp.append(max(data) + 3)
    tmp = sorted(tmp)
    for i in range(len(tmp)):
        if tmp[i-1] - tmp[i] == -1:
            cnt1 += 1
        if tmp[i-1] - tmp[i] == -3:
            cnt3 += 1

    return cnt1*cnt3


def ans2(data):
    dt = []
    tmp = data
    tmp = sorted(tmp)
    dt.append(1)
    for i in range(1,len(tmp)):
        dt.append(0)

    for i in range(len(dt)):
        for j in range(i):
            if tmp[i] - tmp[j] <= 3:
                dt[i] += dt[j]
    return(dt[-1])


print(ans1(data))
print(ans2(data))
