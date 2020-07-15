ilosc = input("Ilość pomiarów: ")
inp2 = input("Pomiary: ")

ilosc = int(ilosc)
inp = []
inp = inp2.split(" ")
ost = 0
wm = "w"
l_basenow = 1

for i in range(ilosc):
    inp[i] = int(inp[i])
    print(str(inp[i]) + " " + str(ost))
    if wm == "w":
        if inp[i] < ost:
            print("m")
            wm = "m"
            l_basenow += 1
    else:
        if inp[i] > ost:
            print("w")
            wm = "w"
            l_basenow += 1
    ost = inp[i]

print(l_basenow)