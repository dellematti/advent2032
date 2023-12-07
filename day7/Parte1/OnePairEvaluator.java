import java.util.HashMap;

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
        if (map.containsValue(2)) return HandRank.ONE_PAIR;
        return next.handEvaluator(hand);
    }
}