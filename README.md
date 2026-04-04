# Seminario de Python 2026 🐍

Este repositorio contiene la resolución de los ejercicios del tp2

## Estructura del Proyecto

El proyecto está organizado siguiendo los requerimientos de la entrega:

* `src/`: Contiene contiene los Jupyter Notebooks (`.ipynb`) numerados según el ejercicio, desde donde se debe ejecutar el código.
* `README.md`: Instrucciones de instalación y ejecución (este archivo).


## Instalación de Dependencias

Para poder ejecutar este proyecto, es necesario tener instalado **Python 3.13.12**. Se recomienda el uso de un entorno virtual para mantener las dependencias aisladas.

1.  **Clonar o descargar el proyecto:**
    ```bash
    git clone <url-del-repositorio>
    cd <nombre-de-la-carpeta>
    ```

2.  **Crear un entorno virtual:**
    ```bash
    python -m venv venv
    ```

3.  **Activar el entorno virtual:**
    * **Windows:** `venv\Scripts\activate`
    * **Linux/macOS:** `source venv/bin/activate`

4.  **Instalar las librerías necesarias:**
    Si existe un archivo `requirements.txt`, ejecuta:
    ```bash
    pip install -r requirements.txt
    ```
    *En caso de no tener el archivo, asegúrate de instalar `jupyter`:*
    ```bash
    pip install jupyter
    ```


preciso fazer um readme em espanhol, vou mandar as informações? primeiro, vou usar o vs code, tem que clonar o projeto no repo: git@github.com:anafts/seminario-python2.git para usar no vscode, precisa instalar a extenção do python e no jupyter notebook, insalar tbm o kernel(geralmenre ao rodar o vscode instala sozinhao, né? no meu foi assim, me corrija se eu tiver errada), depois usar o pyenv na versão 3.13.12 