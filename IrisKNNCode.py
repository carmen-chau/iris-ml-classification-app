#!/usr/bin/env python3
#Carmen Chau
#IrisKNNCode.py
#To process user quantitative input, and returns a Iris species name prediction

import pandas as pd
import numpy as np
import statistics as st 
from sklearn.model_selection import train_test_split

#Importing the UCI dataset as a Panda Dataframe
dataSet = pd.read_csv('IrisDataset.csv')

#Deleting column Id
condensedDataSet = dataSet.drop(columns = "Id") 

#Forming 2 new Panda Dataframes from parent dataSet. Defining the x and y values. x and y are Panda Dataframes stemming from parent condensedDataSet
#x is a Dataframe containing all the data from parent but the data in column "Species"
x = condensedDataSet.drop(columns = "Species")
#y is a Dataframe containing just the species name of each entry
y = condensedDataSet["Species"] 

#Step 4: Splitting the dataset into 3 smaller dataframes called training, validation and testing.
#Assigned a value to variable random_state to ensure consistent splitting of dataset values across different browsing sessions
#Creating a test dataframe with 30 entries. The train and validation dataframe combined have 120 entries.
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 30, random_state = 52) #test dataset size = 30. train + validation dataset size = 120. In total, 150 elements which is the size of the original dataset.
#Assigning train dataframe with 90 entries. Validation dataframe has 30 entries. 
x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train,train_size = 90, random_state = 52)

#Step 5: Converting the "x" and "y" values for each of the 3 datasets into arrays 
#This step is necessary for individual datapoints in the dataset to be accessed and iterated quickly. 
xTrainNumpy = x_train.to_numpy() 
yTrainNumpy = y_train.to_numpy()
xTestNumpy = x_test.to_numpy() 
yTestNumpy = y_test.to_numpy()
xValidationNumpy = x_validation.to_numpy()
yValidationNumpy = y_validation.to_numpy()

#Step 6: Code an method for the euclidean distance algorithm, which is used to find the distance between 2 points. 
#Distance between points is a critical component of the KNN algorithm, as predictions are made based on test point that are closest to the location of the inputed points.

def euclideanDistanceAlgo(point1, point2):
    distanceBeforeSquareRoot = 0
    for elements in range(len(point1)):
        distanceBeforeSquareRoot += (point1[elements] - point2[elements]) ** 2
    finalDistance = distanceBeforeSquareRoot ** 0.5
    return finalDistance

#Step 8: Coding a KNN algorithm 
def kNearestAlgo(xTrain, yTrain, xPredictionData, kNeighbours):
    predictionLabels = [] #empty list to store the predicted Iris flower species based on data in xPredictionData
    print("values of xPredictionData", xPredictionData)
    for testElements in xPredictionData: 
        #looping through the inner arrays in xPredictionData
        #These inner arrays contain the 4 quantitative measurements for each Iris Flower definined in the xPredictionData dataset 
        distanceBetweenPoints = []
        
        for trainElements in xTrain:
            #Iterating through the inner quantative measurements for the Iris flowers in the training dataset
            euclideanDistance = euclideanDistanceAlgo(testElements, trainElements) #The method euclideanDistanceAlgo takes in 4 dimensional arrays. Assuming them to be definied as points in Euclidean space, can calculate the distance between the 2. 
            distanceBetweenPoints.append(euclideanDistance) #The calculated distance is stored in an array called euclideanDistance

        distanceBetweenPoints = np.array(distanceBetweenPoints)# need to convert list distanceBetweenPoints to array for the following calls to work 
        selectedKDistancesIndex = np.argsort(distanceBetweenPoints)[0:kNeighbours]#np.argsort is a method that returns the index of the closest points in order as an array. Indexing the array at [0:kNeighbours] returns kNeighbours # of indexes
        labels = yTrain[selectedKDistancesIndex] #utilizing the concept of Integer Array Indexing, can access the Iris species of the select kNeighbours # of Iris flowers.
        modeOfLabels = st.mode(labels) #getting the label value that is the most common among those selected, which according to the KNN algorithm, is our prediction
        predictionLabels.append(modeOfLabels) #appending mdoeOfLabels to list predictionLabels

    return predictionLabels #A list of predicted Iris species labels are returned

#print(kNearestAlgo(xTrainNumpy, yTrainNumpy, xTestNumpy, 10))

'''
Learning references:

From this website (https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html):

The train_test_split() method can divide data up into the testSize and trainingSize, just depends on what arguments are passed in

Since the arguments accepted are related to train and test, must only pass in the size of THOSE respective categories. Thus, validation dataset can only be formed by splitting off the training and testing datasets.

'''
