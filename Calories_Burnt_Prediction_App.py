# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:17:23 2023

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:07:12 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('D:\Machine Learning with Python\Calories Burnt Prediction\Trained_model.sav','rb'))

#creating a function for prediction
def calories_burnt_prediction(input_data):
    #changing the input_data to numpy data
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    return prediction
def main():
    #giving the title
    st.title('Calores Burnt Predictor Web App')
    
    #getting input from user
    
    Gender = st.text_input('Gender Male->0;Female->1')
    Age = st.text_input('Age')
    Height = st.text_input('Height')
    Weight = st.text_input('Weight')
    Duration = st.text_input('Duration')
    Heart_rate = st.text_input('Heart Rate')
    Body_temp = st.text_input('Body Temperature')
    
    #code for prediction
    predicted_value = ''
    
    #getting input data from the user
    if st.button('Predicted price of Gold : '):
        predicted_value = calories_burnt_prediction([Gender,Age,Height,Weight,Duration,Heart_rate,Body_temp])
        
    st.success(predicted_value)

#Driver Code
if __name__ == '__main__':
    main()