f = open("file.txt", mode='r')
data = [x.rstrip() for x in f.readlines()]


def ans1(data):
    tmp = [[x[0], x[1:]] for x in data]
    x,y=0,0
    rotation = 0 #east
    for i in tmp:
        if i[0] == 'F':
            if rotation == 0:
                x+=int(i[1])
            elif rotation == 90:
                y+=int(i[1])
            elif rotation == 180:
                x-=int(i[1])
            elif rotation == 270:
                y-=int(i[1])
        if i[0] == 'R':
            rotation -= int(i[1])
            rotation = abs(rotation % 360)
        if i[0] == 'L':
            rotation += int(i[1])
            rotation = abs(rotation % 360)
        if i[0] == 'N':
            y+=int(i[1])
        if i[0] == 'E':
            x+=int(i[1])
        if i[0] == 'S':
            y-=int(i[1])
        if i[0] == 'W':
            x-=int(i[1])

    return abs(x) + abs(y)


def ans2(data):
    x,y = 0 , 0
    wx, wy = 10,1
    tmp = [[x[0], x[1:]] for x in data]
    for i in tmp:
        if i[0] == 'F':
            x += wx * int(i[1])
            y += wy * int(i[1])
        if i[0] == 'N':
            wy += int(i[1])
        if i[0] == 'E':
            wx += int(i[1])
        if i[0] == 'S':
            wy -= int(i[1])
        if i[0] == 'W':
            wx -= int(i[1])
        if i[0] == 'L':
            cnt = int(i[1]) / 90
            while cnt:
                wx, wy = -wy, wx
                cnt -= 1
        if i[0] == 'R':
            cnt = int(i[1]) / 90
            while cnt:
                wx, wy = wy, -wx
                cnt -= 1
    return abs(x) + abs(y)


print(ans1(data))
print(ans2(data))
