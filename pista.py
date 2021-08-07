class Pista:
    def __init__(self,nombre,filas,metros,ornamento):
        self.nombre=nombre
        self.filas=filas
        self.metros=metros
        self.ornamento=ornamento
        self.pista=[]
        for i in range(filas):
            self.pista.append([ornamento]*metros)

    def poner_carro(self,carro,fila,metro):
         self.pista[fila][metro]=carro

    def mostrar(self):
         print("    PISTA DE {}".format(self.nombre).center(self.metros))
         print("   ||SALIDA" +("=" * ((self.metros)-25)) + "||META")
         for i in range(self.filas):
             print(" ",end=" ")
             for j in range(self.metros):
                 print(self.pista[i][j], end="")
             print()

    

