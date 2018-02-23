# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:00:38 2018

@author: Tushar
"""
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def eightconn(data,i,j,t,x):
    agent = x
    c = 0
    for a in range(-1,2):
        for b in range(-1,2):
            if ((i+a)>0 and (j+b)<50 and (i+a)<50 and (j+b)>0 
                and data[i+a][j+b] != data[i][j] and data[i+a][j+b] == agent):
                c +=1
    if c>= t:
        return True
    else:
        return False
    
def printmap():
    # create discrete colormap
    cmap = colors.ListedColormap(['white', 'blue', 'red'])
    bounds = [0,1,2,3]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)
    plt.show()
        
t = 3
d = np.array([0] * 1500 + [1] * 500 + [2] * 500)
np.random.shuffle(d)
data = np.reshape(d,(50,50))
printmap()
for h in range(61):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] != 0 and eightconn(data,i,j,t,data[i][j]) == False:
                for k in range(1,len(data)):
                    for l in range(-k,k+1):
                        if ((i+k)<=49 and (j+l)<=49 and (j+l)>=0 and data[i+k][j+l] == 0):
                            if eightconn(data,i+k,j+l,t,data[i][j]):
                                data[i+k][j+l] = data[i][j]
                                data[i][j] = 0
                                break
                        if ((i-k)>=0 and (j+l)<=49 and (j+l)>=0 and data[i-k][j+l] == 0):
                            if eightconn(data,i-k,j+l,t,data[i][j]):
                                data[i-k][j+l] = data[i][j]
                                data[i][j] = 0
                                break
                        if ((j+k)<=49 and (i+l)<=49 and (i+l)>=0 and data[i+l][j+k] == 0):
                            if eightconn(data,i+l,j+k,t,data[i][j]):
                                data[i+l][j+k] = data[i][j]
                                data[i][j] = 0
                                break
                        if ((j-k)<=0 and (i+l)<=49 and (i+l)>=0 and data[i+l][j-k] == 0):
                            if eightconn(data,i+l,j-k,t,data[i][j]):
                                data[i+l][j-k] = data[i][j]
                                data[i][j] = 0
                                break
                    else:
                        continue
                    break
    if h%15 == 0:
        printmap()