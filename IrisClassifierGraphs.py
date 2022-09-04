#!/usr/bin/env python3
#Carmen Chau
#IrisClassifierGraphs.py
#To display a graphical representation of the raw data imported from the UCI Iris database

import pandas as pd
import matplotlib.pyplot as plt 

#Creating a Panda Dataframe by importing Iris Dataset.csv 
dataSet = pd.read_csv('Iris Dataset.csv')

#Deleting column ID
condensedDataSet = dataSet.drop(columns = "Id") 

#Getting the index range for each species (as the dataset is ordered). After observing the table when it is printed out, the entries are distributed like so:
#Entries 0 - 49 are Iris Setosa
#Entries 50 - 99 are Iris Versicolor
#Entries 100 to 149 are Iris Virginica

#GRAPH FOR SepalLengthCm

#Plotting the data: SepalLengthCM FOR IRIS SETOSA
x1 = [i for i in range (0,50)]  #covers values labelled 0-49
y1 = [condensedDataSet.iloc[x]["SepalLengthCm"] for x in x1]
plt.scatter(x1,y1, c = "Blue")

#Plotting the data: SepalLengthCM FOR IRIS VERSICOLOR
x2 = [i for i in range (50,100)] #covers values labelled 50-99
y2 = [condensedDataSet.iloc[x]["SepalLengthCm"] for x in x2]
plt.scatter(x2,y2, c = "Orange")

#Plotting the data: SepalLengthCM FOR IRIS VIRGINICA
x3 = [i for i in range (100,150)] #covers values 100-149
y3 = [condensedDataSet.iloc[x]["SepalLengthCm"] for x in x3]
plt.scatter(x3,y3, c = "Green")

plt.title("Sepal Length of Iris data entries in cm")
plt.xlabel("Index label") 
plt.ylabel("Sepal Length in Cm")
plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])

plt.show()

#GRAPH FOR SepalWidthCm

#Plotting the data: SepalWidthCm FOR IRIS SETOSA
x4 = [i for i in range (0,50)] #covers values 0-49
y4 = [condensedDataSet.iloc[x]["SepalWidthCm"] for x in x1]
plt.scatter(x4,y4, c = "Blue")

#Plotting the data: SepalWidthCm FOR IRIS VERSICOLOR
x5 = [i for i in range (50,100)] #covers values 50-99
y5 = [condensedDataSet.iloc[x]["SepalWidthCm"] for x in x2]
plt.scatter(x5,y5, c = "Orange")

#Plotting the data: SepalWidthCm FOR IRIS VIRGINICA
x6 = [i for i in range (100,150)] #covers values 100-149
y6 = [condensedDataSet.iloc[x]["SepalWidthCm"] for x in x3]
plt.scatter(x6,y6, c = "Green")

plt.title("Sepal Width of Iris data entries in cm")
plt.xlabel("Index label") #this is also known as the row # or ID 
plt.ylabel("Sepal Width in cm")
plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])

plt.show()

#GRAPH FOR PetalLengthCm

#Plotting the data: PetalLengthCm FOR IRIS SETOSA
x7 = [i for i in range (0,50)] #covers values 0-49
y7 = [condensedDataSet.iloc[x]["PetalLengthCm"] for x in x1]
plt.scatter(x7,y7, c = "Blue")

#Plotting the data: PetalLengthCm FOR IRIS VERSICOLOR
x8 = [i for i in range (50,100)] #covers values 50-99
y8 = [condensedDataSet.iloc[x]["PetalLengthCm"] for x in x2]
plt.scatter(x8,y8, c = "Orange")

#Plotting the data: PetalLengthCm FOR IRIS VIRGINICA
x9 = [i for i in range (100,150)] #covers values 100-149
y9 = [condensedDataSet.iloc[x]["PetalLengthCm"] for x in x3]
plt.scatter(x9,y9, c = "Green")

plt.title("Petal Length of Iris data entries in cm")
plt.xlabel("Index label") #this is also known as the row # or ID 
plt.ylabel("Petal Length in cm")
plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])

plt.show()

#GRAPH FOR PetalWidthCm

#Plotting the data: PetalWidthCm FOR IRIS SETOSA
x10 = [i for i in range (0,50)] #covers values 0-49
y10 = [condensedDataSet.iloc[x]["PetalWidthCm"] for x in x1]
plt.scatter(x10,y10, c = "Blue")

#Plotting the data: PetalWidthCm FOR IRIS VERSICOLOR
x11 = [i for i in range (50,100)] #covers values 50-99
y11 = [condensedDataSet.iloc[x]["PetalWidthCm"] for x in x2]
plt.scatter(x11,y11, c = "Orange")

#Plotting the data: PetalWidthCm FOR IRIS VIRGINICA
x12 = [i for i in range (100,150)] #covers values 100-149
y12 = [condensedDataSet.iloc[x]["PetalWidthCm"] for x in x3]
plt.scatter(x12,y12, c = "Green")

plt.title("Petal Width of Iris data entries in cm")
plt.xlabel("Index label") #this is also known as the row # or ID 
plt.ylabel("Petal Width in cm")
plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])

plt.show()