class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.categoria = None
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def _init_(self, raiz):
        self.raiz = Nodo(raiz)

    def insertar(self, valor, categoria, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if valor.lower() < nodo.valor.lower():
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
                nodo.izquierda.categoria = categoria
            else:
                self.insertar(valor, categoria, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
                nodo.derecha.categoria = categoria
            else:
                self.insertar(valor, categoria, nodo.derecha)

    def mostrar_categorias(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        categorias = set()

        if nodo.izquierda:
            categorias.update(self.mostrar_categorias(nodo.izquierda))
        if nodo.categoria is not None:
            categorias.add(nodo.categoria)
        if nodo.derecha:
            categorias.update(self.mostrar_categorias(nodo.derecha))

        return categorias

    def mostrar_animales_en_categoria(self, nodo, categoria, animales):
        if nodo is None:
            return

        if nodo.categoria is not None and nodo.categoria.lower() == categoria.lower():
            animales.append(nodo.valor)

        self.mostrar_animales_en_categoria(nodo.izquierda, categoria, animales)
        self.mostrar_animales_en_categoria(nodo.derecha, categoria, animales)

    def consultar_animal(self):
        categorias = self.mostrar_categorias()
        print("Categorías disponibles:")
        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")

        while True:
            try:
                opcion = int(input("Ingrese el número de la categoría que desea consultar: "))
                if 1 <= opcion <= len(categorias):
                    break
                else:
                    print("Opción no válida. Ingrese un número dentro del rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        categoria_elegida = list(categorias)[opcion - 1] if categorias else None

        if categoria_elegida:
            while True:
                animal = input(f"Ingrese el nombre del animal que desea consultar en la categoría '{categoria_elegida}': ").lower()
                if animal:
                    break
                else:
                    print("Por favor, ingrese un nombre de animal válido.")

            animales_en_categoria = []
            self.mostrar_animales_en_categoria(self.raiz, categoria_elegida, animales_en_categoria)

            encontrado = self._consultar_ayuda(self.raiz, categoria_elegida, animal)
            if encontrado:
                print(f"El animal {animal.capitalize()} pertenece a la categoría {categoria_elegida.capitalize()}.")

                if animales_en_categoria:
                    print(f"Animales en la categoría {categoria_elegida.capitalize()}:")
                    for i, animal_en_categoria in enumerate(animales_en_categoria, start=1):
                        print(f"{i}. {animal_en_categoria.capitalize()}")
                    
                    while True:
                        try:
                            opcion_animal = int(input("Ingrese el número del animal que desea seleccionar: "))
                            if 1 <= opcion_animal <= len(animales_en_categoria):
                                animal_seleccionado = animales_en_categoria[opcion_animal - 1]
                                print(f"Ha seleccionado el animal {animal_seleccionado.capitalize()}.")
                                break
                            else:
                                print("Opción no válida. Ingrese un número dentro del rango.")
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                else:
                    print(f"No hay otros animales en la categoría {categoria_elegida}.")
            else:
                print(f"No se encontró información para el animal {animal} en la categoría {categoria_elegida}.")
        else:
            print("No hay categorías disponibles para consultar.")

    def _consultar_ayuda(self, nodo, categoria, animal):
        if nodo is None:
            return False

        if nodo.valor.lower() == animal and (nodo.categoria is None or nodo.categoria.lower() == categoria.lower()):
            return True

        if animal < nodo.valor.lower():
            return self._consultar_ayuda(nodo.izquierda, categoria, animal)
        else:
            return self._consultar_ayuda(nodo.derecha, categoria, animal)


# Ejemplo de uso
arbol_animales = ArbolBinario("Animal")

# Ingresar información
arbol_animales.insertar("León", "Felino")
arbol_animales.insertar("Águila", "Ave")
arbol_animales.insertar("Tigre", "Felino")
arbol_animales.insertar("Loro", "Ave")
# Puedes agregar más animales y categorías según sea necesario

# Consultar información
arbol_animales.consultar_animal()
