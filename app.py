import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Chargement des variables d'environnement
load_dotenv()

# Configuration de l'API Azure
api_endpoint = f"{os.getenv('AZURE_OPENAI_ENDPOINT')}?api-version={os.getenv('AZURE_OPENAI_API_VERSION')}"
api_key = os.getenv('AZURE_OPENAI_API_KEY')

# Configuration de la recherche Azure
search_endpoint = os.getenv('SEARCH_ENDPOINT')
search_key = os.getenv('SEARCH_KEY')
search_index_name = os.getenv('SEARCH_INDEX_NAME')

# Initialisation du client de recherche
search_client = SearchClient(
    endpoint=search_endpoint,
    index_name=search_index_name,
    credential=AzureKeyCredential(search_key)
)

def search_documents(query, top_k=3):
    try:
        results = search_client.search(
            search_text=query,
            top=top_k,
            select=["content", "title"]
        )
        return [{"content": result["content"], "title": result["title"]} for result in results]
    except Exception as e:
        st.error(f"Erreur lors de la recherche : {e}")
        return []

# Fonction pour interroger le modèle GPT avec contexte RAG
def get_gpt_response(prompt):
    # Recherche de documents pertinents
    relevant_docs = search_documents(prompt)

    # Construction du contexte
    context = "\n".join([f"Document: {doc['title']}\n{doc['content']}" for doc in relevant_docs])

    # Préparation du message système avec le contexte
    system_message = f"""Vous êtes un assistant utile. Utilisez le contexte suivant pour répondre à la question de l'utilisateur de manière précise et pertinente.

Contexte:
{context}

Répondez en vous basant sur le contexte fourni. Si le contexte ne contient pas d'information pertinente, indiquez-le clairement."""

    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    data = {
        "messages": [
            {"role": "system", "content": system_message},
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
st.title("Code de la route GPT")
st.write("Entrez votre texte ci-dessous pour obtenir une réponse du modèle GPT.")


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