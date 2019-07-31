from matplotlib import pyplot as plt
import numpy as np
x=[]
y=[]
file=open('numberofissues.txt','r')
for line in file:
    values=[int(s) for s in line.split( )]
    x.append(values[0])
    y.append(values[1])
plt.title('TREND OF NUMBER OF BOOKs SOLD')
plt.xlabel('DAY NUMBER')
plt.ylabel('NUMBER OF BOOKS SOLD')
plt.plot(x,y,label='*')
plt.show()
file.close()

#for piechart
x=[]
y=[]
d={}
file=open('BOOKS.txt','r')
for line in file:
    values=[s for s in line.split(',')]
    x.append(values[0])
    y.append(values[1])
for i in y:
    d[i]=d.get(i,0)+1
freq= list(d.values())
genre=d.keys()
plt.pie(freq,labels=genre)
plt.title('GENRE DISTRIBUTION IN BOOKSTORE')
plt.show()
file.close()
