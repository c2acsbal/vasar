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

    return atlag

atlagveg = atlag(tartalom,napszamveg)

print(round(atlagveg,2))



