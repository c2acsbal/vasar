f = open("vasarlas.csv", "r", encoding="utf-8")

for tartalom in f:
    tartalom = tartalom.split(";")

def hanynap(tartalom):
    napszam = 0
    for i in tartalom:
       napszam += 1
    
    return napszam

napszamveg = hanynap(tartalom)

print(napszamveg)



    
