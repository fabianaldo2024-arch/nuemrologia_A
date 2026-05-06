import tkinter as tk
import pygame
import os
from tkinter import messagebox, ttk
from datetime import datetime
import struct
import array

# --------------------------------------------------
# Inicializar pygame (sonido) una sola vez
# --------------------------------------------------
pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)

# --------------------------------------------------
# Función para generar un sonido de clic (buffer de audio PCM)
# --------------------------------------------------
def generar_click():
    """Genera un sonido corto de clic como objeto pygame.mixer.Sound."""
    # Parámetros del sonido: frecuencia 1000 Hz, 0.05 segundos, muestreo 22050 Hz
    frecuencia_tono = 1000
    duracion_seg = 0.05
    muestreo = 22050
    num_muestras = int(muestreo * duracion_seg)
    
    # Generar onda sinusoidal atenuada
    muestras = []
    for i in range(num_muestras):
        t = float(i) / muestreo
        # Envolvente de fade out lineal
        envolvente = 1.0 - (i / num_muestras)
        valor = int(32767 * envolvente * __import__('math').sin(2 * __import__('math').pi * frecuencia_tono * t))
        muestras.append(valor)
    
    # Convertir a array de enteros de 16 bits (little-endian)
    arr = array.array('h', muestras)  # 'h' = signed short
    try:
        return pygame.mixer.Sound(buffer=arr.tobytes())
    except Exception as e:
        print(f"No se pudo generar el sonido: {e}")
        return None

# Crear el sonido de clic una sola vez (global)
sound_click = generar_click()

def reproducir_click():
    """Reproduce el clic si está disponible."""
    if sound_click:
        sound_click.play()

# --------------------------------------------------
# LÓGICA DE NUMEROLOGÍA (sin cambios)
# --------------------------------------------------
def reducir_a_digito(n: int) -> int:
    while n >= 10:
        suma = sum(int(d) for d in str(n))
        n = suma
    return n

def calcular_numero_mision(dia: int, mes: int, anio: int) -> int:
    fecha_str = f"{dia}{mes}{anio}"
    suma_total = sum(int(c) for c in fecha_str)
    return reducir_a_digito(suma_total)

SIGNIFICADOS = {
    1: "🌟 INICIADOR: Liderazgo, independencia, creatividad. Viniste a abrir caminos.",
    2: "🕊️ PACIFICADOR: Cooperación, diplomacia, equilibrio. Construyes puentes y armonía.",
    3: "🎨 COMUNICADOR: Creatividad, expresión, alegría. Iluminas con tu arte y optimismo.",
    4: "🏛️ CONSTRUCTOR: Estructura, orden, perseverancia. Construyes bases sólidas.",
    5: "🦋 EXPLORADOR: Libertad, aventura, transformación. Abrazas el cambio con sabiduría.",
    6: "❤️ SANADOR: Amor incondicional, servicio, responsabilidad. Nutres y proteges.",
    7: "🔍 SABIO: Introspección, conocimiento, espiritualidad. Buscas la verdad profunda.",
    8: "⚡ MANIFESTADOR: Abundancia, poder, logros. Materializas sueños con integridad.",
    9: "🌍 HUMANITARIO: Compasión universal, sabiduría, culminación. Sirves a la humanidad."
}

