
sum = 0
min = 0
max = 0
count = 0
string = ""

while string != "Done":
    try: 
         string = input("Unesi broj: ")
         num = int(string)
         sum += num
         if(min > num):
             min = num
         if(max < num):
             max = num
         count += 1
    except ValueError:
        print("Unesi broj ili \"Done\"")

print("Uneseno je", count, "brojeva")
print("Srednja vrijednost unesenih brojeva je: ",(sum/count))
print("Minimum: ", min)
print("Maximum: ", max)
