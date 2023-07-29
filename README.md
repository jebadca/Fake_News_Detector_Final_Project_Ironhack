# Fake News Detector - Final Project by JB @ Ironhack

## Executive Summary
The goal of this project is to classify news as either likely true or likely fake based on a dataset of over 60,000 news articles, approximately half of which are true and half of which are fake. The articles used in the training data have been labeled as true / fake by the organization PolitiFact and come from different news sources. We have run 6 different models, the winner of which is a Recurrent Neural Network with an Long Short-Term Memory architecture. Finally, we have deployed the model for user application using Streamlit. 

See slides presentation at document "Ironhack - Data Analysis - Final Project - JB.pdf" above. 

See SQL queries at "SQL_queries_Fake_News_Detector_JB.sql". 

## Data 

### Sources

Kaggle Dataset: https://www.kaggle.com/datasets/jainpooja/fake-news-detection

IEEE Dataset: https://ieee-dataport.org/open-access/fnid-fake-news-inference-dataset

### EDA

See Tableu Dashboard here: https://public.tableau.com/app/profile/jes.s.badenes/viz/FinalProjectIronhack-FakeNewsDetectorStory/FakeNewsDetector?publish=yes

### Models

See Jupyter Notebook file above, called "Final_Project_Code_Jesus_Badenes".

We ran the following models:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine
- Feedforward Neural Network
- Recurrent Neural Network

### App

See .py file above, called "App.py"

### Results

All models had an accuracy of 80%+. We chose to deploy the RNN LSTM neural net due to its accuracy and ability to deliver a numerical probability of "fakeness" in the user application. Some key limitations were generalization and overfitting - most of the news articles in the training set were from 2015 - 2016, and all of them were US - based. Future development should include adding more divserse news articles, across time, geographies and languages.

