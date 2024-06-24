import numpy as np
import pickle
import streamlit as st

#Loading the saved model
loaded_model = pickle.load(open('C:/Users/Moreme/Documents/Eduvos/ITDAA/Assignments/Heart Disease Predictor', 'rb'))

#Creating a function for prediction
def heart_disease_prediction(input_data):

    #Changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #Reshaping the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
        return "The patient does not have a Heart Disease"
    else:
        return "The patient has a Heart Disease"
    
    
def main():
    
    #Giving a titile for the web page
    st.title('Heart Disease Prediction Web App')
    
    #Getting the input data from the user
    
    age = st.text_input('What is your Age?')
    
    sex = st.text_input('What is your Sex? 1-Male, 0-Female')
    
    cp = st.text_input('What is the patients Chest Pain Type? 1-Typical Angina, 2-Atypical Angina, 3-Non-anginal pain, 4-Asymptomatic')
    
    trestbps = st.text_input('What is the patients Resting Blood Pressure upon admission?')
    
    chol = st.text_input('What is the patients Cholestoral level?')
    
    fbs = st.text_input('What is the patients Fasting Blood Sugar Level?')
    
    thalach = st.text_input('What is the patients achieved Maximum Heart Rate?')
    
    
    #Code for prediction
    diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Generate Result'):
        diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, thalach])
        
    st.success(diagnosis)

    
    
    
if __name__ == '__main__':
    main()
