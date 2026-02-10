# openai-project
Projet réalisé en Python permettant d'interroger OpenAI (Chat GPT)

## Installation

- Vérifier que Python est bien installé

```bash
py --version
```
- Installer les dépendances

```bash
pip install python-dotenv requests openai
```
- Activer le virtual environment (venv)

```bash
py -m venv venv
.\venv\Scripts\activate 
```
- Mettre une clé API dans le fichier .env

- Créer le répertoire outputs à la racine du projet

- Créer un fichier .env à la racine du projet avec comme contenu :

```bash
OPENAI_API_KEY=!!YOUR-API-KEY!!
```

## Samples

- Sample : Simple interrogation de OpenAI
- Sample 1 : Demande de traduction
- Interactive Sample : Demande de génération de code

