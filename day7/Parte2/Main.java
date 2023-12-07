import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.io.File;
import java.util.Scanner;
import java.util.*;

public class Main {

    public static Rank stringToCard ( String carta) {
        if ( carta.equals("J")) return Rank.JOLLY;
        if ( carta.equals("2")) return Rank.TWO;
        if ( carta.equals("3")) return Rank.THREE;
        if ( carta.equals("4")) return Rank.FOUR;
        if ( carta.equals("5")) return Rank.FIVE;
        if ( carta.equals("6")) return Rank.SIX;
        if ( carta.equals("7")) return Rank.SEVEN;
        if ( carta.equals("8")) return Rank.EIGHT;
        if ( carta.equals("9")) return Rank.NINE;
        if ( carta.equals("T")) return Rank.TEN;
        if ( carta.equals("Q")) return Rank.QUEEN;
        if ( carta.equals("K")) return Rank.KING;
        if ( carta.equals("A")) return Rank.ACE;
        throw new IllegalArgumentException("La carta" + carta + "non esiste");
    }



    public static void main(String[] args) throws Exception {
        List<PokerHand> mani = new ArrayList<PokerHand>();


        File file = new File(
            "input.txt");
        Scanner sc = new Scanner(file);

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            Card carta;
            List<Card> carte = new ArrayList<Card>();
            for (int i = 0; i< 5; i++) {
                carta = new Card(stringToCard(String.valueOf(line.charAt(i))));
                carte.add(carta);
            }
            PokerHand mano = new PokerHand(carte);
            // per comodità aggiungo anche il valore a pokerhand come parametro       
            int bid = Integer.parseInt(line.substring(6,line.length()));

            mano.setBid(bid);
            mani.add(mano);
        }




        Collections.sort(mani, new Comparator<PokerHand>() {
            @Override
            public int compare(PokerHand mano1, PokerHand mano2) {
                if(mano1.getRank().ordinal() > mano2.getRank().ordinal() ) return 1;
                if(mano1.getRank().ordinal() < mano2.getRank().ordinal() ) return -1;
                Iterator<Card> iteratorMano1 = mano1.iterator();
                Iterator<Card> iteratorMano2 = mano2.iterator();

                for (int i = 0; i<5; i++) {
                    Card carta1 = iteratorMano1.next();
                    Card carta2 = iteratorMano2.next();
                    if(carta1.getRank().ordinal() > carta2.getRank().ordinal() ) return 1;
                    if(carta1.getRank().ordinal() < carta2.getRank().ordinal() ) return -1;
                }
                return 0;
            }
        });




        int output = 0;
        for( int i = 0; i< mani.size(); i++) {
            output += (mani.get(i).getBid() * (i+1));
        }

        // for(PokerHand mano: mani) {System.out.println(mano + "\t\t" + mano.getRank());}
        System.out.println(output);
        // 251003917   

    }

}