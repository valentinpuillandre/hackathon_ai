#### SUJET RGPD

# 🤖 Assistant RGPD avec Azure & RAG

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
** Azure Search : Base vectorielle pour la recherche
**Python** : Backend général           
   
## Configuration sur Azure 
Document Intelligence ✔️
Azure OpenAI ✔️
