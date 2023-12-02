import java.io.File;
import java.util.Scanner;

public class Parte2 {

    public static void main (String[] args) throws Exception {

        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
 
        int idGame = 0;
        int maxRed = 0;
        int maxGreen = 0;
        int maxBlue = 0;        
        int output = 0;
        while (sc.hasNextLine()) {
            String parola = sc.next();
            if (parola.equals("Game")) {
                parola = sc.next();
                idGame = Integer.parseInt( parola.substring(0,parola.length()-1) );
                output += (maxRed * maxGreen * maxBlue);
                maxRed = 0;
                maxGreen = 0;
                maxBlue = 0;
            }else {
                int quantità = Integer.parseInt(parola);
                String colore = sc.next().replaceAll("[,;]", "");
                // System.out.println(quantità + " " + colore);

                if (colore.equals("red") && quantità > maxRed) maxRed = quantità;
                if (colore.equals("green") && quantità > maxGreen) maxGreen = quantità;
                if (colore.equals("blue") && quantità > maxBlue) maxBlue = quantità;
            }
        }
        output += (maxRed * maxGreen * maxBlue);
        System.out.println(output);
    }

}