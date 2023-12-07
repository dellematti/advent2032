import java.util.HashMap;
import java.util.Map;

public class TwoPairEvaluator implements ChainedHandEvaluator{
    public ChainedHandEvaluator next;
    public TwoPairEvaluator(ChainedHandEvaluator nextEvaluator){
        next = nextEvaluator;
    }
    @Override
    public HandRank handEvaluator(PokerHand hand) {
        HashMap<Rank, Integer> map = new HashMap<>();
        for(Card card : hand){
            Rank rank = card.getRank();
            if(map.containsKey(rank)) {
                map.put(rank, map.get(rank)+1);
            }else{
                map.put(rank, 1);
            }
        }


        int sum = 0;
        for (Map.Entry<Rank, Integer> entry : map.entrySet()) {
            if(entry.getValue() == 2 ) sum++;       
        }
        if( sum == 2 )return HandRank.TWO_PAIR;
        // perde di senso se ho una coppia di jolly e una coppia di altro. Sceglierei un poker, no una doppia-coppia


        // ANCHE SE NON SUCCEDERÀ MAI IL CASO DEI JOLLY NEL TWO-PAIR, SEGUENDO L ORDINE STANDARD SI VA SEMPRE A
        // PREFERIRE UN TRIS RISPETTO A DUE COPPIE
        
        int numeroJolly = 0;
        if (map.containsKey(Rank.JOLLY)) numeroJolly = map.get(Rank.JOLLY);
        if (sum == 1 && numeroJolly == 1) return HandRank.TWO_PAIR;

        return next.handEvaluator(hand);
    }
}