/**
 * Clase Adoquin
 * 
 * @author Hermes
 */

public class Adoquin {

    static int tamano_tablero, cont=0;
    static int [][]tablero;
    /**
     * Coloca un adoquin en las tres celdas dadas del tablero.
     *
     * @param x1 Coordenada x de la primera celda.
     * @param y1 Coordenada y de la primera celda.
     * @param x2 Coordenada x de la segunda celda.
     * @param y2 Coordenada y de la segunda celda.
     * @param x3 Coordenada x de la tercera celda.
     * @param y3 Coordenada y de la tercera celda.
     */
    public static void colocar(int x1, int y1, int x2, int y2, int x3, int y3){
        cont++;
        tablero[x1][y1]=cont;
        tablero[x2][y2]=cont;
        tablero[x3][y3]=cont; 
    }

    /**
     * Algoritmo divide y venceras, para cubrir el tablero con adoquines
     * 
     * @param n - Tamano del lado del subtablero actual.
     * @param x - Coordenada x de la esquina superior izquierda del subtablero actual.
     * @param y - Coordenada y de la esquina superior izquierda del subtablero actual.
     */
    public static void colocarAdoquines(int n, int x, int y){
        int f = 0;
        int c=0;
        if(n==2){
            cont++;
            for(int i = 0; i<n; i++){
                for(int j=0; j<n; j++){
                    if(tablero[x+i][y+j]==0){
                        tablero[x+i][y+j]=cont;
                    }
                }
            }

            return;
        }
        
        //Encontramos la ubicacion de la celda ocupada
        for(int i=x; i< x+n; i++){
            for(int j=y; j< y+n; j++){
                if(tablero[i][j]!=0){
                    f=i;
                    c=j;
                }
            }
        }

        //Si la celda ocupada esta en el primer cuadro
        if(f < x+n / 2 && c < y+n / 2){
            colocar(x + n / 2, y + (n / 2) - 1, x + n / 2,
                y + n / 2, x + n / 2 - 1, y + n / 2);
        }else if (f >= x + n / 2 && c < y + n / 2) {//Si la celda ocupada esta en el segundo cuadro
            colocar(x + (n / 2) - 1, y + (n / 2), x + (n / 2),
                y + n / 2, x + (n / 2) - 1, y + (n / 2) - 1);
        } else if(f < x + n / 2 && c >= y + n / 2){//Si la celda ocupada esta en el tercer cuadro
            colocar(x + n / 2, y + (n / 2) - 1, x + n / 2,
                y + n / 2, x + n / 2 - 1, y + n / 2 - 1);
        } else if(f >= x + n / 2 && c >= y + n / 2){//Si la celda ocupada esta en el cuarto cuadro
            colocar(x + (n / 2) - 1, y + (n / 2), x + (n / 2),
                y + (n / 2) - 1, x + (n / 2) - 1,
                y + (n / 2) - 1);
        }

        //Dividir nuevamente en 4 cuadrantes
        colocarAdoquines(n / 2, x, y + n / 2);
        colocarAdoquines(n / 2, x, y);
        colocarAdoquines(n / 2, x + n / 2, y);
        colocarAdoquines(n / 2, x + n / 2, y + n / 2);

    }


    public static void main(String[] args){
        if(args.length != 1){
            System.out.println("Ejecutar: java Adoquin <k>");
            return;
        }

        int k;
        try{
            k = Integer.parseInt(args[0]);
        }catch(NumberFormatException e){
            System.out.println("Entrada no valida, proporciona un valor de k entero");
            return;
        }

        //Calculamos el tamano del tablero 2^k
        tamano_tablero = (int) Math.pow(2, k);

        //Iniciamos el arreglo tamano 2^k x 2^k
        tablero = new int[tamano_tablero][tamano_tablero];

        //Adoquin especial 
        tablero[0][0] = -1;

        colocarAdoquines(tamano_tablero, 0, 0 );

        //Se imprime el tablero finalizado
        System.out.println("Adoquin especial en la posicion (0,0) con valor -1");
        for(int i=0; i<tamano_tablero; i++){
            for(int j=0; j<tamano_tablero; j++){
                System.out.printf("%4d", tablero[i][j]);
            }
            System.out.println();
        }
    }
}
