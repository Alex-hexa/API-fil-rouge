# Guide de lancement - API Scoring de Sinistre

## 1. Récupération du projet

Pour commencer, clonez le dépôt distant sur votre machine locale :

```bash
git clone <https://github.com/Alex-hexa/API-fil-rouge.git>
```
```bash
cd <API-fil-rouge>
```

## 2. Construction de l'image Docker

Lancez la construction de l'image avec la commande suivante :

```bash
docker build -t api-scoring-sinistre .

```

## 3. Lancement de l'API

Une fois l'image créée, lancez le conteneur en mappant le port **8000** :

```bash
docker run -d -p 8000:8000 --name scoring-service api-scoring-sinistre

```

## 4. Tests et Utilisation (REST)

### A. Accès à Swagger UI

Vous pouvez cliquer sur le lien suivant pour vous rendre sur l'interface graphique :

http://localhost:8000/docs

### B. Exemple de test via cURL

Vous pouvez également soumettre un dossier de sinistre directement depuis votre terminal pour vérifier le calcul du score :

```bash
curl -X 'POST' \
  'http://localhost:8000/score' \
  -H 'Content-Type: application/json' \
  -d '{
  "identifiant_sinistre": "SIN-001",
  "type_sinistre": "automobile",
  "montant_estime_euros": 300,
  "anciennete_contrat_mois": 36,
  "nombre_sinistres_anterieurs": 0,
  "age_assure": 45
}'
```

## 5. Arrêt du service

Pour arrêter et supprimer le conteneur proprement :

- Arrêter :
```bash
docker stop scoring-service
```
    Ctrl+C

- Supprimer

```bash
docker rm scoring-service
```
---
Réalisé par Maxime RICHARD et Alexandre MULARD