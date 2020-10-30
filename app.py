# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:26:08 2020

@author: abhin
"""

import streamlit as st
import pandas as pd
import pickle
import numpy as np
f=open("final_model.pkl", "rb")
model = pickle.load(f)
v= pickle.load(f)
st.write("""final project""")
st.write('---')

st.header('Specify Input Parameters')
text = st.text_input("input text")
lis=[]
for i in range(6):
    lis.append(model[i].predict_proba(v.transform([text]))[:, 1])

st.header('Output')
for i in range(6):
    st.write(lis[i])
st.write('---')



