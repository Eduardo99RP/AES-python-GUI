# 🔐 Cifrador/Descifrador AES en Python (GUI)

Este proyecto es una aplicación de escritorio con interfaz gráfica construida con **Tkinter** que permite **cifrar y descifrar archivos usando el algoritmo AES** (Advanced Encryption Standard). Soporta los tres tamaños de clave: **AES-128**, **AES-192** y **AES-256**.

## 🧰 Características

- Interfaz gráfica intuitiva usando `Tkinter` y `ttk`.
- Cifrado de archivos con clave generada automáticamente.
- Selección de tamaño de clave (128, 192 o 256 bits).
- Descifrado de archivos usando clave hexadecimal.
- Almacena la extensión original del archivo cifrado.
- Copiado rápido de la clave generada.
- Compatibilidad con archivos de cualquier tipo (`.txt`, `.pdf`, `.jpg`, etc.).
- Mensajes de estado y errores amigables.
- Créditos visibles dentro de la aplicación.

## 📦 Requisitos

- Python 3.6 o superior
- Paquetes necesarios:
  ```bash
  pip install pycryptodome
