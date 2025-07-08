from math import floor

class Persona:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.deudas = {}

    def get_id(self):
        return self.id
    
    def iniciar_deudas(self, personas: list):
        for p in personas:
            self.deudas[p] = 0.0
    
    def cambiar_deuda(self, id_destino, valor: float):
        self.deudas[id_destino] += valor


class Grupo:

    def __init__(self, nombre: str):
        self.__id = 0
        self.nombre = nombre
        self.personas = []
    
    def agrgar_persona(self, nombre: str):
        self.__id += 1
        persona = Persona(self.__id, nombre)
        self.personas.append(persona)
    
    def iniciar_deudas(self):
        for i in range(self.__id):
            lista_id = [j + 1 for j in range(self.__id) if j != i]
            self.persona[i].iniciar_deudas(lista_id)
    
    def crear_pago(self, id_pagador: int, total: float):
        excluidos = [id_pagador]
        excluir = True
        while excluir:
            # Excluir a alguien?
            # exlcuidos.append(seleccionado)
            excluir = False
            pass
        valor = floor(total / (self.__id - len(excluidos) - 1))
        for p in self.personas:
            if p.get_id() not in excluidos:
                p.cambiar_deuda(id_pagador, valor)
    
    def pagar_deuda(self):
        pass

