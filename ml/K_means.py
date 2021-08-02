import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import random
import math
img = mpimg.imread('E:\\A33\\nature.png') 
data=[]
for i in range(0,len(img)):
    for j in range(0,len(img[i])):
        temp=img[i][j]
        data.append(temp)
clust=8
c=[data[random.randint(0,len(data))] for i in range(0,8)]

cluster=[[]for i in range(0,8)]
E=10
cycle=0
while(E>0.001):
    E=0
    cycle+=1
    dist=[]
    for abc in range(0,len(data)):
        temp=[]
        ind=0
        d=1000
        for i in range(0,clust):
            a=math.sqrt((c[i][0]-data[abc][0])**2+(c[i][1]-data[abc][1])**2+(c[i][2]-data[abc][2])**2)
            if(a<=d):
                d=a
                ind=i
        cluster[ind].append(data[j])
    for i in range(0,clust):
        x=[0 for k in range(0,3)]
        for h in range(0,len(cluster[i])):
            for f in range(0,3):
                x[f]=x[f]+cluster[i][h]
        for h in range(0,3):
            if(len(cluster[i])!=0):
                x[h]=x[h]/len(cluster[i])
        c[i]=x
        for z in range(0,len(c[i])):
            E=E+(c[i][z]-x[z])**2
    print(E)
    if(cycle==1):
        break
        
            
for i in range(0,8):
    print(len(cluster))
