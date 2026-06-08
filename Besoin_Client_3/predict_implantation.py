"""
Script CLI – Besoin Client 3 : prédiction du type d'implantation
Usage : python predict_implantation.py --puissance_nominale 22.0 --nbre_pdc 4 --lat 48.8 --lon 2.3
"""
import argparse
import numpy as np
import joblib
import os

BASE = os.path.dirname(__file__)


def predict_implantation(puissance: float, nbre_pdc: int, lat: float, lon: float) -> str:
    model   = joblib.load(os.path.join(BASE, 'model_classification.pkl'))
    encoder = joblib.load(os.path.join(BASE, 'label_encoder_classif.pkl'))
    X = np.array([[puissance, nbre_pdc, lat, lon]])
    pred = model.predict(X)
    return encoder.inverse_transform(pred)[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prédit le type d'implantation d'une borne IRVE.")
    parser.add_argument('--puissance_nominale', type=float, required=True)
    parser.add_argument('--nbre_pdc',           type=int,   required=True)
    parser.add_argument('--lat',                type=float, required=True)
    parser.add_argument('--lon',                type=float, required=True)
    args = parser.parse_args()

    resultat = predict_implantation(args.puissance_nominale, args.nbre_pdc, args.lat, args.lon)
    print(f"Type d'implantation prédit : {resultat}")
