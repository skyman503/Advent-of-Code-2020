data = []
for line in open('file.txt'):
    data.append(line.strip())


def hlp(x, y):
    if (x-y)%2!=0:
        return (x-y) // 2 + 1
    else:
        return 0


def ans(data):
    ids = []
    for line in data:
        fr, bk = 0, 127
        lf, rg = 0, 7
        r, c = 0, 0
        for idx, char in enumerate(line):
            if char == 'F':
                bk -= hlp(bk, fr)
                r = min([bk, fr])
            elif char == 'B':
                fr += hlp(bk, fr)
                r = max([bk, fr])
            elif char == 'L':
                rg -= hlp(rg, lf)
                c = min([rg, lf])
            else:
                lf += hlp(rg, lf)
                c = max([rg, lf])
        ids.append(r * 8 + c)
    flg = False
    for i in sorted(ids):
        if i + 1 not in ids and i in ids:
            if flg:
                print(i)
            else:
                flg = True
                print(i + 1)  # second is the total length+1



ans(data)
