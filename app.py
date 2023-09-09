# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:38:19 2023

@author: AnS
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the model
loaded_model=pickle.load(open('House_model.sav','rb'))

#sidebar to navigate
with st.sidebar:
    selected = option_menu ('Prodigy Infotech ML Internship',
                            ['House Price Prediction'
                             #,'abc'
                             ],
                            icons = ['house-fill',#'abc'
                                     ], #google bootstrap icons and copy the name of the one which you want
                            default_index=0)

#house pred page
if(selected == 'House Price Prediction'):
    #page title
    st.title('House Price Prediction')
    
    #user input
    bedrooms=st.number_input("Enter the number of bedrooms:")
    bathrooms=st.number_input("Enter the number of bathrooms:")
    sqlivarea=st.number_input("Enter the living area in square feet:")
    sqlot=st.number_input("Enter the Lot size in square feet:")
    
    #code for prediction
    result=''
    
    #creating a button
    if st.button("Predict the Prize"):
        result=loaded_model.predict([[bedrooms,bathrooms,sqlivarea,sqlot]])
    
    st.success(result)
    
#if (selected == 'abc'):
    #st.title('abc')

