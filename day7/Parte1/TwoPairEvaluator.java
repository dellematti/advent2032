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
        // if (map.containsValue(2)) return HandRank.TWO_PAIR;
        int sum = 0;
        for (Map.Entry<Rank, Integer> entry : map.entrySet()) {
            if(entry.getValue() == 2 ) sum++;       
                // keySet.add(entry.getKey());
        }
        if( sum == 2 )return HandRank.TWO_PAIR;


        return next.handEvaluator(hand);
    }
}