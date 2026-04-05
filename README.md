# Seminario de Python 2026 🐍

Este repositorio contiene los ejercicios realizados para la materia **Seminario Python 2**.

La estructura del proyecto sigue la consigna de la entrega:

Los notebooks con los ejercicios se encuentran dentro de la carpeta notebooks/

Las funciones auxiliares y el código reutilizable se encuentran dentro de la carpeta src/

## Estructura del proyecto

```bash
seminario-python2/
├── notebooks/
│   └── ...
├── src/
│   └── utils.py
├── README.md
└── .gitignore
```

---

## Requisitos previos

Antes de ejecutar el proyecto, es necesario tener instalado:

* [Visual Studio Code](https://code.visualstudio.com/)
* [pyenv](https://github.com/pyenv/pyenv)
* Python **3.13.12**
* Extensión **Python** para VS Code
* Extensión **Jupyter** para VS Code

> **Nota:** Al abrir un notebook (`.ipynb`) en VS Code, normalmente el editor detecta si faltan extensiones o dependencias relacionadas con Jupyter/IPython y suele sugerir su instalación automáticamente.

---

## Clonar el repositorio

Clonar el proyecto desde GitHub:

```bash
git clone git@github.com:anafts/seminario-python2.git
cd seminario-python2
```

---

## Configurar la versión de Python con pyenv

Este proyecto utiliza **Python 3.13.12**.

Verificar las versiones instaladas:

```bash
pyenv versions
```

Si la versión no está instalada, instalarla:

```bash
pyenv install 3.13.12
```

Configurar la versión local para este proyecto:

```bash
pyenv local 3.13.12
```

Verificar la versión activa:

```bash
python --version
```

Debería mostrar:

```bash
Python 3.13.12
```

---

## Instalar dependencias necesarias

Para ejecutar los notebooks, es necesario contar con Jupyter/IPython habilitado en el entorno de Python seleccionado en VS Code.

En muchos casos, al abrir un notebook, VS Code detecta automáticamente si falta el soporte para Jupyter y sugiere la instalación.

Si fuera necesario, puede instalarse manualmente con:

```bash
pip install jupyter ipykernel
```

---

## Abrir y ejecutar el proyecto en VS Code

1. Abrir la carpeta del proyecto en VS Code.
2. Abrir un notebook dentro de la carpeta `notebooks/`.
3. Seleccionar el intérprete de Python correspondiente a la versión configurada con `pyenv`.
4. Si es necesario, seleccionar también el **kernel** asociado a ese intérprete.
5. Ejecutar las celdas del notebook normalmente.

---

## Organización del proyecto

Los ejercicios deben ejecutarse desde notebooks ubicados en la carpeta:

```bash
notebooks/
```

El código reutilizable y las funciones auxiliares deben ubicarse en:

```bash
src/
```

