import pandas as pd
from sklearn import model_selection, ensemble
import random

def PrepData(path):
    """
    Prepares data before its usage, only works for data with the same format as the sample csv provided

    Args:
        path: relative path to the data file in csv format

    Returns:
        Panda dataframe with some wrong numbers added in
    """

    #Gathering relevant data in  pd dataframe
    data = pd.read_csv(path,sep=";")
    data = data[["N1","N2","N3","N4","N5","E1","E2","Winner"]]

    #Changing all winning numbers to 1
    data["Winner"] = data["Winner"].apply(lambda x : 1)
    
    data = data.rename(columns={"Winner":"Y"})

    #Generating a large (Number of winning numbers * 4) number of losing numbers, and adding them to the dataframe
    for i in range(data.shape[0]*4):
        tba = pd.DataFrame([[random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,12),random.randint(1,12),0]],columns=["N1","N2","N3","N4","N5","E1","E2","Y"])
        data = data.append(tba)

    return data

def PrepDatasets(data, test_size=0.2):
    """
    Prepares training and test datasets for the model

    Args:
        data : panda dataframe to make the datasets from
        test_size : the percentage of the size the test dataset will be, 
        for example test_size=0.3 will return a test dataset containing 30% of the original data.shape
        Equals 0.2 by default

    Returns:
        X_train, Y_train : training dataset and its results
        X_test, Y_test : test dataset and its results
    """
    
    data_train, data_test = model_selection.train_test_split(data, test_size=test_size)

    X_train = data_train[["N1","N2","N3","N4","N5","E1","E2"]].values
    Y_train = data_train["Y"].values

    X_test = data_test[["N1","N2","N3","N4","N5","E1","E2"]].values
    Y_test = data_test["Y"].values

    return (X_train, Y_train, X_test, Y_test)

def UserGuess():
    """
    Makes the user specify their guess they wish to have predicted

    Args:
        None

    Returns:
        2D Array with the user's guesses in.
    """

    guess = []
    res = []
    guess.append(int(input("Enter the first number between 1 and 50 :\n")))
    guess.append(int(input("Enter the second number between 1 and 50 :\n")))
    guess.append(int(input("Enter the third number between 1 and 50 :\n")))
    guess.append(int(input("Enter the fourth number between 1 and 50 :\n")))
    guess.append(int(input("Enter the fifth number between 1 and 50 :\n")))
    guess.append(int(input("Enter the first star number between 1 and 12 :\n")))
    guess.append(int(input("Enter the second star number between 1 and 12 :\n")))
    res.append(guess)
    return res

def UserPrediction(guess, model_trained=model):
    """
    Predicts the odds of win and loss based on the user's guess and prints them

    Args:
        guess : 2D Array with the guesses
        model_trained : The model to use for the prediction, by default our own trained model

    Returns:
        Null
    """
    predicted = model_trained.predict_proba(guess)
    print("Chance of winning : ",round(predicted[0][1]*100,2),"%")
    print("Chance of losing : ",round(predicted[0][0]*100,2),"%")


data = PrepData("EuroMillions_numbers.csv")
(X_train, Y_train, X_test, Y_test) = PrepDatasets(data)

#Defining the model, we're using a random forest classifier here.
model = ensemble.RandomForestClassifier(max_depth=5, random_state=0)

#Training the model
model.fit(X_train,Y_train)