import time
#Plik - 1
plik_s = input("Ścieżka do pliku z danymi wejściowymi: ")

for u in range(len(plik_s)):   
    if chr(92) == plik_s[u]:
        plik_s = plik_s[:u] + "/" + plik_s[u + 1:]

plik = open(plik_s)
plik_l = plik.readlines()
plik.close()

ilosc = plik_l[0]
inp2 = plik_l[1]

#Plik - 2
plik_s = input("Ścieżka do pliku z danymi wyjściowymi: ")

for u in range(len(plik_s)):   
    if chr(92) == plik_s[u]:
        plik_s = plik_s[:u] + "/" + plik_s[u + 1:]

plik2 = open(plik_s)
plik2_odp = plik2.readlines()
plik2.close()
odp = plik2_odp[0]

czas1 = time.time()#Stoper - start

#Zmienne do algorytmu
ilosc = int(ilosc)
inp = []
inp = inp2.split(" ")
ost = 0
wm = "w"
l_basenow = 1

#Badanie, czy liczby są coraz większe, czy coraz mniejsze
for i in range(ilosc):
    inp[i] = int(inp[i])
    #print(str(inp[i]) + " " + str(ost))
    if wm == "w":
        if inp[i] < ost:
            #print("m")
            wm = "m"
            l_basenow += 1
    else:
        if inp[i] > ost:
            #print("w")
            wm = "w"
            l_basenow += 1
    ost = inp[i]

#Podsumowanie
czas2 = time.time()
czas3 = czas2 - czas1

if l_basenow == int(odp):
    print("Dobrze!!!")
    print("Czas: " + str(czas3))
    print("Odp: " + str(l_basenow))
else:
    print("Dobrze!!!")
    print("Czas: " + str(czas3))
    print("Odp: " + str(l_basenow))