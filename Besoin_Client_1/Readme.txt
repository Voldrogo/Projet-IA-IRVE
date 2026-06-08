===================================================
BESOIN CLIENT 1 – Visualisation sur carte
===================================================

OBJECTIF :
  Visualiser les bornes IRVE sur une carte interactive selon leur type
  d'implantation et créer une heatmap de densité.

CONTENU DU DOSSIER :
  - IRVE_cleaned.csv          → données nettoyées (sortie Big Data)
  - besoin_client_1.ipynb     → notebook expérimental
  - Readme.txt                → ce fichier

UTILISATION DU NOTEBOOK :
  1. Ouvrir besoin_client_1.ipynb dans VSCode ou Jupyter
  2. Vérifier que IRVE_cleaned.csv est dans ce même dossier
  3. Exécuter toutes les cellules (Kernel > Restart & Run All)

PACKAGES REQUIS :
  pip install pandas folium plotly scikit-learn

SORTIES PRODUITES :
  - carte_implantation.html   → carte interactive par type d'implantation
  - heatmap_densite.html      → carte de chaleur de densité spatiale
  - graphiques de distribution (affichés dans le notebook)

RESPONSABLE : Personne 1
