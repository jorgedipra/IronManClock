# Importamos la biblioteca tkinter para crear la interfaz gráfica y el módulo time para obtener la hora actual
import tkinter as tk
import time

# Creamos una clase llamada IronManClock que representa el reloj digital
class IronManClock:
    def __init__(self):
        # Inicializamos la variable mostrarbarra En caso de que solo se quiera ver la hora sin los controles
        self.mostrarbarra = True 

        # Inicializamos la ventana principal de la aplicación
        self.window = tk.Tk()

        # Configuramos la ventana para que no tenga barra de título y sea transparente
        self.window.overrideredirect(1)
        self.window.attributes('-transparentcolor', 'black')

        # Configuramos el tamaño y la posición de la ventana
        self.window.geometry("350x150+20+20")

        # Establecemos el color de fondo de la ventana en negro
        self.window.configure(bg='black')

        # Creamos una etiqueta para mostrar la hora actual
        self.time_label = tk.Label(self.window, text="", font=("OCR A Extended", 100), bg="black", fg="#00FFFF")
        self.time_label.pack(pady=10)

        # Asociamos los eventos del ratón para permitir arrastrar la ventana
        self.window.bind("<ButtonPress-1>", self.start_move)
        self.window.bind("<B1-Motion>", self.move_window)
        if(self.mostrarbarra==True):
            # Añadimos controles adicionales
            self.add_controls()

        # Actualizamos el reloj y ejecutamos la interfaz gráfica
        self.update_clock()
        self.window.mainloop()

    def start_move(self, event):
        # Guardamos las coordenadas del ratón en el momento del clic
        self.x = event.x
        self.y = event.y

    def move_window(self, event):
        # Calculamos la nueva posición de la ventana según el movimiento del ratón
        self.window.geometry(f"+{event.x_root-self.x}+{event.y_root-self.y}")

    def update_clock(self):
        # Obtenemos la hora actual y la formateamos
        current_time = time.strftime("%I:%M %p").lstrip("0")
        current_time = current_time.zfill(8) # Agregamos cero a la izquierda si es necesario

        # Mostramos la hora en la etiqueta
        self.time_label.configure(text=current_time)

        # Ajustamos el tamaño de la fuente en función del ancho de la ventana
        window_width = self.window.winfo_width()
        font_size = int(window_width / 7)
        if font_size > 100: # Limitamos el tamaño máximo de la fuente a 100
            font_size = 100
        self.time_label.configure(font=("OCR A Extended", font_size))

        if current_time.endswith("PM"): # Si la hora actual termina con "PM", configuramos el color de fuente a naranja (#ff8000)
            self.time_label.configure(fg="#ff8000")
        else: # Si no, configuramos el color de fuente a cyan (#00FFFF)
            self.time_label.configure(fg="#00FFFF")

        # Creamos el efecto de azul neón cambiando continuamente el color de la fuente
        current_color = self.time_label.cget("fg")
        if current_color == "#ff8000": # Si el color es naranja, cambiamos el color de fuente a blanco (#ffffff)
            self.time_label.configure(fg="#ffffff")
        else: # Si no, cambiamos el color de fuente a cyan (#00FFFF)
            self.time_label.configure(fg="#00FFFF")

        current_time = current_time[:-2] + current_time[-2:].upper()
        self.time_label.configure(text=current_time)

        # Esperamos 1000 milisegundos (1 segundo) y luego llamamos a la función `update_clock` nuevamente
        self.window.after(1000, self.update_clock)

    def add_controls(self):
        # Creamos un marco para los controles adicionales
        control_frame = tk.Frame(self.window, bg='#353535')
        control_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Botón para cerrar la ventana
        close_button = tk.Button(control_frame, text="Cerrar", command=self.window.destroy, bg='#353535', fg='white')
        close_button.pack(side=tk.RIGHT, padx=20, pady=5)

        # Botón de opción para siempre en primer plano
        self.always_on_top_var = tk.IntVar()
        always_on_top_rb = tk.Checkbutton(control_frame, text="Primer plano", variable=self.always_on_top_var, command=self.toggle_always_on_top, bg='#353535', fg='white', selectcolor='black')
        always_on_top_rb.pack(side=tk.LEFT, padx=90, pady=5)

    def toggle_always_on_top(self):
        # Configuramos la ventana para que esté siempre en primer plano según el estado del botón de opción
        self.window.attributes('-topmost', self.always_on_top_var.get())

# Creamos una instancia de la clase `IronManClock` y comenzamos la ejecución del reloj
clock = IronManClock()
