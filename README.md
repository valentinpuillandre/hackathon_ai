# Assistant RGPD - Application Streamlit

Cette application est un assistant RGPD développé avec Streamlit et Azure OpenAI. Elle permet d'obtenir des réponses à vos questions concernant le RGPD (Règlement Général sur la Protection des Données).

## Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)
- Un compte Azure avec accès à Azure OpenAI

## Installation

1. Clonez le dépôt :
```bash
git clone <votre-repo>
cd <votre-repo>
```

2. Créez un environnement virtuel Python :
```bash
python3 -m venv venv
```

3. Activez l'environnement virtuel :
- Sur Linux/Mac :
```bash
source venv/bin/activate
```
- Sur Windows :
```bash
.\venv\Scripts\activate
```

4. Installez les dépendances :
```bash
pip install -r requirements.txt
```

5. Créez un fichier `.env` à la racine du projet avec les variables suivantes :
```env
AZURE_OPENAI_API_KEY=votre_clé_api
AZURE_OPENAI_ENDPOINT=votre_endpoint
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

## Utilisation

1. Assurez-vous que l'environnement virtuel est activé :
```bash
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

2. Lancez l'application :
```bash
streamlit run app.py
```

3. Ouvrez votre navigateur à l'adresse : http://localhost:8501

4. Utilisez l'interface pour :
   - Choisir un thème (clair ou sombre)
   - Poser vos questions sur le RGPD
   - Obtenir des réponses détaillées

## Fonctionnalités

- Interface utilisateur intuitive avec Streamlit
- Support des thèmes clair/sombre
- Réponses détaillées sur le RGPD
- Intégration avec Azure OpenAI pour des réponses précises

## Structure du Projet

```
.
├── app.py              # Application principale
├── requirements.txt    # Dépendances Python
├── .env               # Variables d'environnement (non versionné)
└── README.md          # Documentation
```

## Sécurité

- Les clés API et informations sensibles sont stockées dans le fichier `.env`
- Le fichier `.env` est ignoré par Git (via .gitignore)
- Ne partagez jamais votre fichier `.env`

## Dépannage

Si vous rencontrez des erreurs :
1. Vérifiez que l'environnement virtuel est activé
2. Confirmez que toutes les dépendances sont installées
3. Vérifiez que votre fichier `.env` est correctement configuré
4. Assurez-vous que vos clés Azure OpenAI sont valides

Ce projet est une application d’intelligence artificielle permettant de poser des questions sur un document RGPD de format PDF, et d’obtenir des réponses fiables en langage naturel.
Elle utilise une architecture RAG (Retrieval-Augmented Generation) combinée avec Azure OpenAI et Azure Document Intelligence.


## Architecture RAG :

1. Upload du document
2. Extraction du texte + découpage en chunks
3. Génération d’embeddings
4. Envoi des embeddings dans Azure Search
5. Recherche sémantique à partir d’une question
6. Génération de la réponse avec GPT
7. Affichage dans Streamlit

## Technologies utilisées

**Streamlit** : Interface utilisateur
**Azure Document Intelligence** : Extraction de texte depuis PDF
**Azure OpenAI** : Embeddings + génération de texte
**Azure Search** : Base vectorielle pour la recherche
**Python** : Backend général

## Configuration sur Azure
Document Intelligence ✔️
Azure OpenAI ✔️
