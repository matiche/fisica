import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# Hélice Conica

# Hélice Circular
def helice_circular_1():
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    def gen(n):
        t = 0
        r = 5
        while t < 8 * np.pi:
            yield np.array([r * np.cos(t), r * np.sin(t), t])
            t += 5.5 * np.pi / n

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 100
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label='Curva Helice Circular')
    ax.legend()

    # Setting the axes properties

    ax.set_xlim3d([-8.0, 8.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-8.0, 8.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 16.0])
    ax.set_zlabel('Z')
    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=16, repeat=False)
    plt.show()

    pass
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


    helice_circular_im=tk.PhotoImage(file="helice_circular1.gif")
    helice_circular_button=tk.Button(master=frame, text="helice circular", command=helice_circular_1, image=helice_circular_im)
    helice_circular_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()
