"""
Script CLI – Besoin Client 4 : prédiction de la puissance nominale
Usage : python predict_puissance.py --implantation "Voirie" --nbre_pdc 2 --lat 47.2 --lon -1.5
"""
import argparse
import numpy as np
import joblib
import os

BASE = os.path.dirname(__file__)


def predict_puissance(implantation: str, nbre_pdc: int, lat: float, lon: float) -> float:
    model   = joblib.load(os.path.join(BASE, 'model_regression.pkl'))
    encoder = joblib.load(os.path.join(BASE, 'label_encoder_regress.pkl'))
    impl_enc = encoder.transform([implantation])[0]
    X = np.array([[nbre_pdc, lat, lon, impl_enc]])
    return float(model.predict(X)[0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prédit la puissance nominale d'une borne IRVE.")
    parser.add_argument('--implantation', type=str,   required=True, help='Type d\'implantation')
    parser.add_argument('--nbre_pdc',     type=int,   required=True, help='Nombre de points de charge')
    parser.add_argument('--lat',          type=float, required=True, help='Latitude')
    parser.add_argument('--lon',          type=float, required=True, help='Longitude')
    args = parser.parse_args()

    puissance = predict_puissance(args.implantation, args.nbre_pdc, args.lat, args.lon)
    print(f'Puissance nominale prédite : {puissance:.2f} kW')
