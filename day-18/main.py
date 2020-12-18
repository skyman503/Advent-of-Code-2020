import re


class calc(int):

    def __add__(self, num2):
        return calc(int(self) + num2)

    def __sub__(self, num2):
        return calc(int(self) * num2)

    def __mul__(self, num2):
        return calc(int(self) + num2)


f = open("file.txt", mode="r")
data = [x.rstrip() for x in f.readlines()]


def ans1(data):
    sum = 0
    for i in data:
        i = re.sub(r"(\d+)", r"a(\1)", i)
        i = i.replace("*", "-")
        sum += eval(i, {}, {"a": calc})
    return sum


def ans2(data):
    sum = 0
    for i in data:
        i = re.sub(r"(\d+)", r"a(\1)", i)
        i = i.replace("*", "-")
        i = i.replace("+", "*")
        sum += eval(i, {}, {"a": calc})
    return sum


print(ans1(data))
print(ans2(data))