import pandas as pd
from sklearn.ensemble import IsolationForest
import os

if __name__ == "__main__":
    src_csv = "data/estrellas_limpias.csv"
    if not os.path.exists(src_csv):
        raise FileNotFoundError(f"No se encontró {src_csv}. Ejecuta primero preparar_datos.py")

    data = pd.read_csv(src_csv)

    X = data[["bp_rp", "MG"]]
    model = IsolationForest(contamination=0.01, random_state=42)
    model.fit(X)

    data["anomalia"] = model.predict(X)  # -1 = anómala, 1 = normal
    anomalias = data[data["anomalia"] == -1]

    out_csv = "data/posibles_galaxias.csv"
    anomalias.to_csv(out_csv, index=False)
    print(f"🔍 Se detectaron {len(anomalias)} objetos anómalos. Guardados en {out_csv}")
