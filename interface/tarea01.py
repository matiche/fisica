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

def curva_de_ejemplo():
    """
    Curva de Ejemplo que despliega una curva paramétrica en una ventana nueva

    Integrantes:
    - Omar Olivares Urrutia (@ofou)
    :return: plot curve
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z ** 2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='Curva Paramétrica de Ejemplo')
    ax.legend()

    fig.show()

    # Añadir el plot de matplotlib
    # fig = Figure(figsize=(5, 4), dpi=100)
    # t = np.arange(0, 3, .01)
    # fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
    #
    # canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    # canvas.draw()
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #
    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # canvas.mpl_connect("key_press_event", on_key_press)

    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.


def helice_conica():
    # añadir sus códigos aca
    """
        Curva de Ejemplo que despliega una Helice Cónica

        Integrantes:
        - Mario Labbé (@LsMario1998)
        - Mario González (@tatameister)
        - Cristóbal Cortés (@Cristobal140)
        - Thadly Guerra (@Thadly64)
        - Luis Inostroza (@luisinostrozaf)
        :return: Curva Helice Cónica
        """

    plt.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
    print (np.cos((np.pi*30)/180))

    e = 2.718281
    a = 3
    x = a * (e**(np.sin(45) * (1/np.tan(30)*theta))) * np.cos(theta)
    y = a * (e**(np.sin(45) * (1/np.tan(30)*theta)))* np.sin(theta)
    z = a * (e**(np.sin(45) * (1/np.tan(30)*theta))) * (1/np.tan(45))

    ax.plot(x, y, z, label='helice cónica')
    ax.legend()

    plt.show()
    pass
def helice_circular_1():
    """
    Curva que depliega una una helice circular en una ventana nueva

    Integrantes:
    - Felipe Lopez Vergara (@felipelopez00)
    - Bastian Bustamante Moraga (@BastianBustamante)
    - Rodrigo Torrez Queupan (@imperium31)
    - Juan Hernandez Gatica (@juanpablo1994)
    -Eric Rojas Palma (@valukar)
    :return: circular propeller
    """

    # añadir sus códigos aca
    n = 1000
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # caracteristicas de la helice circular
    t_max = 8 * np.pi
    t = np.linspace(0, t_max, n)
    z = t
    r = 5
    y = r * np.sin(t)
    x = r * np.cos(t)
    ax.plot(x, y, z, 'b', lw=2, label='Curva Hélice Circular')
    ax.legend()
    # linea ax.legend()oja al centro de la helice circular
    ax.plot((0, 0), (0, 0), (-t_max * 0.2, t_max * 1.2), color='r', lw=2)

    plt.show()
    pass
def Corona_Sinusoidal():
    '''    INTEGRANTES GRUPO:

          _Luis Soto Zelada (@Luiss23)
          _Diego Rojas (@diegoskky)
          _Lucia Vilches (@luciavj)
          grafica una corona sinusoidal en un plano cartesiano
          De la forma  f(x)=2sen(pi * x)'''
    Fs: int = 80  # corresponde al limite de la funcion en un ciclo
    f: float = 1  # cantidad de unidades del eje y
    sample: int = 80
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)
    plt.plot(x, y)
    plt.show()
    pass

def curva_de_viviani():
    """
    Funcion que muestra una curva de viviani en una nueva ventana

    Integrantes:
    Levi Urbina
    Natalia Valenzuela
    Ricardo Vergara
    Estefany Alarcon

    return: curva_de_viviani
    """

    a = 1
    t = np.linspace(-4, 4 * np.pi, 100)
    x = a * (1 + np.cos(t))
    y = a * np.sin(t)
    z = 2 * a * np.sin(t / 2)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_title("Curva de viviani")
    ax.plot(x, y, z, label="Curva de Viviani", lw=5)
    plt.show()
    pass
def hipopoda_1():
    # añadir sus códigos aca
    '''
           Integrantes:
           - Boris Gutiérrez Cornejo (@BorisAndresLmb)
           - Juan González Jélvez (@JuanGonzalez33)
           - Pablo Barrera Whiteley (@Pablobw)
           - José Flores Cáceres (@JoseFlores9)
           - Cristobal Rojas Saavedra (@cristotix)

           Función hipopoda_1: Grafica la hipopoda
           Utiliza la forma paramétrica de la función
           x= a+(r-a)*cos(t)
           y=(r-a)*sen(t)
           z=2*((a*(r-a))**1/2))*sen(t)
           Parametros:
           a= distancia del centro de la esfera al eje del cilindro
           r=Radio de la esfera
           return: plot Curve (Hipopede)
           '''

    """plt.rcParams['legend.fontsize'] = 12
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 99)
    a = 1
    r = 5
    x = a + (r - a) * np.cos(theta)
    y = (r - a) * np.sin(theta)
    z = 2 * (a * (r - a)) ** (1 / 2) * np.sin(theta / 2)
    curva,= ax.plot(x, y, z,label='Hipopede de Eudoxo')

    def update(num, x, y, curva):
        line.set_data(x[:num], y[:num])
        line.axes.axis([0, 10, 0, 1])
        return curva,
    ax.legend()
