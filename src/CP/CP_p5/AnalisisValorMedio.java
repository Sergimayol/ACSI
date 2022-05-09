package borrador;

/**
 *
 * @author Sergi
 */
public class AnalisisValorMedio {

    private final int n;
    //Razón de visita
    private final int[] V;
    //Tiempo de servicio
    private final double[] S;
    //Número de dispositivos
    private final int NUM_DISPOSITIVOS;

    public AnalisisValorMedio(int n, int[] v, double[] s) {
        this.n = n;
        this.V = v;
        this.S = s;
        this.NUM_DISPOSITIVOS = v.length;
    }

    public double ecRi(int i) {
//        if (this.n == 0) {
//            return this.S[i];
//        }
        return (ecN(i, n - 1) + 1) * this.S[i];
    }

    public double ecR() {
        double r = 0;
        for (int i = 0; i < this.NUM_DISPOSITIVOS; i++) {
            r += this.V[i] * ecRi(i);
        }
        return r;
    }

    public double ecN(int i, int n) {
//        return ecX(int n) * this.V[i] * 
    }

    public double ecX() {
        return
    }

    public double ecXi() {
        return
    }

    public double ecU() {
        return
    }
}
