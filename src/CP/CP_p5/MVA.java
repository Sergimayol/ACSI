package src.CP.CP_p5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author Sergi
 */
public class MVA {

    public static void main(String[] args) {
        try {
            new MVA().test1();
            new MVA().test2();
            new MVA().test3();
        } catch (Exception ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }

    private void test1() {
        System.out.println("--------- TEST 1 ---------");
        int N = 3 + 1;
        int Z = 5;
        int K = 2;
        double[] Si = { 0.03, 0.5 };
        int[] Vi = { 15, 14 };
        MeanValueAnalysis(N, Z, K, Si, Vi);
    }

    private void test2() {
        System.out.println("\n\n\n--------- TEST 2 ---------");
        int N = 10 + 1;
        int Z = 5;
        int K = 2;
        double[] Si = { 0.03, 0.1 };
        int[] Vi = { 8, 7 };
        MeanValueAnalysis(N, Z, K, Si, Vi);
    }

    private void test3() {
        System.out.println("\n\n\n--------- TEST 3 ---------");
        int N = 5 + 1;
        int Z = 2;
        int K = 2;
        double[] Si = { 0.1, 0.2 };
        int[] Vi = { 8, 7 };
        MeanValueAnalysis(N, Z, K, Si, Vi);
    }

    public static void MeanValueAnalysis(int N, int Z, int K, double[] Si, int[] Vi) {
        Double[] Ni = new Double[K];
        Double[] Ri = new Double[K];
        Double[] Xi = new Double[K];
        Double[] Ui = new Double[K];
        double X0 = 0.0;
        double[] Di = new double[K];
        double D = 0;
        List<Double> _list_X0 = new ArrayList<Double>();
        List<Double> _list_R = new ArrayList<Double>();
        for (int i = 0; i < K; i++) {
            Di[i] = Si[i] * Vi[i];
            D += Di[i];
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
                Ui[i] = (X0 * Vi[i] * Si[i]);
                Xi[i] = (X0 * Vi[i]);
            }
            if (n != 0) {
                System.out.println("Trabajo: " + n);
                System.out.println("Xi: " + Arrays.toString(Xi));
                System.out.println("Ni: " + Arrays.toString(Ni));
                System.out.println("Ri: " + Arrays.toString(Ri));
                System.out.println("Ui: " + Arrays.toString(Ui));
                System.out.println("X0: " + X0);
                System.out.println("R: " + R);
                System.out.println("");
            }
        }
    }
}
