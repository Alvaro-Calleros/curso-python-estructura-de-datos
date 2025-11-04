class Sll_alvaro:
    class _Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None
            
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0
       
    def agregar_final(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza ==  None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1 

milist = Sll_alvaro()
print(milist.cabeza)
print(milist.cola)
print(milist.tamano)