import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Hélice Conica

# Hélice Circular

# Corona Sinusoidal

# Curva de Viviani

# Hipopoda

# Espiral Cónica de Papus

# Curva de Arquitas

# Horóptera

def sig(i, XYZ, horoptera):
    horoptera.set_data(XYZ[:2, :i])
    horoptera.set_3d_properties(XYZ[2, :i])
def horoptera():
    plt.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = Axes3D(fig)
    r = 3   #corresponde al radio
    c = 1   #es una constante
    t = np.linspace(-2.*np.pi, 2.0*np.pi, 100)
    #se crean los ejes
    z = t
    x = 2 * r / (1 + ((c ** 2) * (t ** 2)))
    y = 2 * r * c * t / (1 + ((c ** 2) * (t ** 2)))
    #se crea lista de ejes
    XYZ = [x, y, z]
    XYZ = np.array(list(XYZ))
    horoptera, = ax.plot(x[0:1], y[0:1], z[0:1])
    #limites de los ejes
    ax.set_xlim3d([-8.0, 8.0])
    ax.set_xlabel('X')
    ax.set_ylim3d([-8.0, 8.0])
    ax.set_ylabel('Y')
    ax.set_zlim3d([-8.0, 8.0])
    ax.set_zlabel('Z')
    ax.set_title("Horoptera")
    animacion = animation.FuncAnimation(fig, sig, fargs=(XYZ, horoptera), frames=100, blit=False, interval=16,
                                        repeat=False)
    plt.show()
# Curva Bicilindrica

if __name__ == '__main__':
    # Creación de Ventanas
    root = tk.Tk()
    root.wm_title("Tarea 02 (15%)")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    horoptera_img = tk.PhotoImage(file="horoptera.png")
    curva_horoptera = tk.Button(master=frame, image=horoptera_img, command=horoptera, height="100", width="100")
    curva_horoptera.pack(side=tk.BOTTOM, padx=10, pady=10)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)

    tk.mainloop()
