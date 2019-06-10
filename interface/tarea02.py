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
def conico_papus():
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    def gen(n):
        t = -6 * np.pi

        a1 = 30

        a = 15
        for t in np.linspace(-5 * np.pi, 5 * np.pi, 200):
            yield np.array([a1 * np.sin(a) * t * np.cos(t), a1 * np.sin(a) * t * np.sin(t), a1 * np.cos(a) * t])

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 200
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

    # Setting the axes properties
    ax.set_xlim3d([-400.0, 400.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-400.0, 400.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-400.0, 400.0])
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
    root.wm_title("funciones")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)

    curva_de_ejemplo = tk.Button(master=frame, text="conica de papus", command=conico_papus)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)
    Conica_im = tk.PhotoImage(file="conica_papu.gif")
    conica_button = tk.Button(master=frame, text="conica de papus", command=conico_papus, image=Conica_im)
    conica_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()
