from ViajeroFrecuente import ViajeroFrecuente


class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.test,
            '5':self.salir
        }
    def lanzarMenu(self,manejadorViajero):
        #Menu opciones
        #Leer numero viajero y verificarlo
        numeroViajero=0
        bandera=True
        iViajero=0
        while bandera:
            numeroViajero=int(input('Ingrese numero de viajero:\n'))
            resultado=manejadorViajero.buscarViajeroPorNumero(numeroViajero)
            if resultado!=-1:
                bandera=False
                iViajero=resultado
            else:
                print('El numero de viajero ingresado no se encontro.')
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para consultar la cantidad de millas.')
            print('-Ingrese 2 para acumular millas.')
            print('-Ingrese 3 para canjear millas.')
            print('-Ingrese 4 para ejecutar un test.')
            print('-Ingrese 5 para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion=='1' or opcion=='2' or opcion=='3':
                ejecutar(manejadorViajero,iViajero)
            elif opcion=='4':
                ejecutar(manejadorViajero)
            else:
                ejecutar()
    def opcion1(self,manejadorViajero,iViajero):
        manejadorViajero.consultarMillas(iViajero)
    def opcion2(self,manejadorViajero,iViajero):
        millas=int(input('Ingrese las millas para acumular:\n'))
        manejadorViajero.acumularMillas(iViajero,millas)
    def opcion3(self,manejadorViajero,iViajero):
        millas=int(input('Ingrese las millas para canjear:\n'))
        manejadorViajero.canjearMillas(iViajero,millas)
    def test(self,manejadorViajero):
        manejadorViajero.test()
        viajero=ViajeroFrecuente(11,'22222222','Prueba','Test',1000)
        viajero.test()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')