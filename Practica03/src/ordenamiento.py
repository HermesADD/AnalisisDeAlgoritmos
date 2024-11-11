from colorama import Fore, Style, init
"""
Autor:
Hermes Alberto Delgado Díaz
319258613
"""
class AlgoritmosOrdenamiento:
    """
    Clase que implementa algoritmos de ordenamiento que tiene un contador para registrar 
    la cantidad de operaciones elementales realizadas durante la ejecución.
    """

    def __init__(self):
        """
        Inicializa una instancia de algoritmos de ordenamiento con el 
        contador de operaciones en cero.
        """
        self.operaciones = 0
    
    def reiniciar_operaciones(self):
        """
        Reinicia el contador de operaciones a cero.
        """
        self.operaciones = 0
    
    def merge_sort(self, arr):
        """
        Implementa el algoritmo Merge Sort.

        Parámetros
            - arr(list): Lista de elementos a ordenar.

        Retorna:
            - list: Una nueva lista ordenada.
        """
        self.operaciones += 1
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) //2
        izq = self.merge_sort(arr[:mid])
        der = self.merge_sort(arr[mid:])

        return self.merge(izq, der)

    def merge(self, izq, der):
        """
        Combina dos listas ordenadas en una única lista ordenada.
        
        Parámetros:
            - izq(list): Sublista izquierda ordenada.
            - der(list): Sublista derecha ordenada.

        Retorna 
            - list: Lista ordenada que combina 'izq' y 'der'
        """
        resultado = []
        i = j = 0

        while i < len(izq) and j < len(der):
            self.operaciones +=1
            if izq[i] <= der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
        
        resultado.extend(izq[i:])
        resultado.extend(der[j:])

        return resultado
    
    def insertion_sort(self, arr):
        """
        Implementa el algoritmo Insertion Sort.

        Parámetros:
            - arr(list): Lista de elementos a ordenar.
        
        Retorna:
            - list: La misma lista ordena.
        """
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            self.operaciones += 1

            while j >= 0 and arr[j] > temp:
                self.operaciones += 1
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = temp

        return arr
    
    def local_insertion_sort(self, arr):
        """
        Implementa una variante de Insertion Sort utilizando una lista auxiliar.

        Parámetros:
            - arr (list): Lista de elementos a ordenar.

        Retorna:
            - list: La misma lista ordenada en el lugar.
        """
        n = len(arr)
        L = [arr[0]]

        for i in range(1,n):
            self.operaciones += 1
            insertado = False
            for j in range(len(L)):
                self.operaciones += 1
                if arr[i] < L[j]:
                    L.insert(j,arr[i])
                    insertado = True
                    break
            if not insertado: 
                L.append(arr[i])
        
        for i in range(n):
            self.operaciones += 1
            arr[i] = L[i]

        return arr
    
def generar_k_zigzag(n,k):
    """
    Genera una secuencia k-zigzag de tamaño n
    """
    secuencia = list(range(1,n+1))
    resultado = []
    izq = 0
    der = n-1

    while izq <= der:
        for _ in range(k):
            if izq <= der:
                resultado.append(secuencia[izq])
                izq += 1
        for _ in range(k):
            if izq <= der:
                resultado.append(secuencia[der])
                der -= 1
    return resultado

init(autoreset=True)

def realizar_experimentos():
    """
    Realiza experimentos para secuencias de tamaño 1000,2500,5000,10000 y k-zigzag 
    """
    tamanos = [1000,2500,5000,10000]
    k_valores = [3,6] #Se puede modificar

    print(f"{Fore.CYAN}n\tk\tMerge Sort\t\tLocal Insertion\t\tInsertion Sort")
    print(f"{Fore.LIGHTCYAN_EX}{'-' * 95}")

    ordenador = AlgoritmosOrdenamiento()

    for n in tamanos:
        for k in k_valores:
            secuencia = generar_k_zigzag(n,k)

            ordenador.reiniciar_operaciones()
            ordenacion_merge = ordenador.merge_sort(secuencia.copy())
            merge_ops = ordenador.operaciones

            ordenador.reiniciar_operaciones()
            ordenacion_local = ordenador.local_insertion_sort(secuencia.copy())
            local_ops = ordenador.operaciones

            ordenador.reiniciar_operaciones()
            ordenacion_insertion = ordenador.insertion_sort(secuencia.copy()) 
            insertion_ops = ordenador.operaciones

            print(f"{Fore.LIGHTGREEN_EX}{n}\t{k}\t{merge_ops}\t\t\t{local_ops}\t\t\t{insertion_ops}")

if __name__ == "__main__":
    sorter = AlgoritmosOrdenamiento()
    while True:
        print(f"{Fore.LIGHTYELLOW_EX}\nMenú Principal:")
        print(f"{Fore.LIGHTYELLOW_EX}1. Realizar experimentos.")
        print(f"{Fore.LIGHTYELLOW_EX}2. Ingresar valores de n y k.")
        print(f"{Fore.LIGHTYELLOW_EX}3. Salir.")
        opcion = input(f"{Fore.YELLOW}Seleccione una opción: ")

        if opcion == "1":
            realizar_experimentos()  # Asumiendo que tienes la función definida
            break
        elif opcion == "2":
            while True:
                try:
                    n = int(input(f"{Fore.BLUE}\nIngrese el tamaño de la secuencia (n): "))
                    if n <= 0:
                        print(f"{Fore.RED}Error: El tamaño de la secuencia (n) debe ser un número positivo.")
                        continue
                    break
                except ValueError:
                    print(f"{Fore.RED}Error: Debes ingresar un número entero válido para n.")

            while True:
                try:
                    k = int(input(f"{Fore.BLUE}\nIngrese el valor de k (1 <= k <= n/2): "))
                    if k < 1 or k > n // 2:
                        print(f"{Fore.RED}Error: k debe estar entre 1 y n/2.")
                        continue
                    break
                except ValueError:
                    print(f"{Fore.RED}Error: Debes ingresar un número entero válido para k.")
            
            secuencia = generar_k_zigzag(n, k)
            print(f"\n{Fore.CYAN}Secuencia k-zig-zag generada: {secuencia}")
            sorter.reiniciar_operaciones()
            print(f"\n{Fore.LIGHTMAGENTA_EX}Secuencia ordenada con Merge Sort: {sorter.merge_sort(secuencia.copy())}")
            print(f"\n{Fore.LIGHTMAGENTA_EX}Operaciones Merge Sort: {sorter.operaciones}")

            sorter.reiniciar_operaciones()
            print(f"\n{Fore.LIGHTGREEN_EX}Secuencia ordenada con Insertion Sort: {sorter.insertion_sort(secuencia.copy())}")
            print(f"\n{Fore.LIGHTGREEN_EX}Operaciones Insertion Sort: {sorter.operaciones}")

            sorter.reiniciar_operaciones()
            print(f"\n{Fore.LIGHTBLUE_EX}Secuencia ordenada con Local Insertion Sort: {sorter.local_insertion_sort(secuencia.copy())}")
            print(f"\n{Fore.LIGHTBLUE_EX}Operaciones Local Insertion Sort: {sorter.operaciones}")
        elif opcion == "3":
            print(f"{Fore.MAGENTA}Saliendo del programa.")
            break
        else:
            print(f"{Fore.RED}Opción no válida.")