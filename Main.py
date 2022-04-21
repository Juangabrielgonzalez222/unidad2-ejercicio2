from ManejadorViajero import ManejadorViajero
from Menu import Menu

if __name__== '__main__':
    manejadorViajero=ManejadorViajero()
    manejadorViajero.cargarDesdeArchivo()
    menu=Menu()
    menu.lanzarMenu(manejadorViajero)