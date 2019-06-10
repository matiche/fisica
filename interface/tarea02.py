import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

# Hélice Conica
def helice_conica():
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    def gen(n):
        theta = 0
        e = 2.718281
        a = 0.5
        an1 = 45
        an2 = 30

        while theta > -25 * np.pi:
            x = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * np.cos(theta)
            y = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * np.sin(theta)
            z = a * (e ** (np.sin(an1) * (1 / np.tan(an2) * theta))) * (1 / np.tan(an1))
            yield np.array([x, y, z])
            theta += -8 * np.pi / n

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 150
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

    # Setting the axes properties
    ax.set_xlim3d([-10.0, 10.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-10.0, 10.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 10.0])
    ax.set_zlabel('Z')

    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=1000 / N, blit=False, repeat=False)

    plt.show()

# Hélice Circular

# Corona Sinusoidal

# Curva de Viviani

# Hipopoda

# Espiral Cónica de Papus

# Curva de Arquitas

# Horóptera

# Curva Bicilindrica

if __name__ == '__main__':
    # Creación de Ventanas
    root = tk.Tk()
    root.wm_title("Tarea 02 (15%)")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)

    curva_de_ejemplo = tk.Button(master=frame, text="Hélice Cónica", command=helice_conica)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)
    Conica_im = tk.PhotoImage(file="helice_conica.gif")
    conica_button = tk.Button(master=frame, text="Hélice Cónica", command=helice_conica, image=Conica_im)
    conica_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()