public class JuegoEscalera {
    
    public static Integer tirarDado() {
        return (Integer)Math.ceil(Math.random() * 6);
    }

    public static Integer sube(Integer pos) {
        if (pos == 3) {
            System.debug('Jugador sube por escalera al cuadro 11');
            pos = 11;
        } else if (pos == 6) {
            System.debug('Jugador sube por escalera al cuadro 17');
            pos = 17;
        } else if (pos == 9) {
            System.debug('Jugador sube por escalera al cuadro 18');
            pos = 18;
        } else if (pos == 10) {
            System.debug('Jugador sube por escalera al cuadro 12');
            pos = 12;
        }
        return pos;
    }

    public static Integer baja(Integer pos) {
        if (pos == 14) {
            System.debug('Jugador desciende al cuadro 4');
        } else if (pos == 19) {
            System.debug('Jugador desciende al cuadro 8');
            pos = 8;
        } else if (pos == 22) {
            System.debug('Jugador desciende al cuadro 20');
            pos = 20;
        } else if (pos == 24) {
            System.debug('Jugador desciende al cuadro 16');
            pos = 16;
        }
        return pos;
    }

    public static void main() {
        Integer pos = 1;
        System.debug('Bienvenido al juego de la escalera');

        while (pos < 25) {
            Integer numeroDado = tirarDado();
            System.debug('Dado arroja ' + numeroDado);
            pos += numeroDado;
            if (pos > 25) {
                System.debug('Jugador supera el cuadro 25');
                break;
            }
            System.debug('Jugador avanza a cuadro ' + pos);
            if (pos == 3 || pos == 6 || pos == 9 || pos == 10) {
                pos = sube(pos);
            }
            if (pos == 14 || pos == 19 || pos == 22 || pos == 24) {
                pos = baja(pos);
            }
        }
        System.debug('Fin');
    }
}
