===================================================
BESOIN CLIENT 3 – Prédiction du type d'implantation
===================================================

OBJECTIF :
  Classifier automatiquement le type d'implantation d'une borne de recharge
  (voirie, parking public, parking privé…) à partir de ses caractéristiques.

  Cible : colonne 'implantation_station'

CONTENU DU DOSSIER :
  - IRVE_cleaned.csv              → données nettoyées
  - besoin_client_3.ipynb         → notebook expérimental
  - predict_implantation.py       → script CLI final
  - model_classification.pkl      → modèle de classification sauvegardé
  - preprocessor_classif.pkl      → pipeline de prétraitement sauvegardé
  - Readme.txt                    → ce fichier

UTILISATION DU SCRIPT FINAL :
  python predict_implantation.py \
    --puissance_nominale 22.0 \
    --nbre_pdc 4 \
    --region "Bretagne" \
    --type_prise "T3"

  Sortie :
    Type d'implantation prédit : Voirie

PACKAGES REQUIS :
  pip install pandas scikit-learn joblib

RESPONSABLE : Personne 1
