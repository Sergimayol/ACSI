package src.CP.CP_p5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author Sergi
 */
public class MVA {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

    }

    public static void MeanValueAnalysis(int N, int Z, int K, double[] Si, int[] Vi) {
        Double[] Ni = new Double[K];
        Double[] Ri = new Double[K];
        Double[] Xi = new Double[K];
        double X0 = 0.0;
        double[] Di = new double[K];
        List<Double> _list_X0 = new ArrayList<Double>();
        List<Double> _list_R = new ArrayList<Double>();
        for (int i = 0; i < K; i++) {
            Di[i] = Si[i] * Vi[i];
        }
        for (int i = 0; i < K; i++) {
            Ni[i] = 0.0;
            Ri[i] = 0.0;
        }
        for (int n = 0; n < N; n++) {
            for (int i = 0; i < K; i++) {
                Ri[i] = Si[i] * (1 + Ni[i]);
            }
            double R = 0.0;
            for (int i = 0; i < K; i++) {
                R += Ri[i] * Vi[i];
            }
            _list_R.add(R);
            X0 = (n / (R + Z));
            _list_X0.add(X0);
            for (int i = 0; i < K; i++) {
                Ni[i] = (X0 * Vi[i] * Ri[i]);
                Xi[i] = (X0 * Vi[i]);
            }
            System.out.println("Xi: " + Arrays.toString(Xi));
            System.out.println("Ni: " + Arrays.toString(Ni));
            System.out.println("Ri: " + Arrays.toString(Ri));
            System.out.println("X0: " + X0);
            System.out.println("_list_R: " + _list_R);
            System.out.println("_list_X0: " + _list_X0);
            System.out.println("R: " + R);
        }
    }
}
