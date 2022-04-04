

import math

def total_kn(sat, satnica):
    placa=float(sat) * float(satnica)
    return placa
sat=input("Unesi radne sate: ")

satnica=input("Unesi placenost po satu: ")

placa = total_kn(sat, satnica)


print("placa je: " ,placa)


