===================================================
BESOIN CLIENT 4 – Prédiction de la puissance nominale
===================================================

OBJECTIF :
  Prédire la puissance nominale (en kW) d'une borne de recharge à partir
  de ses caractéristiques via un modèle de régression supervisé.

  Cible : colonne 'puissance_nominale'

CONTENU DU DOSSIER :
  - IRVE_cleaned.csv              → données nettoyées
  - besoin_client_4.ipynb         → notebook expérimental
  - predict_puissance.py          → script CLI final
  - model_regression.pkl          → modèle de régression sauvegardé
  - preprocessor_regress.pkl      → pipeline de prétraitement sauvegardé
  - Readme.txt                    → ce fichier

UTILISATION DU SCRIPT FINAL :
  python predict_puissance.py \
    --implantation "Voirie" \
    --nbre_pdc 2 \
    --type_prise "T2" \
    --region "Île-de-France"

  Sortie :
    Puissance nominale prédite : 7.40 kW

PACKAGES REQUIS :
  pip install pandas scikit-learn joblib

RESPONSABLE : Personne 2
