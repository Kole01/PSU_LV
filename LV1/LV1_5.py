p = []
fname = input("Unesite ime datoteke: ")
try:
    fhand = open(fname)
except:
    print("Error:", fname)
    exit()
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        for i in line.split():
            try:
                p.append(float(i))
            except ValueError:
                pass
suma=sum(p)
Srednja_vrijednost=suma/len(p)
print("Srednja vrijednost: ", Srednja_vrijednost)

