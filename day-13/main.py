from sympy.ntheory.modular import crt

f = open("file.txt", mode='r')
data = [x.rstrip() for x in f.readlines()]


def ans1(data):
    time = int(data[0])
    bus = data[1].split(",")
    i = time
    tmp = [int(x) for x in bus if x!='x']
    while i:
        cnt=0
        for x in tmp:
            if i%x==0:
                return (i-time)*x
        i+=1


def ans2(data):
    a=[]
    b=[]
    bus = data[1].split(',')
    for i, n in enumerate(bus):
        if n == 'x':
            continue
        n = int(n)
        a.append(n)
        b.append(n-i)
    return crt(a, b)[0]


print(ans1(data))
print(ans2(data))
