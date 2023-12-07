import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class PokerHand implements Iterable<Card> {
    private int bid;    // valore della scomessa serve per l advent e basta (oppure potrei fare una mappa)
    private final List<Card> cards = new ArrayList<>();
    private FiveOfAKindEvaluator evaluator =
            new FiveOfAKindEvaluator(
                new FourOfAKindEvaluator(
                    new FullHouseEvaluator(
                        new ThreeOfAKindEvaluator(
                            new TwoPairEvaluator(
                                new OnePairEvaluator(
                                    new HighCardEvaluator()))))));
                                

    public PokerHand( List<Card> cardList){
        if (cardList == null) throw new NullPointerException("Card list cannot be null");
        for (Card card: cardList ) {
            if (card == null) throw new NullPointerException("Card cannot be null");
            cards.add(card);
        }
    }

    @Override
    public  Iterator<Card> iterator () {
        return cards.iterator();
    }
    public HandRank getRank(){
        return evaluator.handEvaluator(this);
    }

    public void setBid(int bid) {
        this.bid = bid;
    }

    public int getBid() {
        return bid;
    }

    @Override
    public String toString() {
        String s ="";
        for(Card carta: cards) s += carta + " ";
        return s;
    }




}
