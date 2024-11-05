import random

def generate_k_zigzag(n, k):
    """
    Genera una secuencia k-zig-zag de tamaño n
    """
    sequence = list(range(1, n + 1))
    result = []
    left = 0
    right = n - 1
    while left <= right:
        # Tomar k elementos de izquierda a derecha
        for _ in range(k):
            if left <= right:
                result.append(sequence[left])
                left += 1
        # Tomar k elementos de derecha a izquierda
        for _ in range(k):
            if left <= right:
                result.append(sequence[right])
                right -= 1
    return result

class SortingAlgorithms:
    def __init__(self):
        self.operations = 0
    
    def reset_operations(self):
        self.operations = 0

    def merge_sort(self, arr):
        self.operations += 1
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            self.operations += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            self.operations += 1
            
            while j >= 0 and arr[j] > key:
                self.operations += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def local_insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            self.operations += 1
            
            # Solo comparar con los k elementos anteriores
            while j >= max(0, i-k) and arr[j] > key:
                self.operations += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

def run_experiments():
    sizes = [1000, 2500, 5000, 10000]
    k_values = [2, 4]  # Puedes modificar estos valores
    
    print("n\tk\tMerge Sort\tLocal Insertion\tInsertion Sort")
    print("-" * 60)
    
    sorter = SortingAlgorithms()
    
    for n in sizes:
        for k in k_values:
            # Generar secuencia k-zig-zag
            sequence = generate_k_zigzag(n, k)
            
            # Merge Sort
            sorter.reset_operations()
            sorted_merge = sorter.merge_sort(sequence.copy())
            merge_ops = sorter.operations
            
            # Local Insertion Sort
            sorter.reset_operations()
            sorted_local = sorter.local_insertion_sort(sequence.copy())
            local_ops = sorter.operations
            
            # Insertion Sort
            sorter.reset_operations()
            sorted_insertion = sorter.insertion_sort(sequence.copy())
            insertion_ops = sorter.operations
            
            print(f"{n}\t{k}\t{merge_ops}\t\t{local_ops}\t\t{insertion_ops}")

if __name__ == "__main__":
    # Ejemplo de uso
    n = int(input("Ingrese el tamaño de la secuencia (n): "))
    k = int(input("Ingrese el valor de k (1 ≤ k ≤ n/2): "))
    
    if k < 1 or k > n//2:
        print("Error: k debe estar entre 1 y n/2")
    else:
        # Generar y mostrar la secuencia k-zig-zag
        sequence = generate_k_zigzag(n, k)
        print("\nSecuencia k-zig-zag generada:", sequence)
        
        # Ejecutar experimentos
        print("\nEjecutando experimentos con diferentes tamaños...")
        run_experiments()