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
st.sidebar.title("Menu latéral")
st.sidebar.write("Bienvenu sur iris")

agree = st.sidebar.checkbox("J'accepte les conditions")
if agree:
    st.write("Merci d'avoir accepté !")
# Ajouter un menu déroulant
option = st.sidebar.selectbox("Choisissez une option :", ["Option 1", "Option 2", "Option 3"])
st.write(f"Vous avez choisi : {option}")
from PIL import Image

# Charger une image
image = Image.open("image.jpg")  
# Afficher l'image dans la sidebar
st.sidebar.image(image, caption="Image de la sidebar", use_column_width=True)

# Ajouter un texte formaté
st.sidebar.markdown("### **Bienvenue !**")
st.sidebar.markdown("Découvrez les fonctionnalités de Streamlit 🚀")
with st.sidebar.expander("Plus d'informations"):
    st.write("Voici des informations supplémentaires...")
    st.image("info.png")  
