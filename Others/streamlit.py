{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7b0c59fd-f088-4472-9597-71c301e6a55f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# In Jupyter Notebook, save this as 'app.py'\n",
    "\n",
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the trained model\n",
    "with open(\"model.pkl\", \"rb\") as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "# Streamlit app\n",
    "st.title(\"Iris Flower Prediction\")\n",
    "\n",
    "st.write(\"This app predicts the species of an Iris flower based on its sepal and petal dimensions.\")\n",
    "\n",
    "# User input for features\n",
    "sepal_length = st.slider(\"Sepal Length (cm)\", 4.0, 8.0, 5.0)\n",
    "sepal_width = st.slider(\"Sepal Width (cm)\", 2.0, 4.5, 3.0)\n",
    "petal_length = st.slider(\"Petal Length (cm)\", 1.0, 7.0, 3.0)\n",
    "petal_width = st.slider(\"Petal Width (cm)\", 0.1, 2.5, 1.0)\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict\"):\n",
    "    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    species = ['Setosa', 'Versicolor', 'Virginica']\n",
    "    st.write(f\"The predicted species is: {species[prediction]}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
