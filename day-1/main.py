p = open('input.txt', mode='r')
data = [int(x.rstrip()) for x in p.readlines()]


def ans1(data):
    for x in range(len(data)):
        for j in range(len(data)):
            if x != j:
                if (data[x] + data[j]) == 2020:
                    return data[x] * data[j]


def ans2(data):
    for x in range(len(data)):
        for j in range(len(data)):
            for i in range(len(data)):
                if x !=j:
                    if i != j:
                        if x != i:
                            if (data[x] + data[j] + data[i]) == 2020:
                                return data[x] * data[j] * data[i]


print(ans1(data))
print(ans2(data))
