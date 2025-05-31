# Proyecto Final - Econometría II 

Este proyecto utiliza la API pública de YouTube para recolectar comentarios de videos y construir un dataset para análisis econométrico.

## Objetivo

El objetivo es practicar la recolección de datos reales mediante un pipeline reproducible con una API, cumpliendo con los estándares de documentación, limpieza y estructura exigidos en el curso.

## Autor

[DaveVzHr](https://github.com/DaveVzHr)

## Estructura del repositorio
```
.
EconometríaFinal_166427/
├── README.md
├── .gitignore
├── requirements.txt
├── code/
│ └── scrape_comments.py
└── data/
└── dataset.csv
```

## ¿Cómo usar este scraper?

### 1. Crear archivo `.env` en tu computadora (NO subir a GitHub)

Este archivo debe contener tu clave API de YouTube, así:

YOUTUBE_API_KEY=TU_API_KEY_AQUI


> ❗ Recuerda: este archivo se crea solo en tu compu, nunca se sube a GitHub.

---

### 2. Instalar las dependencias del proyecto

En tu terminal, dentro de la carpeta del proyecto, ejecuta:

pip install -r requirements.txt


### 3. Ejecutar el scraper

Una vez instalado todo, corre el script:

python code/scrape_comments.py

Esto empezará a recolectar comentarios desde los videos de YouTube que hayas definido.

### 4. Ver el resultado

El archivo dataset.csv se guardará automáticamente en la carpeta data/.

