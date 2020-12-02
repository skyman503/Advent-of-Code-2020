f = open("plik.txt", mode='r')
data = [x.rstrip() for x in f.readlines()]


def ans1(data):
    cnt=0
    cii = 0
    for x in data:
        d = {}
        z = x
        z = z.replace("-"," ")
        z = z.replace(":", " ")
        z = z.split(" ")
        for i in z[4]:
            if i == z[2]:
                cii+=1
        if int(z[0]) <= cii <= int(z[1]):
            cnt+=1
        cii = 0
    return cnt


def ans2(data):
    cnt = 0
    cii = 0
    for x in data:
        z = x
        z = z.replace("-"," ")
        z = z.replace(":", " ")
        z = z.split(" ")
        if z[4][int(z[0])-1] == z[2]:
            cii+=1
        if z[4][int(z[1])-1] == z[2]:
            cii+=1
        if cii == 1:
            cnt+=1
        cii=0
    return cnt


print(ans1(data))
print(ans2(data))
