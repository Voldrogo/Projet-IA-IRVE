===================================================
BESOIN CLIENT 2 – Clustering selon la position
===================================================

OBJECTIF :
  Partitionner les bornes de recharge selon leur position géographique
  (latitude/longitude) via un algorithme de clustering non-supervisé.

CONTENU DU DOSSIER :
  - IRVE_cleaned.csv          → données nettoyées
  - besoin_client_2.ipynb     → notebook expérimental
  - predict_cluster.py        → script CLI final
  - model_clustering.pkl      → modèle de clustering sauvegardé
  - Readme.txt                → ce fichier

UTILISATION DU SCRIPT FINAL :
  python predict_cluster.py --lat 48.8566 --lon 2.3522

  Arguments :
    --lat   Latitude de la borne (float)
    --lon   Longitude de la borne (float)

  Sortie :
    Cluster associé : X

EXEMPLE :
  python predict_cluster.py --lat 47.2184 --lon -1.5536

PACKAGES REQUIS :
  pip install pandas scikit-learn joblib folium

RESPONSABLE : Personne 2
