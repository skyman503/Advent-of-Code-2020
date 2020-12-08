f = open("file.txt", mode='r')
data = [x.rstrip() for x in f.readlines()]
acc = 0
dt = {}


def ans1(data):
    global acc
    i = 0
    while i not in dt.keys():
        dt[i] = 1
        if data[i].split(" ")[0] == 'acc':
            acc += int(data[i].split(" ")[1])
            i += 1
        elif data[i].split(" ")[0] == 'jmp':
            dt[i] = 1
            i += int(data[i].split(" ")[1])
        elif data[i].split(" ")[0] == 'nop':
            i += 1
    return acc


def ans2(data):
    for x in range(len(data)):
        com, val = data[x].split(" ")[0], data[x].split(" ")[1]
        if com == 'acc':
            continue
        if com == 'jmp':
            com = 'nop'
        elif com == 'nop':
            com = 'jmp'
        i=0
        acc = 0
        dt = {}
        while i < len(data) and i not in dt.keys():
            dt[i] = 1
            tcom, tval = data[i].split(" ")[0], data[i].split(" ")[1]
            if x == i:
                tcom, tval = com, val
            if tcom == 'acc':
                acc += int(tval)
                i += 1
            elif tcom == 'nop':
                i += 1
            elif tcom == 'jmp':
                i += int(tval)
        if i == len(data):
            return acc


print(ans1(data))
print(ans2(data))
