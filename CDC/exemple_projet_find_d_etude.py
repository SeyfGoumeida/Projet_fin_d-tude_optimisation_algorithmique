import numpy as np
import matplotlib.pyplot as plt

def plot_fun(f,dom):
    
    # affichage du graphe d'une fonction de R^2 dans R,
    # de ses lignes de niveau,
    # et valeur de son minimum sur une grille discrÃ¨te.
    # f : fonction (prenant en entrÃ©e un tableau Ã  2 lignes de points Ã  calculer)
    # dom : domaine de la grille
    
    # Definition des valeurs x1 et x2, des grilles correspondantes et evaluation de f
    x, y = np.linspace(dom[0],dom[1],200), np.linspace(dom[2],dom[3],200)
    x, y = np.meshgrid(x,y)
    z = f(np.array([x.flatten(),y.flatten()])).reshape(x.shape)
    
    # valeur et position du minimum sur la grille:
    imin = np.unravel_index(np.argmin(z),z.shape)
    zmin = z[imin]
    print('valeur du minimum sur la grille : ',zmin)
    xmin, ymin = x[imin], y[imin]
    print('position du minimiseur : (',xmin,',',ymin,')')
    
    # Graphique 3D:
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot([xmin,xmin],[ymin,ymin],[0,zmin],marker='o')
    ax.plot_surface(x, y, z)
    ax.set_title('Graphe de la fonction')
    
    # Graphique des lignes de niveaux
    fig, ax = plt.subplots()
    CS = ax.contour(x, y, z)
    ax.clabel(CS, inline=1, fontsize=10)
    ax.set_title('Lignes de niveau')