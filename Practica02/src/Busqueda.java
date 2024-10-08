import java.util.Random;

/**
 * Clase Busqueda que realiza del ejercicio 2 de la tarea 4.
 * @author Hermes 
 */
public class Busqueda {
    /**
     * Método que crea un arreglo aleatorio de n elementos, con un incremento de maximo 1.
     * @param n Tamaño del arreglo
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

    /**
     * Metodo que busca un elemento z en un arreglo
     * @param X Arreglo de enteros
     * @param z Elemento a buscar
     * @return Indice donde se encuentra el elemento
     */
    public static int busqueda(int[] X, int z){
        return busquedaRec(X, 0, X.length-1,z); 
    }

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
        try {
            if(args.length< 1){
                throw new IllegalArgumentException("Proporciona el valor de n como argumento. \"java Busqueda n\" ");
            }else if(args.length > 1){
                throw new IllegalArgumentException("Proporciona solo el valor de n como argumento. \"java Busqueda n\" ");
            }

            int n = Integer.parseInt(args[0]);

            if (n < 2) {
                throw new IllegalArgumentException("El valor de n debe ser mayor o igual a 2.");
            }

            Random random = new Random();

            int a = random.nextInt(100);
            int[] X= arregloAleatorio(n, a);

            Colors.println("Arreglo generado:", Colors.CYAN);
            Colors.print("[", Colors.MAGENTA);
            
            for(int i = 0; i<n ; i++){
                Colors.print(X[i], Colors.MAGENTA);
                if(i<n-1){
                    Colors.print(",", Colors.MAGENTA);
                }
            }

            Colors.println("]", Colors.MAGENTA);

            int z = a + random.nextInt(20);
            Colors.println("Valor z a buscar:" + z, Colors.YELLOW);

            int index = busqueda(X,z);

            if(index != -1){
                Colors.println("El elemento " + z + " fue encontrado en el indice " + index, Colors.GREEN);
            }else{
                Colors.println("El elemento " + z + " no fue encontrado en el arreglo.", Colors.RED);
            }
        } catch (NumberFormatException e) {
            // Si el argumento proporcionado no es un número válido
            Colors.println("Error: El argumento proporcionado no es un número entero válido.", Colors.RED);
        } catch (IllegalArgumentException e) {
            // Manejo de argumentos inválidos (n menor que 2, o faltan argumentos)
            Colors.println("Error: " + e.getMessage(), Colors.RED);
        } catch (Exception e) {
            // Captura de cualquier otra excepción inesperada
            Colors.println("Error inesperado: " + e.getMessage(), Colors.RED);
        }
    }
}
