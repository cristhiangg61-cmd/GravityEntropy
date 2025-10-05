# 🌌 IA para Identificar Estrellas y Descubrir Galaxias

Este proyecto es un **prototipo educativo** que demuestra cómo usar **datos reales del satélite Gaia** y técnicas básicas de **machine learning** para:

1. Descargar y limpiar datos astronómicos reales.
2. Entrenar una IA sencilla que clasifica estrellas por tipo (azul/roja como ejemplo didáctico).
3. Visualizar la estructura de la Vía Láctea (diagrama color–magnitud).
4. Detectar anomalías que podrían indicar galaxias o cúmulos nuevos.

> 🧠 Diseñado para personas con poco conocimiento técnico en programación.
> 📡 Usa datos reales de la misión **Gaia DR3** (ESA).

---

## 🧭 Requisitos

- Python **3.9+**
- Conexión a internet (para descargar los datos)

### 📦 Instalación rápida

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo usar

1) **Descargar datos de Gaia** (limita a 50k filas para ser rápido):
```bash
python src/descargar_datos.py
```

2) **Preparar/limpiar datos** (calcula magnitud absoluta y filtra nulos):
```bash
python src/preparar_datos.py
```

3) **Entrenar IA sencilla** (clasifica estrellas azul/roja con LightGBM):
```bash
python src/entrenar_modelo.py
```

4) **Visualizar la Vía Láctea** (diagrama color–magnitud):
```bash
python src/graficar_vialactea.py
```

5) **Detectar anomalías** (potenciales estructuras inusuales):
```bash
python src/detectar_anomalias.py
```

> Alternativa: abrir el notebook interactivo (recomendado para principiantes):
```bash
jupyter notebook notebooks/01_prototipo_completo.ipynb
```

---

## 📁 Estructura

```
ia-estrellas-galaxias/
├── data/                     # Archivos descargados/procesados
│   └── README.md
├── notebooks/
│   └── 01_prototipo_completo.ipynb
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

## 🛰️ Fuentes de datos

- Gaia Archive (ESA): https://gea.esac.esa.int/archive/
- SDSS SkyServer: http://skyserver.sdss.org/
- LAMOST DR9: http://dr9.lamost.org/
- DESI Legacy Surveys: https://www.legacysurvey.org/

---

## 📜 Licencia

Código bajo licencia **MIT**. Los datos científicos están sujetos a las licencias y créditos de sus respectivas misiones/consorcios.
