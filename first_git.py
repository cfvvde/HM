str = input()
x = 0
if len(str) % 2 == 1:
    print("false")
else:
    stringg = list(str)
    for i in range(int(len(stringg)/2)):
        print(stringg[i], stringg[-i-1])
        if stringg[i] == stringg[-i-1]:
            x += 1
if x == (int(len(stringg))/2):
    print("True")
else:
    print("False")


