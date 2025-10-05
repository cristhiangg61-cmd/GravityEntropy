import pandas as pd
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    src_csv = "data/estrellas_limpias.csv"
    if not os.path.exists(src_csv):
        raise FileNotFoundError(f"No se encontró {src_csv}. Ejecuta primero preparar_datos.py")

    data = pd.read_csv(src_csv)

    plt.figure(figsize=(8, 6))
    plt.scatter(data["bp_rp"], data["MG"], s=1)
    plt.gca().invert_yaxis()  # magnitudes: más brillante = valor más pequeño (arriba)
    plt.xlabel("Color (BP - RP)")
    plt.ylabel("Magnitud Absoluta (MG)")
    plt.title("Diagrama Color-Magnitud - Vía Láctea (Gaia DR3)")
    plt.tight_layout()
    plt.show()
