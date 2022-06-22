package src.Utilities;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author Sergi
 */
public class CpuMem {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        ArrayList<String> cpu = new ArrayList<String>();
        ArrayList<String> mem = new ArrayList<String>();
        String aux;
        for (int i = 0; i < 12; i++) {
            aux = s.nextLine();
            cpu.add(aux);
            aux = s.nextLine();
            mem.add(aux);
        }
        System.out.println("\n\n\n");
        for (int i = 0; i < cpu.size(); i++) {
            System.out.println(cpu.get(i));
        }
        for (int i = 0; i < mem.size(); i++) {
            System.out.println(mem.get(i));
        }
        s.close();
    }

}
