import java.io.File;
import java.util.Scanner;
import java.util.HashMap; 
import java.util.Map; 
import java.util.List; 
import java.util.ArrayList; 
import java.util.Arrays; 
import java.util.Collections; 

public class Parte2 {

    public static boolean isInteger(String numero) {
        if (numero == null) return false;
        try {
            Integer.parseInt(numero);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }


    public static int stringNumberToInt(String numero) {
        switch(numero) {
            case "one":
                return 1;
            case "two":
                return 2;
            case "three":
                return 3;
            case "four":
                return 4;
            case "five":
                return 5;
            case "six":
                return 6;
            case "seven":
                return 7;
            case "eight":
                return 8;
            case "nine":
                return 9;
        }
        throw new IllegalArgumentException("Eh no ehh");
    }


    public static void main (String[] args) throws Exception {

        File file = new File("input.txt");
        Scanner sc = new Scanner(file);

        int primo = 0;
        int secondo = 0;
        int primaPosizione = Integer.MAX_VALUE;
        int secondaPosizione = 0;
        
        int sum = 0;
        while (sc.hasNextLine()) {
            String riga = sc.nextLine();

            Map<String,Integer> numToIndexFirst = new HashMap<String,Integer>();
            Map<String,Integer> numToIndexLast = new HashMap<String,Integer>();
            ArrayList<String> numeri = new ArrayList<String>(Arrays.asList(
                "one","two","three","four","five","six","seven","eight","nine"));
            for (String numero : numeri) {
                if (riga.indexOf(numero) != -1)
                    numToIndexFirst.put(numero,riga.indexOf(numero));
                if (riga.lastIndexOf(numero) != -1)
                    numToIndexLast.put(numero,riga.lastIndexOf(numero));
            }

            if ( ! numToIndexFirst.isEmpty()) {
                String key = Collections.min(numToIndexFirst.entrySet(), Map.Entry.comparingByValue()).getKey();
                primo = stringNumberToInt(key);
                primaPosizione = numToIndexFirst.get(key);
            }
            if ( ! numToIndexLast.isEmpty()) {
                String key = Collections.max(numToIndexLast.entrySet(), Map.Entry.comparingByValue()).getKey();
                secondo = stringNumberToInt(key);
                secondaPosizione = numToIndexLast.get(key);
            }

            boolean primoModificato = false;
            for (int i = 0; i < riga.length(); i++) {
                String carattere = String.valueOf(riga.charAt(i));
                if (isInteger(carattere)) {
                    if( (primo == 0) || (i < primaPosizione && ! primoModificato)) {
                        primo = Integer.parseInt(carattere);
                        primoModificato = true;
                    }
                    if (i >= secondaPosizione) secondo = Integer.parseInt(carattere);
                }
            }
            sum += primo*10 + secondo;

            primo = 0;
            secondo = 0;
            primaPosizione = Integer.MAX_VALUE;
            secondaPosizione = 0;
        }
        System.out.println(sum);
    }
}
// 53348 soluzione