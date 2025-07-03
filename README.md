# Ai Bounce 2.0

Modelo de IA que aprende la probabilidad de que una palabra siga a un par de palabras anteriores. Ademas genera texto palabra a palabra utilizando esas probabilidades

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Docker](https://img.shields.io/badge/Docker-E4EFF9?style=for-the-badge&logo=docker&logoColor=blue)

# Limitaciones
 - No entiende el lenguaje, solo patrones de ocurrencia. (SE ARREGLARÁ EN ACTUAALIZACIONES FUTURAS)
 - Genera texto que puede ser incoherente o repetitivo, especialmente con corpus pequeño.
 - No generaliza ni razona, solo genera según frecuencias observadas.

# Uso
 - Es una introducción sencilla para entender cómo funcionan los modelos de lenguaje probabilísticos.
 - Base para modelos más complejos como n-gramas de mayor orden o modelos neuronales.
 - Puede servir para generación de texto simple, predicción básica o análisis estadístico de texto.

# Instalacion
## GitHub
 1. Clona el repositorio
    ```bash
    git clone https://github.com/DrxcoDev2/algorithms-ai-bounce2.0/
 2. Prender entorno virtual:
    ```bash
    python3 -m venv ai-bounce
 4. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
 5. Prende:
    ```bash
    python3 mode.py
## Docker (recomendado)
   1. Clona el repositorio
      ```bash
      git clone https://github.com/DrxcoDev2/algorithms-ai-bounce2.0/
   2. Construyelo:
      ```bash
      docker build -t modelai-bounce .
   3. Correlo:
      ```bash
      docker run -it --rm modelai-bounce

# Stats
| Linux  | Windows | Ios
| ------------- | ------------- | ------------- |
| 1.0.0  |  BETA  | NOT |

    
    
