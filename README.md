# UDD_Proyecto-M7_C10_Daniel_toro

# Predicción del Rating de Aplicaciones en Google Play Store

## Descripción

Este proyecto tiene como objetivo predecir la calificación promedio (rating) que recibirá una aplicación en Google Play Store, utilizando características como categoría, precio, tamaño, número de instalaciones y más.

El modelo ayuda a desarrolladores y empresas a anticipar la calidad percibida por los usuarios, facilitando la toma de decisiones para mejorar las aplicaciones antes de su lanzamiento o actualización.

---

## Estructura del Proyecto

- `notebooks/`  
  Contiene el notebook con análisis exploratorio, limpieza de datos, entrenamiento, ajuste y evaluación del modelo.

- `saved_models/`  
  Modelo final entrenado y guardado (`ensemble_rating_model.pkl`).

- `api/`  
  Código para exponer el modelo mediante una API REST (ejemplo con FastAPI).

- `requirements.txt`  
  Dependencias necesarias para ejecutar el proyecto y la API.

---

## Metodología

1. **Análisis Exploratorio de Datos (EDA)**  
   Se exploraron distribuciones, relaciones entre variables y se limpió la información faltante o incorrecta.

2. **Preprocesamiento**  
   Limpieza y transformación de variables, incluyendo codificación de categóricas y conversión de tipos.

3. **Modelado**  
   Entrenamiento de modelos de Machine Learning: Random Forest y XGBoost, con ajuste de hiperparámetros mediante Grid Search.

4. **Ensemble**  
   Combinación de modelos para mejorar precisión y reducir varianza.

5. **Evaluación**  
   Se usaron métricas RMSE, MAE y R² para evaluar el desempeño.

6. **Visualización**  
   Gráficos claros y personalizados para entender la distribución de los datos, importancia de variables y desempeño del modelo.

---

## Uso

### Entrenamiento y Evaluación

Ejecuta el notebook en `notebooks/` para reproducir el análisis y entrenamiento.

### API para Predicción

En la carpeta `api/` encontrarás un ejemplo de FastAPI para desplegar el modelo. 

Ejecuta:

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
