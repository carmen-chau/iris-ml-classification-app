#!/usr/bin/env python3
#Carmen Chau
#IrisApp.py
#To provide a framework for the Iris ML Classification Application to be deployed as a web application

from flask import Flask, render_template, request, redirect, url_for
from sklearn.metrics import accuracy_score 
import IrisKNNCode
import numpy as np

app = Flask(__name__) #Creates a flask instance for use as a web application 

@app.route("/") #the code below will run if the webpage is at its default URL address (the address upon initial opening)
def home():
    return render_template("home.html") #the render_template functions enables the home.html page to display 

@app.route('/', methods = ["POST"])
#POST occurs when the form data on the home page (aka the page with the root url of "/") is submitted.
def irisResult():
    userSeptalLengthCm = request.form.get("sepalLength", type = float) #Lines 21 - 24 use request.form.get to retrive the form entries submitted through a POST request. Arguements passed include the variable name of the value we want to retrive, and a request to convert the string result into a float (although the HTML file accepts number type with decimals, casting it to float ensures it is of the appropriate datatype)
    userSeptalWidthCm = request.form.get("sepalWidth", type = float)
    userPetalLengthCm = request.form.get("petalLength", type = float)
    userPetalWidthCm = request.form.get("petalWidth", type = float)
    userXValueTest = [userSeptalLengthCm, userSeptalWidthCm, userPetalLengthCm, userPetalWidthCm] #Creating list userXValueTest to store all of the retrieved variable data
    userXValueTest = np.array([userXValueTest]) #Converting list userXValueTest into an array 
    testPrediction = IrisKNNCode.kNearestAlgo(IrisKNNCode.xTrainNumpy, IrisKNNCode.yTrainNumpy, IrisKNNCode.xTestNumpy, 10) #This returns the ACCURACY of the algorithm SOLEY USING THE TRAINING AND TESTING DATA. Calling on method kNearestAlgorithm from file IrisKNNCode.py. Then, passing the variables corresponding to the training and testing dataset from file IrisKNNCode, as well as the # of nearest neighbours to retrieve the list of prediction values (which is the Iris flower species names)
    predictionAccuracy = round(accuracy_score(IrisKNNCode.y_test, testPrediction),4) * 100 #The overall algorithm accuracy (from the TRAINING AND TESTING DATA) is calculated by calling on sklearn.metrics.accuracy_score (which returns a float value). This result is then rounded and converted to a percentage
    finalPrediction =  str(IrisKNNCode.kNearestAlgo(IrisKNNCode.xTrainNumpy, IrisKNNCode.yTrainNumpy, userXValueTest, 10))[2:-2] #Now, based on the Iris data inputed by the user and the pre-existing training dataset from IrisKNNCode.py, a Iris flower species can be predicted. The string is indexed from [2:-2] to remove the Jinja2 curly braces that by default, comes with the return value
    if request.method == "POST":
        if finalPrediction == "Iris-setosa":
            return render_template("userResult.html", algorithmAccuracy = predictionAccuracy, userIrisSpecies = finalPrediction, flowerPicture = "/static/IrisSetosa.jpg") #Variable algorithmAccuracy and userIrisSpecies, definied in home.html, are given values to print out on the webpage using Jinja2
        elif finalPrediction == "Iris-versicolor":
            return render_template("userResult.html", algorithmAccuracy = predictionAccuracy, userIrisSpecies = finalPrediction, flowerPicture = "/static/IrisVersicolor.jpg")
        elif finalPrediction == "Iris-virginica":
            return render_template("userResult.html", algorithmAccuracy = predictionAccuracy, userIrisSpecies = finalPrediction, flowerPicture = "/static/IrisVirginica.jpg") 

@app.route('/contact', methods=['GET', 'POST'])
def contactInfo():
    return render_template('contactPage.html')

@app.route('/aboutApplication', methods=['GET', 'POST'])
def aboutApplication():
    return render_template('aboutApp.html')

@app.route('/aboutFlower', methods=['GET', 'POST'])
def aboutIrisFlower():
    return render_template('aboutIrisFlower.html')
            
@app.route('/userRedirect', methods=['GET', 'POST'])
def userRedirect():
    return render_template('home.html')

@app.route('/thankYou', methods=['GET', 'POST'])
def thankYou():
    return render_template('thankYou.html')

if __name__ == '__main__': #The lines below help the file to run when directly invoked by the terminal 
    app.run(debug = True)
