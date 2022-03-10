
test = 0
while test == 0:
    broj = float(input("Zadaj broj: "))
    if broj >= 0.0 and broj <= 1.0:
        test = 1
    else: 
        test=0
if broj>= 0.9:
    print("A")
elif broj>= 0.8:
    print("B")
elif broj>= 0.7:
    print("C")
elif broj>= 0.6:
    print("D")
elif broj< 0.6:
    print("F")
