import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from sklearn.metrics import classification_report
import os

if __name__ == "__main__":
    src_csv = "data/estrellas_limpias.csv"
    if not os.path.exists(src_csv):
        raise FileNotFoundError(f"No se encontró {src_csv}. Ejecuta primero preparar_datos.py")

    data = pd.read_csv(src_csv)

    # Etiqueta didáctica: 'Azul' si bp_rp < 0.8; si no, 'Roja'
    data["tipo"] = data["bp_rp"].apply(lambda x: "Azul" if x < 0.8 else "Roja")

    X = data[["bp_rp", "MG", "parallax", "pmra", "pmdec"]]
    y = data["tipo"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = LGBMClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("📊 Reporte de clasificación (IA sencilla azul/roja):")
    print(classification_report(y_test, y_pred))