"""
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    def gen(n):
        for theta in np.linspace(0, 4 * np.pi, 99):
            yield np.array([5 + (20 - 5) * np.cos(theta), (20 - 5) * np.sin(theta),
                            2 * (5 * (20 - 5)) ** (1 / 2) * np.sin(theta / 2)])

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 100
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

    # Setting the axes properties
    ax.set_xlim3d([-20.0, 20.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-20.0, 20.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-20.0, 20.0])
    ax.set_zlabel('Z')

    anim = ani.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000 / N, blit=False,repeat=False)
    # ani.save('matplot003.gif
    plt.show()
    pass
def conica_de_papus():
    """
        Curva que entrega una conica de papus en la interfaz grafica

        Integrantes:
        - José Fabián Ignacio González Encina (@GoldenFenix)
        - Cristian Eduardo Castillo (@criseduardjjd)
        - Diego Faundez Mendez(@diegofaundezm)
        - Claudio Alcaino Muñoz (@klauser99)
        - Francisco Castillo Moraga(@taifokk)
        :return: conica de papus
        """
    plt.rcParams['legend.fontsize'] = 12

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Prepare arrays x, y, z
    t = np.linspace(-9 * np.pi, 9 * np.pi, 2000)

    a1 = 30

    a = 15
    z = a1 * np.cos(a) * t
    r = z ** 2 + 1
    x = a1 * np.sin(a) * t * np.cos(t)
    y = a1 * np.sin(a) * t * np.sin(t)

    ax.plot(x, y, z, label='espiral conica de papus')
    ax.legend()

    plt.show()

    pass
def Curva_de_Arquitas():
    """""
        Tipo de curva: Curva de Arquitas

        Integrantes:
        Nicolas Fernandez (@matiche)
        Sebastian Mendez  (@SebaMendez)
        Cristobal Moreira (@cmoreirab)
        Gabriel Lara      (@Gabolara453)
        Dennis Queirolo   (@dennis-queirolo)
        :return: Curva de arquitas
        """

    plt.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-10 * np.pi, 10 * np.pi, 100)
    a = 4
    t = 10
    z = a * ((1 - np.cos(theta)) * np.cos(theta)) - (np.pi / 2 <= t <= np.pi / 2)
    z = - a * ((1 - np.cos(theta)) * np.cos(theta)) - (np.pi / 2 <= t <= np.pi / 2)
    x = a * np.cos(theta) ** 2
    y = a * np.cos(theta) * np.sin(theta)

    ax.plot(x, y, z, label=('Curva de Arquitas'))
    ax.legend()

    plt.show()


def horoptera():
    # añadir sus códigos aca
    pass
def Curva_Bicilindrica():
    # añadir sus códigos aca
    pass

if __name__ == '__main__':
    # Creación de Ventanas
    root = tk.Tk()
    root.wm_title("Proyecto de Fisica 2019/01")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)

    # Cada grupo debe utilizar sus propia función
    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Ejemplo", command=curva_de_ejemplo)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hélice Cónica", command=helice_conica)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hélice Circular", command=helice_circular_1)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Corona Sinusoidal", command=Corona_Sinusoidal)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Viviani", command=curva_de_viviani)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hipopoda", command=hipopoda_1)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Arquitas", command=Curva_de_Arquitas)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva Bicilindrica", command=Curva_Bicilindrica)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Conica de Papus", command=conica_de_papus)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Horoptera", command=horoptera)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()
