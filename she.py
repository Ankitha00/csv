import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('myfile.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y)
plt.show()

