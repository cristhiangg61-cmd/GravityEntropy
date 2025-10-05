# AI to Identify Stars and Discover Galaxies

This project is an educational prototype that demonstrates how to use real data from the Gaia satellite and basic machine learning techniques to:

1. Download and clean real astronomical data.
2. Train a simple AI model to classify stars by type (blue/red as a didactic example).
3. Visualize the structure of the Milky Way (color–magnitude diagram).
4. Detect anomalies that could indicate new galaxies or stellar clusters.

Designed for people with little technical programming knowledge.
Uses real data from the Gaia DR3 mission (ESA).

---

## Requirements

* Python 3.9+
* Internet connection (to download data)

### Quick installation

```bash
pip install -r requirements.txt
```

---

## How to Use

1. Download Gaia data (limited to 50k rows for speed):

```bash
python src/descargar_datos.py
```

2. Prepare/Clean data (compute absolute magnitude and filter nulls):

```bash
python src/preparar_datos.py
```

3. Train a simple AI model (classifies blue/red stars using LightGBM):

```bash
python src/entrenar_modelo.py
```

4. Visualize the Milky Way (color–magnitude diagram):

```bash
python src/graficar_vialactea.py
```

5. Detect anomalies (potential unusual structures):

```bash
python src/detectar_anomalias.py
```

Alternatively, open the interactive notebook (recommended for beginners):

```bash
jupyter notebook notebooks/01_prototype_complete.ipynb
```

---

## Structure

```
ia-stars-galaxies/
├── data/                     # Downloaded/processed files
│   └── README.md
├── notebooks/
│   └── 01_prototype_complete.ipynb
├── src/
│   ├── descargar_datos.py
│   ├── preparar_datos.py
│   ├── entrenar_modelo.py
│   ├── graficar_vialactea.py
│   └── detectar_anomalias.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Data Sources

* Gaia Archive (ESA): [https://gea.esac.esa.int/archive/](https://gea.esac.esa.int/archive/)
* SDSS SkyServer: [http://skyserver.sdss.org/](http://skyserver.sdss.org/)
* LAMOST DR9: [http://dr9.lamost.org/](http://dr9.lamost.org/)
* DESI Legacy Surveys: [https://www.legacysurvey.org/](https://www.legacysurvey.org/)

---

## License

Code under the MIT License. Scientific data are subject to the licenses and credits of their respective missions/consortia.