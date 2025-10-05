import pandas as pd
import numpy as np
import os

if __name__ == "__main__":
    src_csv = "data/estrellas_gaia.csv"
    if not os.path.exists(src_csv):
        raise FileNotFoundError(f"No se encontró {src_csv}. Ejecuta primero descargar_datos.py")

    data = pd.read_csv(src_csv)

    # Distancia en parsecs a partir de la paralaje (mas)
    data["dist_pc"] = 1000.0 / data["parallax"]

    # Magnitud absoluta MG
    data["MG"] = data["phot_g_mean_mag"] - 5 * np.log10(data["dist_pc"] / 10)

    # Eliminamos valores faltantes en columnas clave
    data = data.dropna(subset=["bp_rp", "MG"])

    # Guardamos
    out_csv = "data/estrellas_limpias.csv"
    data.to_csv(out_csv, index=False)
    print(f"✅ Datos preparados y guardados en {out_csv}")
