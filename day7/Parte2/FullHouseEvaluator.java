import java.util.HashMap;
import java.util.Map;

public class FullHouseEvaluator implements ChainedHandEvaluator{
    public ChainedHandEvaluator next;
    public FullHouseEvaluator(ChainedHandEvaluator nextEvaluator){
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
        if (map.containsValue(3) && map.containsValue(2)) return HandRank.FULL_HOUSE;

        // caso del jolly:
        int sum = 0;
        for (Map.Entry<Rank, Integer> entry : map.entrySet()) {
            if(entry.getValue() == 2 && entry.getKey() != Rank.JOLLY ) sum++;       
        }
        int numeroJolly = 0;
        if (map.containsKey(Rank.JOLLY)) numeroJolly = map.get(Rank.JOLLY);
        if( sum == 2 && numeroJolly == 1 )return HandRank.FULL_HOUSE;


        return next.handEvaluator(hand);
    }
}