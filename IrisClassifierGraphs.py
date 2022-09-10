#!/usr/bin/env python3
#Carmen Chau
#IrisClassifierGraphs.py
#To display graphical representations of the data imported from the UCI Iris Flower dataset. 

import pandas as pd
import matplotlib.pyplot as plt 

#Importing the UCI dataset as a Panda Dataframe
dataSet = pd.read_csv('Iris Dataset.csv')

#Deleting column Id
condensedDataSet = dataSet.drop(columns = "Id") 

#The 150 entries of the dataset are categorized into 3 different species.
#Entries 0 - 49 are Iris Setosa
#Entries 50 - 99 are Iris Versicolor
#Entries 100 to 149 are Iris Virginica

#Scatter plot graphs for variable SepalLengthCm

#Graph for the sepal length of Iris Setosa data entries 
x1 = [i for i in range (0,50)]
y1 = [condensedDataSet.iloc[x]["SepalLengthCm"] for x in x1]
plt.scatter(x1,y1, c = "Blue")

#Graph for the sepal length of Iris Versicolor data entries 
x2 = [i for i in range (50,100)] 
y2 = [condensedDataSet.iloc[x]["SepalLengthCm"] for x in x2]
plt.scatter(x2,y2, c = "Orange")

#Graph for the sepal length of Iris Virginica data entries 
x3 = [i for i in range (100,150)] 
y3 = [condensedDataSet.iloc[x]["SepalLengthCm"] for x in x3]
plt.scatter(x3,y3, c = "Green")

#Adding title, axis labels and legend for SepalLengthCm graphs
plt.title("Sepal Length of Iris data entries in cm")
plt.xlabel("Index label") 
plt.ylabel("Sepal Length in Cm")
plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])

#display all SepalLengthCm graphs
plt.show()

#Scatter plot graphs for variable SepalWidthCm

#Graph for the sepal width of Iris Setosa data entries 
x4 = [i for i in range (0,50)] 
y4 = [condensedDataSet.iloc[x]["SepalWidthCm"] for x in x1]
plt.scatter(x4,y4, c = "Blue")

#Graph for the sepal width of Iris Versicolor data entries 
x5 = [i for i in range (50,100)] 
y5 = [condensedDataSet.iloc[x]["SepalWidthCm"] for x in x2]
plt.scatter(x5,y5, c = "Orange")

#Graph for the sepal width of Iris Virginica data entries 
x6 = [i for i in range (100,150)] 
y6 = [condensedDataSet.iloc[x]["SepalWidthCm"] for x in x3]
plt.scatter(x6,y6, c = "Green")

#Adding title, axis labels and legend for SepalWidthCm graphs
plt.title("Sepal Width of Iris data entries in cm")
plt.xlabel("Index label")
plt.ylabel("Sepal Width in cm")
plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])

#display all SepalWidthCm graphs
plt.show()

#Scatter plot graphs for variable PetalLengthCm

#Graph for the petal length of Iris Setosa data entries 
x7 = [i for i in range (0,50)] 
y7 = [condensedDataSet.iloc[x]["PetalLengthCm"] for x in x1]
plt.scatter(x7,y7, c = "Blue")

#Graph for the petal length of Iris Versicolor data entries 
x8 = [i for i in range (50,100)]
y8 = [condensedDataSet.iloc[x]["PetalLengthCm"] for x in x2]
plt.scatter(x8,y8, c = "Orange")

#Graph for the petal length of Iris Virginica data entries 
x9 = [i for i in range (100,150)]
y9 = [condensedDataSet.iloc[x]["PetalLengthCm"] for x in x3]
plt.scatter(x9,y9, c = "Green")

#Adding title, axis labels and legend for PetalLengthCm graphs
plt.title("Petal Length of Iris data entries in cm")
plt.xlabel("Index label")
plt.ylabel("Petal Length in cm")
plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])

#display all PetalLengthCm graphs
plt.show()

#Scatter plot graphs for variable PetalWidthCm

#Graph for the petal width of Iris Setosa data entries 
x10 = [i for i in range (0,50)] 
y10 = [condensedDataSet.iloc[x]["PetalWidthCm"] for x in x1]
plt.scatter(x10,y10, c = "Blue")

#Graph for the petal width of Iris Versicolor data entries 
x11 = [i for i in range (50,100)] 
y11 = [condensedDataSet.iloc[x]["PetalWidthCm"] for x in x2]
plt.scatter(x11,y11, c = "Orange")

#Graph for the petal width of Iris Virginica data entries
x12 = [i for i in range (100,150)] 
y12 = [condensedDataSet.iloc[x]["PetalWidthCm"] for x in x3]
plt.scatter(x12,y12, c = "Green")

#Adding title, axis labels and legend for PetalWidthCm graphs
plt.title("Petal Width of Iris data entries in cm")
plt.xlabel("Index label") 
plt.ylabel("Petal Width in cm")
plt.legend(["Iris Setosa", "Iris Versicolor", "Iris Virginica"])

#display all PetalWidthhCm graphs
plt.show()