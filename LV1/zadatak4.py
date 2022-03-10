unosi = []
counter = 0
while True:
    broj = input("Zadaj Broj: ")
    try:
        if broj == "Done":
            break
        float(broj)
    except: 
        print("Niste zadali broj!")
    else: 
        unosi.append(broj)
        counter +=1