# --------------------------------------------------
# INTERFAZ GRÁFICA
# --------------------------------------------------
class AppNumerologia:
    def __init__(self, root):
        self.root = root
        self.root.title("Numerología Pitagórica - Tu Número de Misión")
        self.root.geometry("650x750")
        self.root.configure(bg="#f2efe9")

        # Estilos
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Pastel.TLabel", background="#f2efe9", foreground="#5a4d3e", font=("Segoe UI", 10))
        style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"), background="#f2efe9", foreground="#7b6b5a")
        style.configure("Logo.TLabel", font=("Georgia", 12, "italic"), background="#f2efe9", foreground="#9b8a75")

        # Logo y slogan
        self.logo_frame = tk.Frame(root, bg="#f2efe9")
        self.logo_frame.pack(pady=20)
        self.logo_text = tk.Label(self.logo_frame, text="TechSilver", font=("Segoe UI", 20, "bold"),
                                  fg="#b0a085", bg="#f2efe9")
        self.logo_text.pack()
        self.slogan = tk.Label(self.logo_frame, text="Independencia Tecnológica",
                               font=("Segoe UI", 10, "italic"), fg="#b8ab91", bg="#f2efe9")
        self.slogan.pack()

        # Separador
        tk.Frame(root, height=2, bg="#d9cdb0", relief="flat").pack(fill="x", padx=30, pady=10)

        # Título
        titulo = tk.Label(root, text="🔮 Tu Número de Misión según la Numerología Pitagórica",
                          font=("Segoe UI", 14, "bold"), bg="#f2efe9", fg="#6b5c4a")
        titulo.pack(pady=10)

        # Marco de entrada de fecha
        frame_fecha = tk.Frame(root, bg="#fdfbf7", relief="groove", bd=2,
                               highlightbackground="#e2d6c0", highlightthickness=1)
        frame_fecha.pack(pady=20, padx=40, fill="x")

        tk.Label(frame_fecha, text="📅 Fecha de nacimiento", font=("Segoe UI", 12),
                 bg="#fdfbf7", fg="#8b7a64").grid(row=0, column=0, columnspan=3, pady=10)

        tk.Label(frame_fecha, text="Día", bg="#fdfbf7", fg="#9b8a75").grid(row=1, column=0, padx=10, pady=5)
        self.dia = tk.Spinbox(frame_fecha, from_=1, to=31, width=5, font=("Segoe UI", 12),
                              bg="#ffffff", relief="flat", highlightbackground="#d9cdb0")
        self.dia.grid(row=2, column=0, padx=10, pady=5)

        tk.Label(frame_fecha, text="Mes", bg="#fdfbf7", fg="#9b8a75").grid(row=1, column=1, padx=10)
        self.mes = tk.Spinbox(frame_fecha, from_=1, to=12, width=5, font=("Segoe UI", 12),
                              bg="#ffffff", relief="flat")
        self.mes.grid(row=2, column=1, padx=10)

        tk.Label(frame_fecha, text="Año", bg="#fdfbf7", fg="#9b8a75").grid(row=1, column=2, padx=10)
        self.anio = tk.Spinbox(frame_fecha, from_=1900, to=datetime.now().year, width=7,
                               font=("Segoe UI", 12), bg="#ffffff", relief="flat")
        self.anio.grid(row=2, column=2, padx=10)

        # Botón calcular (con sonido)
        self.btn_calcular = tk.Button(root, text="✨ Calcular mi número ✨", command=self.calcular_con_sonido,
                                      bg="#cbd9b9", fg="#3e4d2e", font=("Segoe UI", 12, "bold"),
                                      relief="raised", bd=3, activebackground="#b9c7a5", cursor="hand2")
        self.btn_calcular.pack(pady=20)

        # Área para el número gigante
        self.frame_numero = tk.Frame(root, bg="#f2efe9")
        self.frame_numero.pack(pady=10)
        self.numero_label = tk.Label(self.frame_numero, text="?", font=("Segoe UI", 96, "bold"),
                                     bg="#f2efe9", fg="#b8a47a")
        self.numero_label.pack()

        # Definición
        self.definicion_label = tk.Label(root, text="Ingresa tu fecha y presiona calcular",
                                         wraplength=550, justify="center", font=("Segoe UI", 11),
                                         bg="#f2efe9", fg="#7f6e59")
        self.definicion_label.pack(pady=20, padx=30)

        # Valores por defecto
        self.dia.delete(0, tk.END)
        self.dia.insert(0, "6")
        self.mes.delete(0, tk.END)
        self.mes.insert(0, "11")
        self.anio.delete(0, tk.END)
        self.anio.insert(0, "1959")

    def vibrar_numero(self):
        """Efecto visual: cambia color momentáneamente."""
        original_color = self.numero_label.cget("fg")
        self.numero_label.config(fg="#d67e2e")
        self.root.after(200, lambda: self.numero_label.config(fg=original_color))

    def calcular_con_sonido(self):
        """Reproduce sonido y luego calcula."""
        reproducir_click()  # Sonido global
        self.calcular()

    def calcular(self):
        """Lógica de cálculo y actualización de la interfaz."""
        try:
            dia = int(self.dia.get())
            mes = int(self.mes.get())
            anio = int(self.anio.get())
            datetime(anio, mes, dia)  # Validación simple
        except ValueError:
            messagebox.showerror("Fecha inválida", "Por favor ingresa una fecha real (ej: 6 11 1959)")
            return

        num = calcular_numero_mision(dia, mes, anio)
        self.numero_label.config(text=str(num))
        definicion = SIGNIFICADOS.get(num, "Número especial. Eres único.")
        self.definicion_label.config(text=f"🔢 Número {num}: {definicion}")
        self.vibrar_numero()

# --------------------------------------------------
# EJECUCIÓN PRINCIPAL
# --------------------------------------------------
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppNumerologia(ventana)
    ventana.mainloop()