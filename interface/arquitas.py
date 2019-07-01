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


def Atras(ventana):
    ventana.quit()
    ventana.destroy()


def sig(i, XYZ, arquitas):
    arquitas.set_data(XYZ[:2, :i])
    arquitas.set_3d_properties(XYZ[2, :i])


def sig1(s, X1Y1Z1, arquitas):
    arquitas.set_data(X1Y1Z1[:2, :s])
    arquitas.set_3d_properties(X1Y1Z1[2, :s])


def aceleracion():
    Tiempo = int(Entrada_ti.get())
    ti = t[Tiempo]
    x_v = -2 * a * np.cos(2 * ti)
    y_v = -2 * a * np.sin(2 * ti)
    z_v = (((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))
    x_v1 = -2 * a * np.cos(2 * ti)
    y_v1 = -2 * a * np.sin(2 * ti)
    z_v1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))
    ace = "(" + str(round(x_v, 3)) + "," + str(round(y_v, 3)) + "," + str(round(z_v, 8)) + ")"
    Var.set(ace)
    ace1 = "(" + str(round(x_v1, 3)) + "," + str(round(y_v1, 3)) + "," + str(round(z_v1, 8)) + ")"
    Var.set(ace1)


def velocidad():
    Tiempo = int(Entrada_ti.get())
    ti = t[Tiempo]
    x_a = -2 * a * np.sin(ti) * np.cos(ti)
    y_a = a * np.cos(2 * ti)
    z_a = (((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)
    x_a1 = -2 * a * np.sin(ti)
    y_a1 = a * np.cos(2 * ti)
    z_a1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)
    vel = "(" + str(round(x_a, 3)) + "," + str(round(y_a, 3)) + "," + str(round(z_a, 8)) + ")"
    vel1 = "(" + str(round(x_a1, 3)) + "," + str(round(y_a1, 3)) + "," + str(round(z_a1, 8)) + ")"
    Var.set((vel))
    Var.set((vel1))


def velocidad_media():
    TiempoI = int(Entrada_ti.get())
    TiempoF = int(Entrada_tf.get())
    ti = t[TiempoI]
    tf = t[TiempoF]
    ti1 = t[TiempoI]
    tf1 = t[TiempoF]
    x_vi = -2 * a * np.sin(ti) * np.cos(ti)
    y_vi = a * np.cos(2 * ti)
    z_vi = (((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_vi1 = -2 * a * np.sin(ti1) * np.cos(ti1)
    y_vi1 = a * np.cos(2 * ti1)
    z_vi1 = -(((2) ** 1 / 2) * a * np.cos(ti1 / 2) * np.cos(ti1 / 2) * (2 * np.cos(ti1) - 1)) / (
                (2 * np.cos(ti1) - np.cos(2 / ti1) - 1) ** 1 / 2)

    x_vf = -2 * a * np.sin(tf) * np.cos(tf)
    y_vf = a * np.cos(2 * tf)
    z_vf = (((2) ** 1 / 2) * a * np.cos(tf / 2) * np.cos(ti / 2) * (2 * np.cos(tf) - 1)) / (
                (2 * np.cos(tf) - np.cos(2 / tf) - 1) ** 1 / 2)

    x_vf1 = -2 * a * np.sin(tf1) * np.cos(tf1)
    y_vf1 = a * np.cos(2 * tf1)
    z_vf1 = -(((2) ** 1 / 2) * a * np.cos(tf1 / 2) * np.cos(tf1 / 2) * (2 * np.cos(tf1) - 1)) / (
                (2 * np.cos(tf1) - np.cos(2 / tf1) - 1) ** 1 / 2)

    x_v = (x_vf - x_vi) / (tf - ti)
    y_v = (y_vf - y_vi) / (tf - ti)
    z_v = (z_vf - z_vi) / (tf - ti)
    x_v1 = (x_vf1 - x_vi1) / (tf1 - ti1)
    y_v1 = (y_vf1 - y_vi1) / (tf1 - ti1)
    z_v1 = (z_vf1 - z_vi1) / (tf1 - ti1)

    vel = "(" + str(round(x_v, 8)) + "," + str(round(y_v, 8)) + "," + str(round(z_v, 8)) + ")"
    Var.set((vel))

    vel1 = "(" + str(round(x_v1, 8)) + "," + str(round(y_v1, 8)) + "," + str(round(z_v1, 8)) + ")"
    Var.set((vel1))


def aceleracion_media():
    TiempoI = int(Entrada_ti.get())
    TiempoF = int(Entrada_tf.get())
    ti = t[TiempoI]
    tf = t[TiempoF]
    ti1 = t[TiempoI]
    tf1 = t[TiempoF]
    x_ai = -2 * a * np.cos(2 * ti)
    y_ai = -2 * a * np.sin(2 * ti)
    z_ai = (((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    x_ai1 = -2 * a * np.cos(2 * ti1)
    y_ai1 = -2 * a * np.sin(2 * ti1)
    z_ai1 = -(((2) ** 1 / 2) * a * np.cos(ti1 / 2) + np.cos(ti1 / 2) * (
                (2 * np.cos(ti1) - 1) / ((2 * np.cos(ti1) - np.cos(2 / ti1) - 1) ** 1 / 2)))

    x_af = -2 * a * np.cos(2 * tf)
    y_af = -2 * a * np.sin(2 * tf)
    z_af = (((2) ** 1 / 2) * a * np.cos(tf / 2) + np.cos(tf / 2) * (
                (2 * np.cos(tf) - 1) / ((2 * np.cos(tf) - np.cos(2 / tf) - 1) ** 1 / 2)))

    x_af1 = -2 * a * np.cos(2 * tf1)
    y_af1 = -2 * a * np.sin(2 * tf1)
    z_af1 = -(((2) ** 1 / 2) * a * np.cos(tf1 / 2) + np.cos(tf1 / 2) * (
                (2 * np.cos(tf1) - 1) / ((2 * np.cos(tf1) - np.cos(2 / tf1) - 1) ** 1 / 2)))

    x_a = (x_af - x_ai) / (tf - ti)
    y_a = (y_af - y_ai) / (tf - ti)
    z_a = (z_af - z_ai) / (tf - ti)
    x_a1 = (x_af1 - x_ai1) / (tf1 - ti1)
    y_a1 = (y_af1 - y_ai1) / (tf1 - ti1)
    z_a1 = (z_af1 - z_ai1) / (tf1 - ti1)

    ace = "(" + str(round(x_a, 8)) + "," + str(round(y_a, 8)) + "," + str(round(z_a, 8)) + ")"
    Var.set((ace))

    ace1 = "(" + str(round(x_a1, 8)) + "," + str(round(y_a1, 8)) + "," + str(round(z_a1, 8)) + ")"
    Var.set((ace1))


def curvatura():
    Tiempo = int(Entrada_ti.get())
    ti = t[Tiempo]
    x_pder = -2 * a * np.sin(ti) * np.cos(ti)
    y_pder = a * np.cos(2 * ti)
    z_pder = (((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_pder1 = -2 * a * np.sin(ti) * np.cos(ti)
    y_pder1 = a * np.cos(2 * ti)
    z_pder1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_sder = -2 * a * np.cos(2 * ti)
    y_sder = -2 * a * np.sin(2 * ti)
    z_sder = (((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    x_sder1 = -2 * a * np.cos(2 * ti)
    y_sder1 = -2 * a * np.sin(2 * ti)
    z_sder1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    cruz_x = [(y_pder * z_sder) - (y_sder * z_pder), -((x_pder * z_sder) - (x_sder * z_pder)),
              (x_pder * y_sder) - (x_sder * y_pder)]

    cruz_x1 = [(y_pder1 * z_sder1) - (y_sder1 * z_pder1), -((x_pder1 * z_sder1) - (x_sder1 * z_pder1)),
               (x_pder1 * y_sder1) - (x_sder1 * y_pder1)]

    r = np.sqrt((cruz_x[0]) ** 2 + (cruz_x[1]) ** 2 + (cruz_x[2]) ** 2)
    s = (np.sqrt((x_pder ** 2) + (y_pder ** 2) + (z_pder ** 2))) ** 3

    r1 = np.sqrt((cruz_x1[0]) ** 2 + (cruz_x1[1]) ** 2 + (cruz_x1[2]) ** 2)
    s1 = (np.sqrt((x_pder1 ** 2) + (y_pder1 ** 2) + (z_pder1 ** 2))) ** 3

    curv = round(r / s, 8)
    Var.set(curv)
    curv1 = round(r1 / s1, 8)
    Var.set(curv1)


def radio_curvatura():
    Tiempo = int(Entrada_ti.get())
    ti = t[Tiempo]
    # derivadas
    x_pder = -2 * a * np.sin(ti) * np.cos(ti)
    y_pder = a * np.cos(2 * ti)
    z_pder = (((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_pder1 = -2 * a * np.sin(ti) * np.cos(ti)
    y_pder1 = a * np.cos(2 * ti)
    z_pder1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_sder = -2 * a * np.cos(2 * ti)
    y_sder = -2 * a * np.sin(2 * ti)
    z_sder = (((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    x_sder1 = -2 * a * np.cos(2 * ti)
    y_sder1 = -2 * a * np.sin(2 * ti)
    z_sder1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    cruz_x = [(y_pder * z_sder) - (y_sder * z_pder), -((x_pder * z_sder) - (x_sder * z_pder)),
              (x_pder * y_sder) - (x_sder * y_pder)]

    cruz_x1 = [(y_pder1 * z_sder1) - (y_sder1 * z_pder1), -((x_pder1 * z_sder1) - (x_sder1 * z_pder1)),
               (x_pder1 * y_sder1) - (x_sder1 * y_pder1)]

    r = np.sqrt((cruz_x[0]) ** 2 + (cruz_x[1]) ** 2 + (cruz_x[2]) ** 2)
    s = (np.sqrt((x_pder ** 2) + (y_pder ** 2) + (z_pder ** 2))) ** 3

    r1 = np.sqrt((cruz_x1[0]) ** 2 + (cruz_x1[1]) ** 2 + (cruz_x1[2]) ** 2)
    s1 = (np.sqrt((x_pder1 ** 2) + (y_pder1 ** 2) + (z_pder1 ** 2))) ** 3

    curv = r / s
    radio_curv = round(1 / curv, 8)
    Var.set(radio_curv)

    curv1 = r1 / s1
    radio_curv1 = round(1 / curv1, 8)
    Var.set(radio_curv1)


def torsion():
    Tiempo = int(Entrada_ti.get())
    ti = t[Tiempo]
    # derivadas

    x_pder = -2 * a * np.sin(ti) * np.cos(ti)
    y_pder = a * np.cos(2 * ti)
    z_pder = (((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_pder1 = -2 * a * np.sin(ti) * np.cos(ti)
    y_pder1 = a * np.cos(2 * ti)
    z_pder1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_sder = -2 * a * np.cos(2 * ti)
    y_sder = -2 * a * np.sin(2 * ti)
    z_sder = (((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    x_sder1 = -2 * a * np.cos(2 * ti)
    y_sder1 = -2 * a * np.sin(2 * ti)
    z_sder1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    x_tder = 2 * a * np.sin(ti) * np.cos(ti)
    y_tder = -2 * a * np.sin(2 * ti) + (a / (np.cos(2 * ti) ** 3)) / 4
    z_tder = -(((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_tder1 = 2 * a * np.sin(ti) * np.cos(ti)
    y_tder1 = -2 * a * np.sin(2 * ti) + (a / (np.cos(2 * ti) ** 3)) / 4
    z_tder1 = (((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    cruz_x = [(y_pder * z_sder) - (y_sder * z_pder), -((x_pder * z_sder) - (x_sder * z_pder)),
              (x_pder * y_sder) - (x_sder * y_pder)]
    r = np.sqrt((cruz_x[0]) ** 2 + (cruz_x[1]) ** 2 + (cruz_x[2]) ** 2) ** 2
    cruz_numerador = [(y_sder * z_tder) - (y_tder * z_sder), -((x_sder * z_tder) - (x_tder * z_sder)),
                      (x_sder * y_tder) - (x_tder * y_sder)]

    cruz_x1 = [(y_pder1 * z_sder1) - (y_sder1 * z_pder1), -((x_pder1 * z_sder1) - (x_sder1 * z_pder1)),
               (x_pder1 * y_sder1) - (x_sder1 * y_pder1)]
    r1 = np.sqrt((cruz_x1[0]) ** 2 + (cruz_x1[1]) ** 2 + (cruz_x1[2]) ** 2) ** 2
    cruz_numerador1 = [(y_sder1 * z_tder1) - (y_tder1 * z_sder1), -((x_sder1 * z_tder1) - (x_tder1 * z_sder1)),
                       (x_sder1 * y_tder1) - (x_tder1 * y_sder1)]

    r_torsion = round((cruz_numerador[0] * x_pder + cruz_numerador[1] * y_pder + cruz_numerador[2] * z_pder) / r, 3)
    Var.set(r_torsion)
    r_torsion1 = round(
        (cruz_numerador1[0] * x_pder1 + cruz_numerador1[1] * y_pder1 + cruz_numerador1[2] * z_pder1) / r1, 3)
    Var.set(r_torsion1)


def radio_torsion():
    Tiempo = int(Entrada_ti.get())
    ti = t[Tiempo]
    # derivadas
    x_pder = -2 * a * np.sin(ti) * np.cos(ti)
    y_pder = a * np.cos(2 * ti)
    z_pder = (((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_pder1 = -2 * a * np.sin(ti) * np.cos(ti)
    y_pder1 = a * np.cos(2 * ti)
    z_pder1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_sder = -2 * a * np.cos(2 * ti)
    y_sder = -2 * a * np.sin(2 * ti)
    z_sder = (((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    x_sder1 = -2 * a * np.cos(2 * ti)
    y_sder1 = -2 * a * np.sin(2 * ti)
    z_sder1 = -(((2) ** 1 / 2) * a * np.cos(ti / 2) + np.cos(ti / 2) * (
                (2 * np.cos(ti) - 1) / ((2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)))

    x_tder = 2 * a * np.sin(ti) * np.cos(ti)
    y_tder = -2 * a * np.sin(2 * ti) + (a / (np.cos(2 * ti) ** 3)) / 4
    z_tder = -(((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    x_tder1 = 2 * a * np.sin(ti) * np.cos(ti)
    y_tder1 = -2 * a * np.sin(2 * ti) + (a / (np.cos(2 * ti) ** 3)) / 4
    z_tder1 = (((2) ** 1 / 2) * a * np.cos(ti / 2) * np.cos(ti / 2) * (2 * np.cos(ti) - 1)) / (
                (2 * np.cos(ti) - np.cos(2 / ti) - 1) ** 1 / 2)

    cruz_x = [(y_pder * z_sder) - (y_sder * z_pder), -((x_pder * z_sder) - (x_sder * z_pder)),
              (x_pder * y_sder) - (x_sder * y_pder)]
    r = np.sqrt((cruz_x[0]) ** 2 + (cruz_x[1]) ** 2 + (cruz_x[2]) ** 2) ** 2
    cruz_numerador = [(y_sder * z_tder) - (y_tder * z_sder), -((x_sder * z_tder) - (x_tder * z_sder)),
                      (x_sder * y_tder) - (x_tder * y_sder)]
    r_torsion = round((cruz_numerador[0] * x_pder + cruz_numerador[1] * y_pder + cruz_numerador[2] * z_pder) / r, 8)
    radio_t = 1 / r_torsion
    Var.set(radio_t)

    cruz_x1 = [(y_pder1 * z_sder1) - (y_sder1 * z_pder1), -((x_pder1 * z_sder1) - (x_sder1 * z_pder1)),
               (x_pder1 * y_sder1) - (x_sder1 * y_pder1)]
    r1 = np.sqrt((cruz_x1[0]) ** 2 + (cruz_x1[1]) ** 2 + (cruz_x1[2]) ** 2) ** 2
    cruz_numerador1 = [(y_sder1 * z_tder1) - (y_tder1 * z_sder1), -((x_sder1 * z_tder1) - (x_tder1 * z_sder1)),
                       (x_sder1 * y_tder1) - (x_tder1 * y_sder1)]
    r_torsion1 = round((cruz_numerador1[0] * x_pder1 + cruz_numerador1[1] * y_pder1 + cruz_numerador1[2] * z_pder1) / r,
                       8)
    radio_t1 = 1 / r_torsion1
    Var.set(radio_t1)


def posicion():
    Tiempo = int(Entrada_ti.get())

    X = round(XYZ[0][Tiempo], 8)
    Y = round(XYZ[1][Tiempo], 8)
    Z = round(XYZ[2][Tiempo], 8)
    Axes = "(" + str(X) + "," + str(Y) + "," + str(Z) + ")"
    Var.set(Axes)
    X1 = round(X1Y1Z1[0][Tiempo], 8)
    Y1 = round(X1Y1Z1[1][Tiempo], 8)
    Z1 = round(X1Y1Z1[2][Tiempo], 8)
    Axes1 = "(" + str(X1) + "," + str(Y1) + "," + str(Z1) + ")"
    Var.set(Axes1)


def desbloquear_botones():
    boton_posicion.config(state="normal")
    boton_velocidad.config(state="normal")
    boton_aceleracion.config(state="normal")
    boton_velocidad_media.config(state="normal")
    boton_aceleracion_media.config(state="normal")
    boton_curvatura.config(state="normal")
    boton_radio_curvatura.config(state="normal")
    boton_torsion.config(state="normal")
    boton_radio_torsion.config(state="normal")
    boton_longitud_arco.config(state="normal")


def presionado(boton):
    desbloquear_botones()
    if (boton == "posicion"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="disabled")
        boton_posicion.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: posicion())
    elif (boton == "velocidad"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="disabled")
        boton_velocidad.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: velocidad())
    elif (boton == "aceleracion"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="disabled")
        boton_aceleracion.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: aceleracion())
    elif (boton == "velocidad media"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="normal")
        boton_velocidad_media.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: velocidad_media())
    elif (boton == "aceleracion media"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="normal")
        boton_aceleracion_media.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: aceleracion_media())
    elif (boton == "curvatura"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="disabled")
        boton_curvatura.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: curvatura())
    elif (boton == "radio curvatura"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="disabled")
        boton_radio_curvatura.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: radio_curvatura())
    elif (boton == "torsion"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="disabled")
        boton_torsion.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: torsion())
    elif (boton == "radio torsion"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="disabled")
        boton_radio_torsion.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: radio_curvatura())
    elif (boton == "longitud de arco"):
        Entrada_ti.config(state="normal")
        Entrada_tf.config(state="normal")
        boton_longitud_arco.config(state="disabled")
        Boton_R.config(state="normal", command=lambda: radio_curvatura())


if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.geometry("900x900")
    ventana.title("Curva de Arquitas")
    # creamos el frame contenedor de los elementos
    frame = tk.Frame(ventana)
    frame.grid(column=0, row=0)

    # creamos el grafico
    plt.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    frame_grafico = FigureCanvasTkAgg(fig, master=frame)
    frame_grafico.get_tk_widget().grid(column=1, row=1, columnspan=6, rowspan=9)

    ax = fig.gca(projection='3d')
    ab = fig.gca(projection='3d')
    a = 8  # corresponde al radio
    t = np.linspace(-1 / 2 * np.pi, 1 / 2 * np.pi, 100)
    x1 = a * np.cos(t) ** 2
    y1 = a * np.cos(t) * np.sin(t)
    z1 = - a * ((1 - np.cos(t)) * (np.cos(t)) ** 1 / 2)
    z = a * (((1 - np.cos(t)) * np.cos(t)) ** 1 / 2)
    x = a * np.cos(t) ** 2
    y = a * np.cos(t) * np.sin(t)
    XYZ = [x, y, z]
    X1Y1Z1 = [x1, y1, z1]
    XYZ = np.array(list(XYZ))
    X1Y1Z1 = np.array(list(X1Y1Z1))
    arquitas, = ax.plot(x[0:1], y[0:1], z[0:1])
    arquitas1, = ab.plot(x1[1:0], y1[1:0], z1[1:0])

    ax.set_xlim3d([-8.0, 8.0])
    ax.set_xlabel('Eje X')
    ax.set_ylim3d([-8.0, 8.0])
    ax.set_ylabel('Eje Y')
    ax.set_zlim3d([-8.0, 8.0])
    ax.set_zlabel('Eje Z')
    animacion = animation.FuncAnimation(fig, sig, fargs=(XYZ, arquitas), frames=100, blit=False, interval=1,
                                        repeat=False)

    ab.set_xlim3d([8.0, -8.0])
    ab.set_xlabel('Eje X1')
    ab.set_ylim3d([8.0, -8.0])
    ab.set_ylabel('Eje Y1')
    ab.set_zlim3d([8.0, -8.0])
    ab.set_zlabel('Eje Z1')
    animacion1 = animation.FuncAnimation(fig, sig1, fargs=(X1Y1Z1, arquitas1), frames=100, blit=False, interval=1,
                                         repeat=False)
    # creando Entradas para los numeros
    frame_entradas_texto = tk.Frame(frame)
    frame_entradas_texto.grid(column=1, row=10)
    texto_ti = tk.Label(frame_entradas_texto, text="Ti")
    texto_ti.grid(column=0, row=0)
    Entrada_ti = tk.Entry(frame_entradas_texto, state="disabled")
    Entrada_ti.grid(column=1, row=0, padx=(0, 50))
    texto_tf = tk.Label(frame_entradas_texto, text="Tf")
    texto_tf.grid(column=2, row=0)
    Entrada_tf = tk.Entry(frame_entradas_texto, state="disabled")
    Entrada_tf.grid(column=3, row=0, padx=(0, 50))
    Var = tk.StringVar()
    Boton_R = tk.Button(frame_entradas_texto, text="Resp =", state="disabled")
    Boton_R.grid(column=4, row=0)
    Res = tk.Label(frame_entradas_texto, textvariable=Var)
    Res.grid(column=5, row=0)

    # BOTONES--------------------------------------

    titulo = tk.Label(frame, text="Curva de Arquitas", font=("letter case", 50))
    titulo.grid(column=1, row=0, pady=40, columnspan=5, )

    boton_posicion = tk.Button(frame, text="Posicion ", width=20, height=2, command=lambda: presionado("posicion"))
    boton_posicion.grid(column=0, row=1)

    boton_velocidad = tk.Button(frame, text="Velocidad", width=20, height=2, command=lambda: presionado("velocidad"))
    boton_velocidad.grid(column=0, row=2)

    boton_velocidad_media = tk.Button(frame, text="Velocidad Media", width=20, height=2,
                                      command=lambda: presionado("velocidad media"))
    boton_velocidad_media.grid(column=0, row=3)

    boton_aceleracion = tk.Button(frame, text="Aceleracion", width=20, height=2,
                                  command=lambda: presionado("aceleracion"))
    boton_aceleracion.grid(column=0, row=4)

    boton_aceleracion_media = tk.Button(frame, text="Aceleracion Media", width=20, height=2,
                                        command=lambda: presionado("aceleracion media"))
    boton_aceleracion_media.grid(column=0, row=5)

    boton_curvatura = tk.Button(frame, text="Curvatura", width=20, height=2,
                                command=lambda: presionado("curvatura"))
    boton_curvatura.grid(column=0, row=6)

    boton_radio_curvatura = tk.Button(frame, text="Radio de Curvatura", width=20, height=2,
                                      command=lambda: presionado("radio curvatura"))
    boton_radio_curvatura.grid(column=0, row=7)

    boton_torsion = tk.Button(frame, text="Torsion", width=20, height=2,
                              command=lambda: presionado("torsion"))
    boton_torsion.grid(column=0, row=8)

    boton_radio_torsion = tk.Button(frame, text="Radio de Torsion", width=20, height=2,
                                    command=lambda: presionado("radio torsion"))
    boton_radio_torsion.grid(column=0, row=9)

    boton_longitud_arco = tk.Button(frame, text="Longitud de Arco", width=20, height=2,
                                    command=lambda: presionado("longitud de arco"))
    boton_longitud_arco.grid(column=0, row=10)

    boton_ani = tk.Button(frame, text="Ani", width=20, height=2)
    boton_ani.grid(column=6, row=0)
    boton_atras = tk.Button(frame, text="<", width=20, height=2, command=lambda: Atras(ventana))
    boton_atras.grid(column=0, row=0)
    tk.mainloop()
