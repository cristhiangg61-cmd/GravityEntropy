from astroquery.gaia import Gaia
import pandas as pd

if __name__ == "__main__":
    # Consulta a Gaia DR3 (limitamos a 50,000 filas para que sea rápido y didáctico)
    query = """
    SELECT TOP 50000
      source_id, ra, dec, parallax, pmra, pmdec,
      phot_g_mean_mag, bp_rp, ruwe
    FROM gaiadr3.gaia_source
    WHERE ruwe < 1.4 AND parallax_over_error > 5
    """

    print("Lanzando consulta a Gaia...")
    job = Gaia.launch_job_async(query)
    results = job.get_results().to_pandas()

    # Guardar datos crudos
    results.to_csv("data/estrellas_gaia.csv", index=False)
    print("✅ Datos descargados y guardados en data/estrellas_gaia.csv")
