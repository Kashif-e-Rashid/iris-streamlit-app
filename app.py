import streamlit as st
import joblib
import numpy as np

model_data = joblib.load("iris_model.joblib")
model = model_data["model"]
target_names = model_data["target_names"]

feature_names = ["Sepal length (cm)", "Sepal width (cm)", "Petal length (cm)", "Petal width (cm)"]

st.title(" Iris Flower Classifier ")
st.write("Enter the measurements below to predict the type of Iris flower. ")

sl_values = []
sl_values.append(st.slider("Sepal length (cm)", 4.0, 8.0, 5.0))
sl_values.append(st.slider("Sepal width (cm)", 2.0, 4.5, 3.0))
sl_values.append(st.slider("Petal length (cm)", 1.0, 7.0, 4.0))
sl_values.append(st.slider("Petal width (cm)", 0.1, 2.5, 1.0))

if st.button("Predict"):
    x = np.array(sl_values).reshape(1, -1)
    prediction = model.predict(x)[0]
    st.success(f"The predicted Iris type is : **{target_names[prediction]}**")