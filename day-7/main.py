import sys
sys.setrecursionlimit(1500)
dt={}
f = open("file.txt",mode='r')
data = [x.rstrip() for x in f.readlines()]

for x in data:
    tmp = {}
    color = x.split(' bags contain ')[0]
    contain = x.split(' bags contain ')[1]
    if 'no other bags' in contain:
        pass
    else:
        contain = contain.split(' ')
        m=0
        while m < len(contain):
            count = contain[m]
            contained = contain[m+1] + ' ' + contain[m+2]
            tmp[contained] = count
            m += 4
    dt[color] = tmp

ans = {}


def ans1(data, goal):
    global ans
    for x, y in data.items():
        for z,_ in y.items():
            if z == goal:
                ans[x] = 1
                ans1(data, x)


def ans2(data, goal):
    cnt =1
    for x, y in data[goal].items():
        cnt = cnt + int(y) * int(ans2(data, x))
    return cnt


ans1(dt, "shiny gold")
print(len(ans))
print(ans2(dt, "shiny gold")-1)
