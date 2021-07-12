# -*- coding: utf-8 -*-
"""Credit Card Fraud Prediction


"""

#importing the dependencies
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Loading the dataset
credit_card_data = pd.read_csv("/content/creditcard.csv")

#first 5 rows of dataset
credit_card_data.head()

# distribution of fraudulent transaction
# 0-->Valid Transaction, &  ,  1--> Fraudulent Transaction
credit_card_data['Class'].value_counts()

# separating the data for analysis as it is highly unbalanced
legit = credit_card_data[credit_card_data.Class==0]
fraud = credit_card_data[credit_card_data.Class==1]

print(legit.shape,fraud.shape)



# Compare values for the two types of transactions
credit_card_data.groupby('Class').mean()

legit_sample = legit.sample(n =492 )      # as there are same number of frauds

#Concatenating the values to create a balanced data set
new_dataset = pd.concat([legit_sample,fraud],axis=0)
#new_dataset.tail()

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

# Splitting the data into features and targets
X= new_dataset.drop('Class',axis=1)
Y = new_dataset['Class']
#print(X)

#Split data into training and testing
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2, stratify=Y,random_state=2)

# Logistic Regression
model = LogisticRegression()

#training the model with training data
model.fit(X_train,Y_train)

# Evaluation of accuracy of our model based on training data
X_train_prediction = model.predict(X_train)
training_data_acc = accuracy_score(X_train_prediction,Y_train)
#print(training_data_acc)

#now testing accuracy for testing data
X_test_prediction = model.predict(X_test)
test_data_acc = accuracy_score(X_test_prediction,Y_test)

# Testing for some random values
input_data = (26,-0.529912284186556,0.873891581460326,1.34724732930113,0.145456676582257,0.414208858362661,0.10022309405219,0.711206082959649,0.1760659570625,-0.286716934699997,-0.484687683196852,0.872489590125871,0.851635859904339,-0.571745302934562,0.100974273045751,-1.51977183258512,-0.284375978261788,-0.310523584869201,-0.404247868800905,-0.823373523914155,-0.290347610865436,0.0469490671140629,0.208104855076299,-0.185548346773547,0.00103065983293288,0.0988157011025622,-0.552903603040518,-0.0732880835681738,0.0233070451077205,6.14)  # random values excluding class
#changing it to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshaping array as our model is trained in different dimensions
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


prediction = model.predict(input_data_reshaped)
#print(prediction)
if prediction[0]==0:
    print("Valid Transaction")
if prediction[0]==1:
    print("Fraud Transaction")
