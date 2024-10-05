import java.util.Random;
import java.util.Scanner;

/**
 * Clase Busqueda que realiza del ejercicio 2 de la tarea 4.
 * @author Hermes 
 */
public class Busqueda {
    
    public static int[] arregloAleatorio(int n, int a, int b){
        int[] X = new int[n];
        X[0] = a;  // El primer valor es a
        X[n - 1] = b;  // El último valor es b
        
        // Generar valores intermedios respetando las restricciones
        Random random = new Random();
        for (int i = 1; i < n - 1; i++) {
            if (X[i - 1] < b) {
                // Si el valor anterior es menor que b, podemos incrementar o mantener
                X[i] = X[i - 1] + random.nextInt(2);  // Puede ser el mismo valor o aumentar 1
            } else {
                // Si el valor anterior ya es mayor o igual que b, lo mantenemos o decrementamos
                X[i] = X[i - 1] - random.nextInt(2);  // Puede ser el mismo valor o disminuir 1
            }
        }
        return X;
    }

    public static int busqueda(int[] X,int ini, int fin,  int z){
        if (ini > fin) {
            return -1;  // No encontrado
        }

        int mid = (ini + fin) / 2;

        if (X[mid] == z) {
            return mid;  // Valor encontrado
        }

        // Si X[mid] es menor que z, movemos el índice hacia adelante
        if (X[mid] < z) {
            int nuevoInicio = mid + (z - X[mid]);  // Aprovechamos que la diferencia es ≤ 1
            return busqueda(X, nuevoInicio, fin, z);  // Llamada recursiva
        } else {
            // Si X[mid] es mayor que z, movemos el índice hacia atrás
            int nuevoFin = mid - (X[mid] - z);  // Aprovechamos que la diferencia es ≤ 1
            return busqueda(X, ini, nuevoFin, z);  // Llamada recursiva
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
        int b = a + n;  // Valor aleatorio para b, garantizando que b > a

        // Generar el arreglo
        int[] X = arregloAleatorio(n, a, b);

        // Imprimir el arreglo generado
        System.out.println("Arreglo generado:");
        for (int i = 0; i < n; i++) {
            System.out.print(X[i] + " ");
        }
        System.out.println();

        // Generar un valor z aleatorio entre a y b
        int z = a + random.nextInt(b - a + 1);
        System.out.println("Valor z a buscar: " + z);

        // Realizar la búsqueda
        int indice = busqueda(X,0,X.length-1, z);

        // Imprimir el resultado
        if (indice != -1) {
            System.out.println("Elemento " + z + " encontrado en el índice " + indice);
        } else {
            System.out.println("Elemento " + z + " no encontrado en el arreglo.");
        }

        scanner.close();
    }
}
