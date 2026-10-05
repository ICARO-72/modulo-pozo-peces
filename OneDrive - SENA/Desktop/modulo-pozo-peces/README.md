# 🐟 Módulo de Gestión de Pozos - SENA

**Evidencia:** GA7-220501096-AA3-EV01  
**Programa:** Análisis y Desarrollo de Software (ADSO)

---

## 🔗 Repositorio

[ICARO-72/modulo-pozo-peces](https://github.com/ICARO-72/modulo-pozo-peces)

## 🚀 Descripción

Aplicación web desarrollada con Python y Flask para la gestión de pozos de piscicultura. Permite registrar, visualizar y eliminar pozos desde una interfaz web.

La página principal se sirve en la ruta `/` y utiliza Flask para mostrar `templates/index.html`.

## 🛠️ Tecnologías

- Python 3
- Flask
- HTML5 y CSS3
- Git y GitHub

## ⚙️ Instalación y ejecución

Clona el repositorio, instala Flask y ejecuta el archivo principal:

```bash
git clone https://github.com/ICARO-72/modulo-pozo-peces.git
cd modulo-pozo-peces
pip install Flask
python app.py
```

Abre `http://127.0.0.1:5000/` en el navegador. Flask busca la plantilla `index.html` dentro de la carpeta `templates`.

> `debug=True` es apropiado únicamente para desarrollo. Desactívalo antes de desplegar la aplicación.
