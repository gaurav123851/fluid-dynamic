import streamlit as st
import pickle
import numpy as np

# Load the wrapper
@st.cache(allow_output_mutation=True)
def load_model():
    with open("\GAURAV\Users\as\iCloudPhotos\Photos\Desktop\Project\fluid_model_wrapper.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Web App Title
st.title("🌊 Fluid Dynamics Prediction Model")

# Input form
st.subheader("Enter input features:")

# Example: let's assume 3 input features. You can change the number based on your model
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)

# Predict button
if st.button("Predict"):
    input_data = [[feature1, feature2, feature3]]
    prediction = model.predict(input_data)
    st.success(f"📈 Prediction: {prediction[0]}")
