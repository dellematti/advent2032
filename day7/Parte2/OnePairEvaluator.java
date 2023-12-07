import java.util.HashMap;
import java.util.Map;

public class OnePairEvaluator implements ChainedHandEvaluator{
    public ChainedHandEvaluator next;
    public OnePairEvaluator(ChainedHandEvaluator nextEvaluator){
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
        if (map.containsValue(2)) return HandRank.ONE_PAIR;
        
        for (Map.Entry<Rank, Integer> entry : map.entrySet()) {
            if(entry.getValue() == 2-numeroJolly && entry.getKey() != Rank.JOLLY ) return HandRank.ONE_PAIR;       
        }


        return next.handEvaluator(hand);
    }
}