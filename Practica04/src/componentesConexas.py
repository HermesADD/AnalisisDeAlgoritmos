"""
Autor:
Hermes Alberto Delgado Díaz
319258613
"""
def leer_grafica(nombreArchivo):
  """
  Lee una gráfica desde un archivo.

  Parámetros:
  - nombreArchivo(str): Nombre del archivo que contiene la gráfica.

  Retorno:
  - dict: Un diccionario donde las claves son los vértices y los valores son vecinos.
  
  Ejemplo de formato del archivo:
    a,b,c,d,e,
    a,b,
    b,c,
    d,e,
  Resultado:
    {
      'a': ['b'],
      'b': ['a', 'c'],
      'c': ['b'],
      'd': ['e'],
      'e': ['d']
    }
  """

  with open(nombreArchivo, 'r') as file:
    vertices = file.readline().strip().split(',')
    vertices = [vertice for vertice in vertices if vertice]#Evita vértices vacíos ""

    grafica = {vertice: [] for vertice in vertices}

    for linea in file:
      arista = linea.strip().split(',')
      arista = [a for a in arista if a]#Evita aristas vacías ""
      if len(arista) == 2:
        u,v = arista
        if u in grafica and v in grafica:
          grafica[u].append(v)
          grafica[v].append(u)

  return grafica

def dfs_componente_conexa(grafica, vertice, visitados):
  """
  Realiza una búsqeda DFS para encontrar una componente conexa de una gráfica.

  Parámetros:
  - grafica(dict): La gráfica.
  - vertice(str): Vértice inicial para la búsqueda.
  - visitados(set): Conjunto de vértices ya visitados.
  
  Retorno:
  - list: Lista de vértices que forman la componente conexa a la que pertenece el vértice inicial.
  """
  componente = [vertice]
  visitados.add(vertice)

  for vecino in grafica[vertice]:
    if vecino not in visitados:
      componente.extend(dfs_componente_conexa(grafica,vecino,visitados))

  return componente

def componentes_conexas(grafica):
  """
  Encuentra todas las componentes conexas de una gráfica no dirigida.
  
  Parámetros:
  - grafica(dict): La gráfica.

  Retorno:
  - list: Lista de componentes conexas de la gráfica.
  """
  visitados = set()
  componentes = []

  for vertice in grafica:
    if vertice not in visitados:
      componente = dfs_componente_conexa(grafica,vertice,visitados)
      componentes.append(componente)

  return componentes

def main(archivo):
  """
  Función principal. Lee una gráfica desde un archivo, calcula sus componentes conexas y las imprime.

  Parámetros:
  - archivo(str): Nombre del archivo que contiene la gráfica.
  """
  grafica = leer_grafica(archivo)
  componentes = componentes_conexas(grafica)
  print("Gráfica:")
  for vertice, vecinos in grafica.items():
    print(f"{vertice}: {', '.join(vecinos)}")
  print("\nEn la gráfica anterior se encuentran las siguientes componentes conexas:")
  for componente in componentes:
    print(f"[{', '.join(componente)}]")

if __name__ == "__main__":
  # Ejecuta la función principal con el archivo "grafica.txt"
  main("grafica.txt")