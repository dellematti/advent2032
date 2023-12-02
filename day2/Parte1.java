

import java.io.File;
import java.util.Scanner;
import java.util.HashMap; 
import java.util.Map; 
import java.util.List; 
import java.util.ArrayList; 
import java.util.Arrays; 
import java.util.Collections; 

public class Parte1 {


    public static void main (String[] args) throws Exception {

        File file = new File(
            "input.txt");
        Scanner sc = new Scanner(file);

 
        int idGame = 0;
        boolean gameValido = false;
        int output = 0;
        while (sc.hasNextLine()) {
             String parola = sc.next();
            if (parola.equals("Game")) {
                if (gameValido) 
                    output += idGame;
                parola = sc.next();
                idGame = Integer.parseInt( parola.substring(0,parola.length()-1) );
                gameValido = true;
            }else {
                int quantità = Integer.parseInt(parola);
                String colore = sc.next().replaceAll("[,;]", "");
                // System.out.println(quantità + " " + colore);

                if (colore.equals("red") && quantità > 12) gameValido = false;
                if (colore.equals("green") && quantità > 13) gameValido = false;
                if (colore.equals("blue") && quantità > 14) gameValido = false;
            }


        }
        if (gameValido) 
            output += idGame;
        System.out.println(output);

    }


}