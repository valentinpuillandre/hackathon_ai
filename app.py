import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Configuration de l'API Azure
api_endpoint = f"{os.getenv('AZURE_OPENAI_ENDPOINT')}?api-version={os.getenv('AZURE_OPENAI_API_VERSION')}"
api_key = os.getenv('AZURE_OPENAI_API_KEY')

# Fonction pour interroger le modèle GPT
def get_gpt_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    data = {
        "messages": [
            {"role": "system", "content": "Vous êtes un assistant utile."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }
    try:
        response = requests.post(api_endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Erreur lors de l'appel à l'API : {e}"

# Interface Streamlit
st.title("Application GPT sur Azure")
st.write("Entrez votre texte ci-dessous pour obtenir une réponse du modèle GPT.")

# Choix du thème
theme = st.selectbox("Choisissez le thème de couleur:", ["White", "Dark"])

# Appliquer un style simple selon le thème
if theme == "Dark":
    st.markdown(
        """
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body { background-color: white; color: black; }
        </style>
        """,
        unsafe_allow_html=True
    )

# Saisie utilisateur
user_input = st.text_area("Votre texte:", "")

# Bouton pour envoyer
if st.button("Envoyer"):
    if user_input.strip():
        response = get_gpt_response(user_input)
        st.write("Réponse du modèle GPT:")
        st.write(response)
    else:
        st.warning("Veuillez entrer un texte.")