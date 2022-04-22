import csv
from ViajeroFrecuente import ViajeroFrecuente

class ManejadorViajero:
    __listaViajeros=[]
    def __init__(self):
        self.__listaViajeros=[]
    def agregarViajero(self,viajero):
        if type(viajero)==ViajeroFrecuente:
            self.__listaViajeros.append(viajero)
        else:
            print('Error, no se pudo agregar un viajero a la lista, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='viajeros.csv'
        archivo=open(nombreArchivo)
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                self.agregarViajero(ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4])))
        archivo.close()
        print('Fin de la carga desde: ',nombreArchivo)
    def buscarViajeroPorNumero(self,numero):
        i=0
        bandera=True
        cantidadViajeros=len(self.__listaViajeros)
        while i<cantidadViajeros and bandera:
            if self.__listaViajeros[i].comprobarNumero(numero):
                bandera=not bandera
            else:
                i+=1
        resultado=None
        if bandera:
            resultado=-1
        else:
            resultado=i
        return resultado
    def consultarMillas(self,iViajero):
        print('Millas: ',self.__listaViajeros[iViajero].cantidadTotaldeMillas())
    def acumularMillas(self,iViajero,millasNuevas):
        if millasNuevas<0:
            print('No se admiten valores negativos')
        else:
            print('Millas actuales: ',self.__listaViajeros[iViajero].acumularMillas(millasNuevas))
    def canjearMillas(self,iViajero,millasACanjear):
        if millasACanjear<0:
            print('No se admiten valores negativos')
        else:
            print('Millas actuales: ',self.__listaViajeros[iViajero].canjearMillas(millasACanjear))
    def test(self):
        print('Comienza test ManejadorViajero')
        manejador=ManejadorViajero()
        print('Metodo cargarDesdeArchivo()')
        manejador.cargarDesdeArchivo()
        print('Metodo agregarViajero()')
        manejador.agregarViajero('viajero')
        manejador.agregarViajero(ViajeroFrecuente(19,'38123123','Pedro','Fernandez',1000))
        print('Metodo buscarViajeroPorNumero()')
        print(manejador.buscarViajeroPorNumero(23))
        iViajero=manejador.buscarViajeroPorNumero(19)
        print(iViajero)
        print('Metodo consultarMillas()')
        manejador.consultarMillas(iViajero)
        print('Metodo acumularMillas()')
        manejador.acumularMillas(iViajero,1000)
        manejador.acumularMillas(iViajero,-1000)
        print('Metodo canjearMillas()')
        manejador.canjearMillas(iViajero,2001)
        manejador.canjearMillas(iViajero,2000)
        manejador.canjearMillas(iViajero,-1000)
        print('Fin test ManejadorViajero. \n')