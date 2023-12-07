import java.util.HashMap;

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
        return next.handEvaluator(hand);
    }
}