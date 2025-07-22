# UDD_Proyecto-M7_C10_Daniel_toro

# API de Predicción de Rating de Apps

Esta API recibe datos de una app móvil con las siguientes características y devuelve una predicción del **Rating** junto con un intervalo de confianza.

---

## Características esperadas (features)

| Nombre          | Descripción                      |
|-----------------|---------------------------------|
| `Reviews`       | Número de reviews                |
| `Size`          | Tamaño de la app (MB, KB, etc.) |
| `Installs`      | Número de instalaciones         |
| `Price`         | Precio de la app                |
| `Updated_Day`   | Día de la última actualización  |
| `Updated_Month` | Mes de la última actualización  |
| `Updated_Year`  | Año de la última actualización  |

---

## Endpoint

### POST `https://datv.pythonanywhere.com/predice`

Envía un JSON con las características (excepto `Rating`) en orden y recibe la predicción del rating junto con el intervalo de confianza.

---

### Ejemplo de request

```json
{
  "features": [1000, 50, 100000, 0, 12, 5, 2024],
  "confidence": 0.95
}

