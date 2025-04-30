# 🔐 Cifrador/Descifrador AES en Python (GUI)

Este proyecto es una aplicación de escritorio con interfaz gráfica construida con **Tkinter** que permite **cifrar y descifrar archivos usando el algoritmo AES** (Advanced Encryption Standard). Soporta los tres tamaños de clave: **AES-128**, **AES-192** y **AES-256**.

##  Características

- Interfaz gráfica intuitiva usando `Tkinter` y `ttk`.
- Cifrado de archivos con clave generada automáticamente.
- Selección de tamaño de clave (128, 192 o 256 bits).
- Descifrado de archivos usando clave hexadecimal.
- Almacena la extensión original del archivo cifrado.
- Copiado rápido de la clave generada.
- Compatibilidad con archivos de cualquier tipo (`.txt`, `.pdf`, `.jpg`, etc.).
- Mensajes de estado y errores amigables.
- Créditos visibles dentro de la aplicación.

##  Requisitos

- Python 3.6 o superior
- Paquetes necesarios:
  ```bash
  pip install pycryptodome 
  ```

## Uso
#### 1. Clona este repositorio:
```bash
git clone https://github.com/Eduardo99RP/AES-python-GUI.git
cd AES-python-GUI
```
#### 2. Ejecuta la aplicación:
```bash 
python3 AES_Int.py
```
#### 3. Para cifrar un archivo:
- Selecciona el archivo a cifrar.
- Elige el tamaño de la clave.
- Selecciona la carpeta o nombre del archivo de salida.
- Presiona Cifrar Archivo.
- Guarda la clave generada en un lugar seguro (necesaria para descifrar).

#### 4. Para descifrar un archivo:

- Selecciona el archivo .enc.
- Ingresa la clave usada durante el cifrado (en formato hexadecimal).
- Selecciona la carpeta o archivo de salida.
- Presiona Descifrar Archivo

### ⚠️ ¡No pierdas la clave generada al cifrar, ya que no hay forma de recuperarla!
