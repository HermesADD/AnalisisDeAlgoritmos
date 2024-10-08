import java.util.Random;
import java.util.Scanner;

/**
 * Clase Busqueda que realiza del ejercicio 2 de la tarea 4.
 * @author Hermes 
 */
public class Busqueda {
    
    /**
     * Método que crea un arreglo aleatorio de n elementos, con un incremento de maximo 1.
     * @param a Primer elemento 
     * @return arreglo de n elementos
     */
    public static int[] arregloAleatorio(int n, int a){
        int[] X = new int[n];
        X[0] = a;
        
        Random random = new Random();
        
        for (int i = 1; i <= n - 1; i++) {
            X[i] = X[i - 1] + random.nextInt(2);
        }

        return X;
    }

    public static int busqueda(int[] X, int z){
        return busquedaRec(X, 0, X.length-1,z); 
    }
    /**
     * Metodo que busca un elemento z en el arreglo
     * @param X
     * @param ini
     * @param fin
     * @param z
     * @return
     */
    private static int busquedaRec(int[] X,int ini, int fin,  int z){
        if (ini > fin) {
            return -1;
        }

        int mid = (ini + fin) / 2;

        if (X[mid] == z) {
            return mid;
        }

        if (X[mid] < z) {
            int nuevoInicio = mid + (z - X[mid]); 
            return busquedaRec(X, nuevoInicio, fin, z);
        }else{
            int nuevoFin = mid - (X[mid] - z); 
            return busquedaRec(X, ini, nuevoFin, z);  
        }
    }

    public static void main(String  args[]){
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // Leer el valor de n
        System.out.print("Ingrese el valor de n: ");
        int n = scanner.nextInt();

        // Generar valores aleatorios para a y b, asegurando que a < b
        int a = random.nextInt(100);  // Valor aleatorio para a

        // Generar el arreglo
        int[] X = arregloAleatorio(n, a);

        // Imprimir el arreglo generado
        System.out.println("Arreglo generado:");
        for (int i = 0; i < n; i++) {
            System.out.print(X[i] + " ");
        }
        System.out.println();

        // Generar un valor z aleatorio entre a y b
        int z = a + random.nextInt(20);
        System.out.println("Valor z a buscar: " + z);

        // Realizar la búsqueda
        int indice = busqueda(X, z);

        // Imprimir el resultado
        if (indice != -1) {
            System.out.println("Elemento " + z + " encontrado en el índice " + indice);
        } else {
            System.out.println("Elemento " + z + " no encontrado en el arreglo.");
        }

        scanner.close();
    }
}
