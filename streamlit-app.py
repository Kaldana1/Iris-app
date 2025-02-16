import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Charger le modèle à partir du fichier .pkl
with open('lenvo/Application_Model_Classifier_Iris.pkl', 'rb') as file:
    model = pickle.load(file)

# Définir les colonnes de l'iris dataset
species = ['setosa', 'versicolor', 'virginica']

# Interface Streamlit
st.title('Prédiction de la fleur Iris')

# Demander à l'utilisateur de saisir des informations
st.write("Entrez les caractéristiques de la fleur Iris:")

sepal_length = st.slider('Longueur du sépale (cm)', 4.0, 8.0, 5.5)
sepal_width = st.slider('Largeur du sépale (cm)', 2.0, 5.0, 3.0)
petal_length = st.slider('Longueur du pétale (cm)', 1.0, 7.0, 3.5)
petal_width = st.slider('Largeur du pétale (cm)', 0.1, 2.5, 1.0)

# Créer un tableau numpy avec les valeurs saisies
input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Faire la prédiction
if st.button('Prédire'):
    prediction = model.predict(input_features)
    st.write(f"Le modèle prédit que la fleur est : {species[prediction[0]]}")

# Ajouter un peu d'informations sur le modèle
st.sidebar.title("À propos")
st.sidebar.write("""
    Ce modèle utilise un classifieur KNN pour prédire l'espèce de la fleur Iris.
    Il a été entraîné sur le dataset Iris de la bibliothèque scikit-learn.
    Utilisez les sliders ci-dessus pour entrer les caractéristiques d'une fleur et prédire son espèce.
""")

import streamlit as st
st.title("Mon premier application ")
st.header("Experience sur mon jeu de donnée")
st.subheader(" Mon jeu de donne iris")
st.slider("Longueur du Petal",0.0,5.0)
st.slider("Largeur du Petal",0.0,5.0)
st.slider("Longueur du Metal",0.0,5.0)
st.slider("Largeur du Metal",0.0,5.0)
st.button("Cliquez ici")

