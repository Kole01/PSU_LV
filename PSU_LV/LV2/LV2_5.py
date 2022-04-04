import matplotlib.pyplot as plt
import numpy as np
import skimage.io

def image(square,num_high,num_wid):
    
    img = np.zeros((square*num_wid,square*num_high))
    black_square = np.zeros((square,square))
    white_square = np.ones(square,square))
    row1=black_square
    for i in range (square):
        for j in range (square):
            white_square[i,j]+=254
    
    for i in range (num_wid):
        for j in range (num_high):
            if int(i%2)==0:
                row1=np.hstack(row1,white_square)
            else:
                row1=np.hstack(row1,black_square)


    


square = input("Zadaj dimenzije kvadrata: ")
num_high = input ("Zadaj broj kvadrata po visini: ")
num_wid = input ("Zadaj broj kvadrata po sirini")




