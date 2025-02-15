import os
import streamlit as st

st.write(" Dossier actuel :", os.getcwd())  # Affiche le dossier où tourne Streamlit
st.write(" Fichier en cours d'exécution :", __file__)  # Affiche le chemin du script


import streamlit as st
import pickle
import numpy as np

with open("Application_Model_Classifier_Iris.pkl", "rb") as file:
    knn = pickle.load(file)
    
# Charger le modèle .pkl
@st.cache_data
def load_model():
    with open("Application_Model_Classifier_Iris.pkl", "rb") as file:
        knn = pickle.load(file)
    return knn

knn = load_model()

# Interface Streamlit
st.title("🌸 Prédiction de la Fleur d'Iris")

# Ajouter une sidebar
st.sidebar.header("📊 Paramètres d'entrée")

# Création des entrées utilisateur
sepal_length = st.sidebar.slider("Longueur du sépal", 4.0, 8.0, 5.0)
sepal_width = st.sidebar.slider("Largeur du sépal", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Longueur du pétale", 1.0, 7.0, 4.0)
petal_width = st.sidebar.slider("Largeur du pétale", 0.1, 2.5, 1.3)

# Prédiction
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(features)

# Affichage du résultat
st.subheader("Résultat de la Prédiction 🏷️")
st.write(f"**La fleur prédite est : {prediction[0]}**")



import streamlit as st
st.write("Bonjour Le monde")
st.title("Mon premier application ")
st.header("Experience sur mon jeu de donnée")
st.subheader(" Mon jeu de donne iris")
st.slider("Longueur du Petal",0.0,5.0)
st.slider("Largeur du Petal",0.0,5.0)
st.slider("Longueur du Metal",0.0,5.0)
st.slider("Largeur du Metal",0.0,5.0)
st.button("Cliquez ici")
import pickle
import numpy as np

# Charger le modèle .pkl
@st.cache_data
def load_model():
    with open("Application_Model_Classifier_Iris.pkl", "rb") as file:
        knn = pickle.load(file)
    return model

knn = load_model()

# Interface Streamlit
st.title("🌸 Prédiction de la Fleur d'Iris")

# Ajouter une sidebar
st.sidebar.header("📊 Paramètres d'entrée")

# Création des entrées utilisateur
sepal_length = st.sidebar.slider("Longueur du sépal", 4.0, 8.0, 5.0)
sepal_width = st.sidebar.slider("Largeur du sépal", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Longueur du pétale", 1.0, 7.0, 4.0)
petal_width = st.sidebar.slider("Largeur du pétale", 0.1, 2.5, 1.3)

# Prédiction
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = knn.predict(features)

# Affichage du résultat
st.subheader("Résultat de la Prédiction 🏷️")
st.write(f"**La fleur prédite est : {prediction[0]}**")
 
