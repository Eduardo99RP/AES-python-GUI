"""
##################################################
Cifrador/Descifrador AES                      
##################################################
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

class AESCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrador/Descifrador AES")
        self.root.geometry("500x500")  # Aumentado para los créditos
        self.root.resizable(False, False)
        
        # Variables
        self.key_size = tk.IntVar(value=256)
        self.file_path = tk.StringVar()
        self.key = tk.StringVar()
        self.output_path = tk.StringVar()
        
        # Estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TRadiobutton', background='#f0f0f0', font=('Arial', 10))
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Pestaña de cifrado
        self.tab_encrypt = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_encrypt, text='Cifrar')
        self.create_encrypt_tab()
        
        # Pestaña de descifrado
        self.tab_decrypt = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_decrypt, text='Descifrar')
        self.create_decrypt_tab()
        
        # Barra de estado
        self.status_bar = ttk.Label(root, text='Listo', relief=tk.SUNKEN)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Créditos
        credit_frame = ttk.Frame(root)
        credit_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=3)

        ttk.Label(credit_frame, text="Creadores: Eduardo Rivera y Alejandro Macías", 
                font=('Arial', 10), foreground='black').pack(anchor='center')

    
    def create_encrypt_tab(self):
        """Crea la interfaz para la pestaña de cifrado"""
        # Frame principal
        frame = ttk.Frame(self.tab_encrypt)
        frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Selección de archivo
        ttk.Label(frame, text="Archivo a cifrar:").grid(row=0, column=0, sticky='w', pady=5)
        entry_file = ttk.Entry(frame, textvariable=self.file_path, width=40)
        entry_file.grid(row=1, column=0, padx=5)
        ttk.Button(frame, text="Examinar", command=self.browse_file).grid(row=1, column=1)
        
        # Tamaño de clave
        ttk.Label(frame, text="Tamaño de clave:").grid(row=2, column=0, sticky='w', pady=5)
        
        key_frame = ttk.Frame(frame)
        key_frame.grid(row=3, column=0, columnspan=2, sticky='w')
        
        ttk.Radiobutton(key_frame, text="AES-128", variable=self.key_size, value=128).pack(side=tk.LEFT)
        ttk.Radiobutton(key_frame, text="AES-192", variable=self.key_size, value=192).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(key_frame, text="AES-256", variable=self.key_size, value=256).pack(side=tk.LEFT)
        
        # Carpeta de salida
        ttk.Label(frame, text="Guardar cifrado en:").grid(row=4, column=0, sticky='w', pady=5)
        entry_output = ttk.Entry(frame, textvariable=self.output_path, width=40)
        entry_output.grid(row=5, column=0, padx=5)
        ttk.Button(frame, text="Examinar", command=self.browse_output).grid(row=5, column=1)
        
        # Botón de cifrado
        ttk.Button(frame, text="Cifrar Archivo", command=self.encrypt_file, 
                  style='Accent.TButton').grid(row=6, column=0, columnspan=2, pady=20)
        
        # Clave generada
        ttk.Label(frame, text="Clave generada:").grid(row=7, column=0, sticky='w', pady=5)
        entry_key = ttk.Entry(frame, textvariable=self.key, width=50, state='readonly')
        entry_key.grid(row=8, column=0, columnspan=2, sticky='w', padx=5)
        
        # Botón para copiar clave
        ttk.Button(frame, text="Copiar Clave", command=self.copy_key).grid(row=9, column=0, columnspan=2, pady=5)
    
    def create_decrypt_tab(self):
        """Crea la interfaz para la pestaña de descifrado"""
        # Frame principal
        frame = ttk.Frame(self.tab_decrypt)
        frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Selección de archivo
        ttk.Label(frame, text="Archivo a descifrar:").grid(row=0, column=0, sticky='w', pady=5)
        entry_file = ttk.Entry(frame, textvariable=self.file_path, width=40)
        entry_file.grid(row=1, column=0, padx=5)
        ttk.Button(frame, text="Examinar", command=self.browse_encrypted_file).grid(row=1, column=1)
        
        # Clave
        ttk.Label(frame, text="Clave (hexadecimal):").grid(row=2, column=0, sticky='w', pady=5)
        entry_key = ttk.Entry(frame, textvariable=self.key, width=50)
        entry_key.grid(row=3, column=0, columnspan=2, sticky='w', padx=5)
        
        # Carpeta de salida
        ttk.Label(frame, text="Guardar descifrado en:").grid(row=4, column=0, sticky='w', pady=5)
        entry_output = ttk.Entry(frame, textvariable=self.output_path, width=40)
        entry_output.grid(row=5, column=0, padx=5)
        ttk.Button(frame, text="Examinar", command=self.browse_output).grid(row=5, column=1)
        
        # Botón de descifrado
        ttk.Button(frame, text="Descifrar Archivo", command=self.decrypt_file, 
                  style='Accent.TButton').grid(row=6, column=0, columnspan=2, pady=20)
    
    def browse_file(self):
        """Abre diálogo para seleccionar archivo a cifrar"""
        file_path = filedialog.askopenfilename(title="Seleccionar archivo a cifrar")
        if file_path:
            self.file_path.set(file_path)
            self.output_path.set(file_path + '.enc')
            self.status_bar.config(text=f"Archivo seleccionado: {os.path.basename(file_path)}")
    
    def browse_encrypted_file(self):
        """Abre diálogo para seleccionar archivo cifrado"""
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo cifrado",
            filetypes=[("Archivos cifrados", "*.enc"), ("Todos los archivos", "*.*")]
        )
        if file_path:
            self.file_path.set(file_path)
            base_name = os.path.splitext(file_path)[0]
            self.output_path.set(base_name + '_decrypted')
            self.status_bar.config(text=f"Archivo cifrado seleccionado: {os.path.basename(file_path)}")
    
    def browse_output(self):
        """Abre diálogo para seleccionar ubicación de salida"""
        if self.notebook.index(self.notebook.select()) == 0:  # Pestaña de cifrado
            output_path = filedialog.asksaveasfilename(
                title="Guardar archivo cifrado como",
                defaultextension=".enc",
                filetypes=[("Archivos cifrados", "*.enc")]
            )
        else:  # Pestaña de descifrado
            output_path = filedialog.asksaveasfilename(
                title="Guardar archivo descifrado como"
            )
        
        if output_path:
            self.output_path.set(output_path)
            self.status_bar.config(text=f"Ubicación de salida: {os.path.basename(output_path)}")
    
    def encrypt_file(self):
        """Cifra el archivo seleccionado"""
        if not self.file_path.get():
            messagebox.showerror("Error", "Seleccione un archivo para cifrar")
            return
        
        try:
            # Generar clave
            key = get_random_bytes(self.key_size.get() // 8)
            self.key.set(key.hex())
            
            # Cifrar archivo
            cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
            
            with open(self.file_path.get(), 'rb') as f_in:
                file_data = f_in.read()
            
            padded_data = pad(file_data, AES.block_size)
            encrypted_data = cipher.encrypt(padded_data)
            
            # Guardar archivo cifrado (incluyendo IV y extensión original)
            with open(self.output_path.get(), 'wb') as f_out:
                file_extension = os.path.splitext(self.file_path.get())[1]
                f_out.write(len(file_extension).to_bytes(1, 'big'))  # Longitud de extensión
                f_out.write(file_extension.encode())                  # Extensión original
                f_out.write(cipher.iv)                                # Vector de inicialización
                f_out.write(encrypted_data)                           # Datos cifrados
            
            messagebox.showinfo(
                "Éxito",
                f"Archivo cifrado correctamente con AES-{self.key_size.get()}\n"
                f"Guardado en: {self.output_path.get()}\n\n"
                "¡NO OLVIDE GUARDAR LA CLAVE PARA DESCIFRAR!"
            )
            self.status_bar.config(text=f"Archivo cifrado: {os.path.basename(self.output_path.get())}")
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cifrar el archivo:\n{str(e)}")
            self.status_bar.config(text="Error al cifrar")
    
    def decrypt_file(self):
        """Descifra el archivo seleccionado"""
        if not self.file_path.get() or not self.key.get():
            messagebox.showerror("Error", "Seleccione un archivo e ingrese la clave")
            return
        
        try:
            # Convertir clave hexadecimal a bytes
            key = bytes.fromhex(self.key.get())
            
            # Leer archivo cifrado
            with open(self.file_path.get(), 'rb') as f_in:
                ext_len = int.from_bytes(f_in.read(1), 'big')  # Longitud de extensión
                file_extension = f_in.read(ext_len).decode()   # Extensión original
                iv = f_in.read(16)                             # Vector de inicialización
                encrypted_data = f_in.read()                   # Datos cifrados
            
            # Descifrar
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
            
            # Determinar nombre de archivo de salida
            output_path = self.output_path.get()
            if not output_path.endswith(file_extension):
                output_path += file_extension
            
            # Guardar archivo descifrado
            with open(output_path, 'wb') as f_out:
                f_out.write(decrypted_data)
            
            messagebox.showinfo(
                "Éxito",
                f"Archivo descifrado correctamente\n"
                f"Guardado en: {output_path}"
            )
            self.status_bar.config(text=f"Archivo descifrado: {os.path.basename(output_path)}")
        
        except ValueError:
            messagebox.showerror("Error", "Clave inválida. Debe ser una cadena hexadecimal")
            self.status_bar.config(text="Clave inválida")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo descifrar el archivo:\n{str(e)}")
            self.status_bar.config(text="Error al descifrar")
    
    def copy_key(self):
        """Copia la clave al portapapeles"""
        if self.key.get():
            self.root.clipboard_clear()
            self.root.clipboard_append(self.key.get())
            self.status_bar.config(text="Clave copiada al portapapeles")
        else:
            self.status_bar.config(text="No hay clave para copiar")

if __name__ == "__main__":
    root = tk.Tk()
    try:
        icono = PhotoImage(file="key.png")
        root.tk.call('wm', 'iconphoto', root._w, icono)
    except:
        print("No se pudo cargar el icono PNG")
    app = AESCipherGUI(root)
    root.mainloop()