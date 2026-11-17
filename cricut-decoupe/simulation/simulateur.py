#!/usr/bin/env python3
"""Simulation purement hors ligne de trajectoires — n'ouvre aucun port série."""
import json


def construire_trajet(points):
    """Valide des points (x, y) fictifs en mm et produit un plan neutre."""
    if len(points) < 2:
        raise ValueError("Deux points minimum")
    commandes = []
    for i, point in enumerate(points):
        if len(point) != 2 or not all(isinstance(n, (int, float)) and not isinstance(n, bool) for n in point):
            raise ValueError("Coordonnées numériques requises")
        x, y = map(float, point)
        if not all(0 <= n <= 100 for n in (x, y)):
            raise ValueError("Hors zone fictive 0–100 mm")
        commandes.append({"operation": "aller_sans_couper" if i == 0 else "tracer_simule", "x_mm": x, "y_mm": y})
    return {"simulation": True, "connexion_usb": False, "commandes": commandes}


if __name__ == "__main__":
    exemple = [(10, 10), (40, 10), (40, 40), (10, 40), (10, 10)]
    print(json.dumps(construire_trajet(exemple), indent=2, ensure_ascii=False))
