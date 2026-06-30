# 🛒 Simulador de Carrito de Compras - Tienda de Hardware

Este proyecto es una aplicación de consola desarrollada en Python que simula el sistema de un carrito de compras para una tienda virtual enfocada en componentes de PC de alto rendimiento y setups *enthusiast-grade* (incluyendo procesadores como el Ryzen 7 9800X3D y gráficas serie RTX). 

El sistema permite a los usuarios interactuar con un catálogo, agregar productos, revisar el detalle de su compra, y ver el total a pagar con conversión dinámica de divisas.

## 🚀 Características Principales

El proyecto fue desarrollado cumpliendo estrictamente con los siguientes requerimientos técnicos:

* **Estructuras de Control y Datos:** Implementación de un menú interactivo mediante bucles `while`, manejo de errores con bloques `try/except`, e iteración de datos mediante ciclos `for`. La información en memoria se gestiona a través de listas y diccionarios anidados.
* **Modularización:** Separación estricta de responsabilidades.
  * `main.py`: Maneja exclusivamente la interfaz de usuario, los `prints` y los `inputs`.
  * `logica.py`: Contiene toda la lógica de negocio y el procesamiento de datos. No interactúa directamente con el usuario por consola.
* **Persistencia de Datos (Punto Extra):** El estado del carrito se guarda de manera local en un archivo `carrito.json` al salir del programa. Al volver a ejecutar la aplicación, el sistema lee este archivo y precarga la sesión anterior para evitar la pérdida de datos.
* **Consumo de API Pública (Punto Extra):** Integración con la librería `requests` para consultar la API gratuita de `mindicador.cl`. Esto permite obtener el valor real y actualizado del dólar, mostrando al usuario el total de su compra tanto en Pesos Chilenos (CLP) como en Dólares (USD).

## 📁 Estructura del Proyecto

```text
├── main.py          # Archivo principal de ejecución (Interfaz y Menú)
├── logica.py        # Módulo de procesamiento, estructuras y peticiones HTTP
├── carrito.json     # Archivo autogenerado para la persistencia de datos
└── README.md        # Documentación del proyecto
