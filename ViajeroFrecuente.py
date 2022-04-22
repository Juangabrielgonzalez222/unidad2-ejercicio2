class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=0
    def __init__(self,numViajero=0,dni='',nombre='',apellido='',millas=0):
        self.__num_viajero=numViajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    def acumularMillas(self,nuevaMilla):
        self.__millas_acum+=nuevaMilla
        return self.__millas_acum
    def comprobarNumero(self,numero):
        return self.__num_viajero==numero
    def canjearMillas(self,nuevaMilla):
        if nuevaMilla<=self.__millas_acum:
            self.__millas_acum-=nuevaMilla
            print('Se canjearon {} millas'.format(nuevaMilla))
        else:
            print('No se pudo realizar la operacion, la cantidad de millas a canjear es mayor que la cantidad de millas acumuladas.')
        return self.__millas_acum
    def mostrarDatos(self):
        print('Numero:{}, DNI:{}, Nombre:{}, Apellido:{} Millas:{}'.format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum))
    def test(self):
        print('Comienza test ViajeroFrecuente')
        viajero1=ViajeroFrecuente(1,'33222222','Pedro','Fernandez',900)
        viajero2=ViajeroFrecuente(2,'40555555','Camila','Gutierrez',1200)
        print('Metodo cantidadTotaldeMillas()')
        print(viajero1.cantidadTotaldeMillas())
        print(viajero2.cantidadTotaldeMillas())
        print('Metodo acumularMillas()')
        print(viajero1.acumularMillas(100))
        print(viajero2.acumularMillas(800))
        print('Metodo comprobarNumero()')
        print(viajero1.comprobarNumero(1))
        print(viajero2.comprobarNumero(3))
        print('Metodo canjearMillas()')
        print(viajero1.canjearMillas(3000))
        print(viajero2.canjearMillas(1000))
        print('Metodo mostrarDatos()')
        viajero1.mostrarDatos()
        viajero2.mostrarDatos()
        print('Fin test ViajeroFrecuente. \n')