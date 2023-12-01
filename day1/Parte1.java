import java.io.File;
import java.util.Scanner;

public class Parte1 {

    public static boolean isInteger(String numericValue) {
        if (numericValue == null) return false;
        try {
            Integer.parseInt(numericValue);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }


    public static void main (String[] args) throws Exception {

        File file = new File(
            "input.txt");
        Scanner sc = new Scanner(file);

        int primo = 0;
        int secondo = 0;
        int sum = 0;

        String riga = "";
        while (sc.hasNextLine()) {
            riga = sc.nextLine();
            for (int i = 0; i < riga.length(); i++) {
                String carattere = String.valueOf(riga.charAt(i));
                if (isInteger(carattere)) {
                    if(primo == 0) primo = Integer.parseInt(carattere);
                    secondo = Integer.parseInt(carattere);
                }
            }
        sum += primo*10 + secondo;
        primo = 0;
        secondo = 0;
        }
        System.out.println(sum);
    }
}