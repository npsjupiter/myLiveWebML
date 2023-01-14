import streamlit as st

import matplotlib.pyplot as plt
import numpy as np


st.title("ML Project for my Leaernig")
st.image("th.jpg")
st.image("tm.jpg")

st.write("""Welcome to my new project on Machine learning.
            here we will learn about how to create streamlit application , 
            how to use machine learning model in streamlit for deployment. This deplpoyement will be handled by 
            Streamlit and Github""")
st.code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt""")
st.latex(r"y=m1*x1+m2*x2+....+c")
st.latex(r"y= e^y/(1+e^y)")
st.latex(r"x+y=0")

st.video("production ID_3764259.mp4")
st.video("Videos.mp4")
st.checkbox("yes")
st.button("Click")
# st.radio("Pick any of the option", ["Random Forest", "Decision Tree" , "Logistic Regression"])
st.select_slider("Pick any of the option", ["Random Forest", "Decision Tree" , "Logistic Regression"])
st.multiselect("Pick any of the option", ["Random Forest", "Decision Tree" , "Logistic Regression"])
st.slider("max_depth", 5, 10)

st.text_input("Please enter your email")
st.date_input("Please enter the dob")


st.balloons()
st.progress(10)

st.sidebar.title("My Side for selection")
st.sidebar.radio("Pick any of the option", ["Random Forest", "Decision Tree" , "Logistic Regression"])

rn=np.random.normal(1,2, size=20)
fig, ax=plt.subplots()
ax.hist(rn)
st.pyplot(fig)


import pandas as pd


df=pd.DataFrame(np.random.randn(600,2)/ [50,50]+ [37.76, -122.4], columns=["lat", "LON"])
st.map(df)

























