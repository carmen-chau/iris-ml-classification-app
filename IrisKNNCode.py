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

#Converting variable x and y into arrays 
xTrainNumpy = x_train.to_numpy() 
yTrainNumpy = y_train.to_numpy()
xTestNumpy = x_test.to_numpy() 
yTestNumpy = y_test.to_numpy()
xValidationNumpy = x_validation.to_numpy()
yValidationNumpy = y_validation.to_numpy()

#Step 6: Code an method for the euclidean distance algorithm, which is used to find the distance between 2 points. 
#Distance between points is a critical component of the KNN algorithm, as predictions are made based on test point that are closest to the location of the inputed points.

def euclideanDistanceAlgo(point1, point2):
    ''' 
    Calculates the euclidean distance between 2 points

    Parameters
    ----------
    point1 (array): An array with the coordinates of the point
    point2 (array): An array with the corrdinates of another point

    Returns
    -------
    float
        The euclidean distance between the 2 points
    '''
    distanceBeforeSquareRoot = 0
    for elements in range(len(point1)):
        distanceBeforeSquareRoot += (point1[elements] - point2[elements]) ** 2
    finalDistance = distanceBeforeSquareRoot ** 0.5
    return finalDistance

#Step 8: Coding a KNN algorithm 
def kNearestAlgo(xTrain, yTrain, xPredictionData, kNeighbours):
    '''
    Implements the K- Nearest Neighbour (KNN) Algorithm 

    Parameters
    ----------
    xTrain : Array
        The array containing only the quantative measurements of the Iris flowers
    yTrain : Array
        The array with the species label of the flowers in xTrain
    xPredictionDataTrain : Array
        The array contain unknown Iris Flower measurements
    kNeighbours : int
        The number of existing points of which the unknown measurement is compared to
    
    Returns
    -------
    str
        Returns the species name corresponding to the unknown measurements
    '''
    predictionLabels = [] #empty list to store the predicted Iris flower species
    for testElements in xPredictionData: 
        #looping through the inner arrays in xPredictionData
        #These inner arrays contain the 4 quantitative measurements for each Iris Flower definined in the xPredictionData dataset 
        distanceBetweenPoints = []
        for trainElements in xTrain:
            #Iterating through the inner quantative measurements for the Iris flowers in the training dataset
            euclideanDistance = euclideanDistanceAlgo(testElements, trainElements) 
            #The calculated distance is stored in an list called euclideanDistance
            distanceBetweenPoints.append(euclideanDistance)

        #converting distanceBetweenPoints to an array 
        distanceBetweenPoints = np.array(distanceBetweenPoints)
        #Retrieving the index of the kNeightbour number of points
        selectedKDistancesIndex = np.argsort(distanceBetweenPoints)[0:kNeighbours]
        #Utilizing the concept of Integer Array Indexing, retrieving the species for each of the selected kNeighbour points 
        labels = yTrain[selectedKDistancesIndex]
        #Determining the species that is the most frequest among selected points. This will be the species name returned as the final prediction
        modeOfLabels = st.mode(labels)
        #Appending modeOfLabels to list predictionLabels
        predictionLabels.append(modeOfLabels)

    return predictionLabels #A list of predicted Iris species labels are returned
