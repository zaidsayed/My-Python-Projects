from matplotlib import pyplot as plt
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
    values= line.split(',')
    x.append(values[0])
    y.append(values[1])
for i in y:
    d[i]=d.get(i,0)+1
freq= d.values()
genre=d.keys()
#colors = {}
plt.pie(freq,labels=genre,startangle=90)
plt.title('GENRE DISTRIBUTION IN BOOKSTORE')
plt.show()
file.close()
