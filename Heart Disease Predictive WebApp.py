# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:53:51 2024

@author: Moreme
"""

import numpy as np
import pickle
import streamlit

"Loading the saved model"
loaded_model = pickle.load(open('C:/Users/Moreme/Documents/Eduvos/ITDAA/Assignments/Heart Disease Predictor', 'rb'))