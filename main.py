import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mixer
import pygame
import uuid

ruta_mezclas = 0
# Obtener la ruta del archivo actual
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_const = ruta_actual
rutas = {
    "background": os.path.join(ruta_actual, "background.jpg"),
    "mezclas": os.path.join(ruta_actual, "mezclas")
}

def cargar_canciones():
    canciones = mixer.getCanciones()
    return canciones

def crear_mix():
    cancion1 = combo_cancion1.get()
    cancion2 = combo_cancion2.get()

    if cancion1 and cancion2:  # Verificar si se seleccionaron dos canciones
        boton_crear_mix.config(text="Mixing...", state="disabled", fg="white")
        ventana.update()

        mezcla = mixer.mix(cancion1, cancion2)
        rutas["mezclas"]=os.path.join(ruta_const, "mezclas")
        # Generar un nombre de archivo único para la mezcla
        nombre_archivo = str(uuid.uuid4()) + ".mp3"
        ruta_mezcla = os.path.join(rutas["mezclas"], nombre_archivo)
        mezcla.export(ruta_mezcla, format='mp3')

        rutas["mezclas"]=ruta_mezcla

        boton_crear_mix.config(text="Do mix", state="normal", fg="white")
        messagebox.showinfo("Mix creado", "Mix has been created")
    else:
        messagebox.showwarning("Alert", "Select two songs to mix")

def reproducir_mix(ruta_mix):
    pygame.mixer.music.load(rutas["mezclas"])
    pygame.mixer.music.play() 

def detener_reproduccion():
    pygame.mixer.music.pause()

ventana = tk.Tk()
ventana.attributes("-fullscreen", True)  # Establecer la ventana en pantalla completa

# Inicializar pygame
pygame.mixer.init()

# Crear la carpeta para las mezclas si no existe
if not os.path.exists(rutas["mezclas"]):
    os.makedirs(rutas["mezclas"])

# Construir la ruta de la imagen de fondo a partir de la ruta actual
ruta_imagen = rutas["background"]

# Cargar la imagen de fondo
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))

fondo = ImageTk.PhotoImage(imagen)

# Crear un widget Label para mostrar la imagen de fondo
label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Estilos de la fuente
titulo_font = ("Arial", 36, "bold")

# Crear un widget Label para el título
label_titulo = tk.Label(ventana, text="UNDERTALE MIXER", font=titulo_font, fg="purple",bg="black")
label_titulo.pack(pady=100)

# Crear las listas desplegables
combo_cancion1 = ttk.Combobox(ventana, state="readonly")
combo_cancion2 = ttk.Combobox(ventana, state="readonly")

# Obtener las canciones del archivo     mixer.py
canciones = cargar_canciones()

# Obtener las rutas de acceso a las canciones
rutas_canciones = list(canciones.keys())

# Establecer las opciones de las listas desplegables
combo_cancion1['values'] = rutas_canciones
combo_cancion2['values'] = rutas_canciones

# Posicionar las listas desplegables en la ventana
combo_cancion1.pack(pady=50)
combo_cancion2.pack(pady=10)

# Crear el botón "Crear mix"
boton_crear_mix = tk.Button(ventana, text="DO MIX", bg="green", command=crear_mix, fg="white")
boton_crear_mix.pack(pady=20)

# Crear el botón "Reproducir mix"
boton_reproducir = tk.Button(ventana, text="Play song", bg="green", command=lambda: reproducir_mix(rutas["mezclas"]), fg="white")
boton_reproducir.pack(pady=20)

# Crear el botón "Detener reproducción"
boton_detener = tk.Button(ventana, text="Stop song", bg="red", command=detener_reproduccion, fg="white")
boton_detener.pack(pady=10)

ventana.mainloop()