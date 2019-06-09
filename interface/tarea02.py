import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as ani
from mpl_toolkits.mplot3d import Axes3D
# Hélice Conica

# Hélice Circular

# Corona Sinusoidal

# Curva de Viviani

# Hipopoda
def Hipopoda():
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    def gen():
        for theta in np.linspace(0, 4 * np.pi, 99):
            yield np.array([20 + (50 - 20) * np.cos(theta), (50 - 20) * np.sin(theta),
                            2 * (5 * (50 - 20)) ** (1 / 2) * np.sin(theta / 2)])
    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 100
    plt.rcParams['legend.fontsize'] = 12
    data = np.array(list(gen())).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1],label='Hipopede de Eudoxo')

    ax.set_xlim3d([-50.0, 50.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-50.0, 50.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-50.0, 50.0])
    ax.set_zlabel('Z')
    anim = ani.FuncAnimation(fig, update, N, fargs=(data, line), interval=1700 / N, blit=False,repeat=False)
    ax.legend()
    plt.show()
    pass
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
    hipopoda_im = tk.PhotoImage(file="Figure_1.gif")
    hipopoda_button = tk.Button(master=frame, text="Hipopoda", command=Hipopoda, image=hipopoda_im)
    hipopoda_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()
