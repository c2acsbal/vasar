f = open("vasarlas.csv", "r", encoding="utf-8")

for tartalom in f:
    tartalom = tartalom.strip().split(";")

def hanynap(tartalom):
    napszam = 0
    for i in tartalom:
       napszam += 1
    
    return napszam

napszamveg = hanynap(tartalom)

print(napszamveg)



def koltesmentes(tartalom):
    napszam = 0
    for i in tartalom:
        if int(i) == 0:
            napszam +=1
    
    return (napszam)

napszamvegkoltsegmentes = koltesmentes(tartalom)

print(napszamvegkoltsegmentes)
    

def atlag(tartalom, napszamveg):
    sum = 0
    for i in tartalom:
        i = int(i)
        sum += i
    
    atlag = sum / napszamveg

    return atlag, sum

atlagveg, sum = atlag(tartalom,napszamveg)

print(round(atlagveg,2))



def kicsnagy(tartalom):
    kicsike = 100000000000000
    for i in tartalom:
        i = int(i)
        if i != 0:
            if i < kicsike:
                kicsike = i

    nagyocska = -10000000

    for t in tartalom:
        t = int(i)
        if t > nagyocska:
            nagyocska = t


    return(kicsike, nagyocska)

kicsi, nagy = kicsnagy(tartalom)

print("Legykisebbb",kicsi, "Legynagyobb",nagy)

print(sum)

def sori(tartalom):
    ennyi = 0
    for i in len(tartalom):
        if tartalom[i] 