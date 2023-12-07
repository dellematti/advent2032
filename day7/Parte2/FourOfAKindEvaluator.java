import java.util.HashMap;
import java.util.Map;

public class FourOfAKindEvaluator implements ChainedHandEvaluator{
    public ChainedHandEvaluator next;
    public FourOfAKindEvaluator(ChainedHandEvaluator nextEvaluator){
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
        int numeroJolly = 0;
        if (map.containsKey(Rank.JOLLY))
            numeroJolly = map.get(Rank.JOLLY); 
            // contiene due jolly e il numero è 2, quindi fa 4 solo coi jolly !!!!!!


        if (map.containsValue(4)) return HandRank.FOUR_OF_A_KIND;
        
        
        for (Map.Entry<Rank, Integer> entry : map.entrySet()) {
            if(entry.getValue() == 4-numeroJolly && entry.getKey() != Rank.JOLLY ) return HandRank.FOUR_OF_A_KIND;       
        }


        return next.handEvaluator(hand);
    }
}

