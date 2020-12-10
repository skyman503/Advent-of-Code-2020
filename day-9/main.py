f = open("file.txt", mode="r")
data = [x.rstrip() for x in f.readlines()]


def sum25(data, num, start):
    for i in range(start, start+25):
        for j in range(i, start+ 25):
            if i != j:
                if int(data[i]) + int(data[j]) == num:
                    return True
    return False


def ans1(data):
    for i in range(25,len(data)):
        if not sum25(data, int(data[i]), i-25):
            return data[i]


def ans2(data, err):
    for i in range(2, 50):
        for j in range(0, len(data)-i):
            curr_lst = []
            for k in range(0, i):
                curr_lst.append(int(data[j+k]))
            if sum(curr_lst) == int(err):
                return min(curr_lst)+max(curr_lst)


err = int(ans1(data))
print(err)
print(ans2(data, err))
